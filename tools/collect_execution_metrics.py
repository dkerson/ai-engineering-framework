#!/usr/bin/env python3
"""Collect AI Engineering Framework usage metrics from lightweight ledgers.

The script reads local FOS ledgers, generates a usage report, and can publish
sanitized contributor snapshots to a shared telemetry repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


LEDGER_DIR = Path("framework") / "operating-system"
REPORTS_DIR = LEDGER_DIR / "reports"
LEDGER_FILES = [
    "MISSION_LEDGER.md",
    "EXECUTION_METRICS.md",
    "TOKEN_METRICS.md",
    "SKILL_USAGE.md",
    "EXECUTION_MEMORY_INDEX.md",
]


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def read_markdown_table(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []

    rows: list[dict[str, str]] = []
    headers: list[str] | None = None

    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            headers = None
            continue

        cells = split_markdown_row(line)
        if is_separator_row(cells):
            continue

        if headers is None:
            headers = cells
            continue

        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))
        rows.append(dict(zip(headers, cells)))

    return rows


def parse_int(value: str) -> int:
    match = re.search(r"-?\d+", value or "")
    return int(match.group(0)) if match else 0


def weighted_savings(baseline: int, actual: int) -> int:
    if baseline <= 0:
        return 0
    pct = round(((baseline - actual) / baseline) * 100)
    return max(0, min(95, pct))


def normalize_user_id(user: str, anonymize: bool) -> str:
    clean = re.sub(r"[^A-Za-z0-9_.-]+", "-", user.strip() or "unknown").strip("-")
    if not anonymize:
        return clean or "unknown"
    digest = hashlib.sha256(clean.lower().encode("utf-8")).hexdigest()[:12]
    return f"user-{digest}"


def dedupe_rows(rows: Iterable[dict[str, str]], keys: list[str]) -> list[dict[str, str]]:
    seen: set[tuple[str, ...]] = set()
    result: list[dict[str, str]] = []
    for row in rows:
        key = tuple(row.get(k, "") for k in keys)
        if key in seen:
            continue
        seen.add(key)
        result.append(row)
    return result


def filter_rows(rows: list[dict[str, str]], required_columns: list[str]) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if all(column in row for column in required_columns)
        and all(row.get(column, "").strip() for column in required_columns[:2])
    ]


@dataclass
class MetricsSummary:
    mission_count: int
    done_count: int
    execution_count: int
    baseline_units: int
    actual_units: int
    estimated_savings_pct: int
    retries_avoided: int
    errors_avoided: int
    modes: Counter
    surfaces: Counter
    models: Counter
    skills: Counter
    waste_signals: list[str]
    savings_signals: list[str]
    promotion_review_due: bool
    promotion_review_reason: str


def summarize(
    mission_rows: list[dict[str, str]],
    execution_rows: list[dict[str, str]],
    token_rows: list[dict[str, str]],
    skill_rows: list[dict[str, str]],
    promotion_cadence: int,
) -> MetricsSummary:
    mission_rows = dedupe_rows(
        mission_rows,
        ["Date", "Project", "Mission", "Type", "Mode", "Outcome"],
    )
    execution_rows = dedupe_rows(
        execution_rows,
        ["Date", "Mission", "Surface", "Mode", "Baseline Units", "Actual Units"],
    )

    baseline = sum(parse_int(row.get("Baseline Units", "")) for row in execution_rows)
    actual = sum(parse_int(row.get("Actual Units", "")) for row in execution_rows)
    retries = sum(parse_int(row.get("Retries Avoided", "")) for row in execution_rows)
    errors = sum(parse_int(row.get("Errors Avoided", "")) for row in execution_rows)

    modes: Counter = Counter()
    surfaces: Counter = Counter()
    models: Counter = Counter()
    skills: Counter = Counter()

    for row in mission_rows:
        if row.get("Mode"):
            modes[row["Mode"]] += 1

    if not modes:
        for row in execution_rows:
            if row.get("Mode"):
                modes[row["Mode"]] += 1

    for row in execution_rows:
        if row.get("Surface"):
            surfaces[row["Surface"]] += 1
        if row.get("Recommended Model"):
            models[row["Recommended Model"]] += 1

    for row in skill_rows:
        skill = row.get("Skill", "")
        if skill:
            skills[skill.strip("` ")] += parse_int(row.get("Count", "1")) or 1

    if not skills:
        for row in mission_rows:
            for skill in re.split(r",\s*", row.get("Skills", "")):
                if skill and skill != "-":
                    skills[skill.strip("` ")] += 1

    waste_signals = [
        row.get("Waste Signals", "").strip()
        for row in token_rows
        if row.get("Waste Signals", "").strip()
    ]
    savings_signals = [
        row.get("Savings", "").strip()
        for row in token_rows
        if row.get("Savings", "").strip()
    ]

    mission_count = len(mission_rows)
    if mission_count == 0:
        due = False
        reason = "No missions recorded."
    elif mission_count >= promotion_cadence and mission_count % promotion_cadence == 0:
        due = True
        reason = f"{mission_count} missions reached cadence of {promotion_cadence}."
    elif mission_count >= promotion_cadence:
        due = False
        remaining = promotion_cadence - (mission_count % promotion_cadence)
        reason = f"{remaining} mission(s) until next {promotion_cadence}-mission review."
    else:
        due = False
        reason = f"{promotion_cadence - mission_count} mission(s) until first review."

    return MetricsSummary(
        mission_count=mission_count,
        done_count=sum(1 for row in mission_rows if row.get("Outcome", "").lower() == "done"),
        execution_count=len(execution_rows),
        baseline_units=baseline,
        actual_units=actual,
        estimated_savings_pct=weighted_savings(baseline, actual),
        retries_avoided=retries,
        errors_avoided=errors,
        modes=modes,
        surfaces=surfaces,
        models=models,
        skills=skills,
        waste_signals=waste_signals,
        savings_signals=savings_signals,
        promotion_review_due=due,
        promotion_review_reason=reason,
    )


def counter_table(counter: Counter, empty_label: str) -> str:
    if not counter:
        return f"| Item | Count |\n|------|-------|\n| {empty_label} | 0 |"
    lines = ["| Item | Count |", "|------|-------|"]
    for item, count in counter.most_common():
        lines.append(f"| {item} | {count} |")
    return "\n".join(lines)


def bullet_list(items: list[str], empty_label: str, limit: int = 10) -> str:
    unique: list[str] = []
    seen: set[str] = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    if not unique:
        return f"- {empty_label}"
    return "\n".join(f"- {item}" for item in unique[:limit])


def render_report(
    summary: MetricsSummary,
    *,
    scope: str,
    project: str,
    team: str,
    generated_at: str,
    source: str,
) -> str:
    promotion = "yes" if summary.promotion_review_due else "no"
    return f"""# Usage Report

## Scope
- Team: {team}
- Project: {project}
- Scope: {scope}
- Generated at: {generated_at}
- Source: {source}

## Data Quality
- Measurement type: estimated operational units, not real tokens.
- Confidence: Media, unless the active surface exposes real token telemetry.
- Privacy: reports must not include prompts, secrets, long code excerpts or private data.

## Executive Summary
- Missions recorded: {summary.mission_count}
- Done missions: {summary.done_count}
- Structured execution entries: {summary.execution_count}
- Baseline units: {summary.baseline_units}
- Actual units: {summary.actual_units}
- Estimated savings: {summary.estimated_savings_pct}%
- Retries avoided: {summary.retries_avoided}
- Errors avoided: {summary.errors_avoided}
- Promotion review due: {promotion}
- Promotion review reason: {summary.promotion_review_reason}

## Usage By Mode
{counter_table(summary.modes, "No mode data")}

## Usage By Surface
{counter_table(summary.surfaces, "No surface data")}

## Recommended Models
{counter_table(summary.models, "No model data")}

## Skill Usage
{counter_table(summary.skills, "No skill data")}

## Waste Signals
{bullet_list(summary.waste_signals, "No waste signals recorded.")}

## Savings Signals
{bullet_list(summary.savings_signals, "No savings signals recorded.")}

## Recommended Actions
- Keep ledgers short and evidence-based.
- Run this collector after executable framework missions.
- Review promotion candidates every 10 real missions or earlier on repeated critical failures.
- Do not convert estimated units into money or real tokens without trustworthy telemetry.
"""


def load_local_ledgers(root: Path) -> dict[str, list[dict[str, str]]]:
    fos = root / LEDGER_DIR
    return {
        "missions": filter_rows(read_markdown_table(fos / "MISSION_LEDGER.md"), ["Date", "Project", "Mission"]),
        "executions": filter_rows(read_markdown_table(fos / "EXECUTION_METRICS.md"), ["Date", "Mission", "Baseline Units"]),
        "tokens": filter_rows(read_markdown_table(fos / "TOKEN_METRICS.md"), ["Date", "Mission", "Waste Signals"]),
        "skills": filter_rows(read_markdown_table(fos / "SKILL_USAGE.md"), ["Skill", "Count"]),
    }


def collect_contributor_ledgers(project_dir: Path) -> dict[str, list[dict[str, str]]]:
    result = {"missions": [], "executions": [], "tokens": [], "skills": []}
    contributors = project_dir / "contributors"
    if not contributors.exists():
        return result

    for contributor in contributors.iterdir():
        if not contributor.is_dir():
            continue
        result["missions"].extend(filter_rows(read_markdown_table(contributor / "MISSION_LEDGER.md"), ["Date", "Project", "Mission"]))
        result["executions"].extend(filter_rows(read_markdown_table(contributor / "EXECUTION_METRICS.md"), ["Date", "Mission", "Baseline Units"]))
        result["tokens"].extend(filter_rows(read_markdown_table(contributor / "TOKEN_METRICS.md"), ["Date", "Mission", "Waste Signals"]))
        result["skills"].extend(filter_rows(read_markdown_table(contributor / "SKILL_USAGE.md"), ["Skill", "Count"]))
    return result


def collect_team_ledgers(telemetry_root: Path) -> dict[str, list[dict[str, str]]]:
    result = {"missions": [], "executions": [], "tokens": [], "skills": []}
    projects = telemetry_root / "projects"
    if not projects.exists():
        return result

    for project_dir in projects.iterdir():
        if not project_dir.is_dir():
            continue
        project = collect_contributor_ledgers(project_dir)
        for key in result:
            result[key].extend(project[key])
    return result


def copy_ledgers(root: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for name in LEDGER_FILES:
        source = root / LEDGER_DIR / name
        if source.exists():
            shutil.copy2(source, destination / name)


def write_json_summary(path: Path, summary: MetricsSummary, metadata: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    unique_waste = list(dict.fromkeys(summary.waste_signals))
    unique_savings = list(dict.fromkeys(summary.savings_signals))
    data = {
        "metadata": metadata,
        "scope": metadata.get("scope", ""),
        "project": metadata.get("project", ""),
        "team": metadata.get("team", ""),
        "generated_at": metadata.get("generated_at", ""),
        "mission_count": summary.mission_count,
        "done_count": summary.done_count,
        "execution_count": summary.execution_count,
        "baseline_units": summary.baseline_units,
        "actual_units": summary.actual_units,
        "estimated_savings_pct": summary.estimated_savings_pct,
        "retries_avoided": summary.retries_avoided,
        "errors_avoided": summary.errors_avoided,
        "promotion_review_due": summary.promotion_review_due,
        "promotion_review_reason": summary.promotion_review_reason,
        "mode_counts": dict(summary.modes.most_common()),
        "surface_counts": dict(summary.surfaces.most_common()),
        "model_counts": dict(summary.models.most_common()),
        "skill_counts": dict(summary.skills.most_common()),
        "waste_signals": unique_waste,
        "savings_signals": unique_savings,
        "data_quality": {
            "measurement_type": "estimated operational units, not real tokens",
            "confidence": "Media",
            "privacy": "No prompts, secrets, long code excerpts or private data",
        },
    }
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect framework usage metrics.")
    parser.add_argument("--framework-root", default=".", help="Path to the framework repository.")
    parser.add_argument("--project", default="framework", help="Project key for reports.")
    parser.add_argument("--team", default="Otus7", help="Team or organization name.")
    parser.add_argument("--telemetry-root", help="Optional shared telemetry repository path.")
    parser.add_argument("--publish", action="store_true", help="Publish sanitized contributor ledgers to telemetry root.")
    parser.add_argument("--user", default=os.environ.get("USERNAME") or os.environ.get("USER") or "unknown")
    parser.add_argument("--no-anonymize-user", action="store_true", help="Store the user name instead of a hash.")
    parser.add_argument("--promotion-cadence", type=int, default=10)
    args = parser.parse_args()

    root = Path(args.framework_root).resolve()
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_id = normalize_user_id(args.user, anonymize=not args.no_anonymize_user)

    local_ledgers = load_local_ledgers(root)
    local_summary = summarize(
        local_ledgers["missions"],
        local_ledgers["executions"],
        local_ledgers["tokens"],
        local_ledgers["skills"],
        args.promotion_cadence,
    )

    local_report = render_report(
        local_summary,
        scope="local",
        project=args.project,
        team=args.team,
        generated_at=generated_at,
        source=str(root / LEDGER_DIR),
    )
    local_report_path = root / REPORTS_DIR / "USAGE_REPORT.md"
    local_report_path.parent.mkdir(parents=True, exist_ok=True)
    local_report_path.write_text(local_report, encoding="utf-8")
    write_json_summary(
        root / REPORTS_DIR / "USAGE_REPORT.json",
        local_summary,
        {
            "scope": "local",
            "project": args.project,
            "team": args.team,
            "generated_at": generated_at,
        },
    )

    if args.telemetry_root:
        telemetry_root = Path(args.telemetry_root).resolve()
        project_dir = telemetry_root / "projects" / args.project

        if args.publish:
            contributor_dir = project_dir / "contributors" / user_id
            copy_ledgers(root, contributor_dir)
            contributor_report = render_report(
                local_summary,
                scope="contributor",
                project=args.project,
                team=args.team,
                generated_at=generated_at,
                source=str(contributor_dir),
            )
            (contributor_dir / "USAGE_REPORT.md").write_text(contributor_report, encoding="utf-8")
            write_json_summary(
                contributor_dir / "USAGE_REPORT.json",
                local_summary,
                {
                    "scope": "contributor",
                    "project": args.project,
                    "team": args.team,
                    "generated_at": generated_at,
                    "user_id": user_id,
                },
            )

        project_ledgers = collect_contributor_ledgers(project_dir)
        if project_ledgers["missions"] or project_ledgers["executions"]:
            project_summary = summarize(
                project_ledgers["missions"],
                project_ledgers["executions"],
                project_ledgers["tokens"],
                project_ledgers["skills"],
                args.promotion_cadence,
            )
            project_report = render_report(
                project_summary,
                scope="project",
                project=args.project,
                team=args.team,
                generated_at=generated_at,
                source=str(project_dir / "contributors"),
            )
            project_reports = project_dir / "reports"
            project_reports.mkdir(parents=True, exist_ok=True)
            (project_reports / "USAGE_REPORT.md").write_text(project_report, encoding="utf-8")
            write_json_summary(
                project_reports / "USAGE_REPORT.json",
                project_summary,
                {
                    "scope": "project",
                    "project": args.project,
                    "team": args.team,
                    "generated_at": generated_at,
                },
            )

        team_ledgers = collect_team_ledgers(telemetry_root)
        if team_ledgers["missions"] or team_ledgers["executions"]:
            team_summary = summarize(
                team_ledgers["missions"],
                team_ledgers["executions"],
                team_ledgers["tokens"],
                team_ledgers["skills"],
                args.promotion_cadence,
            )
            team_report = render_report(
                team_summary,
                scope="team",
                project="all",
                team=args.team,
                generated_at=generated_at,
                source=str(telemetry_root / "projects"),
            )
            team_reports = telemetry_root / "team" / "reports"
            team_reports.mkdir(parents=True, exist_ok=True)
            (team_reports / "USAGE_REPORT.md").write_text(team_report, encoding="utf-8")
            write_json_summary(
                team_reports / "USAGE_REPORT.json",
                team_summary,
                {
                    "scope": "team",
                    "project": "all",
                    "team": args.team,
                    "generated_at": generated_at,
                },
            )

    print(f"Local usage report: {local_report_path}")
    if args.telemetry_root:
        print(f"Telemetry root: {Path(args.telemetry_root).resolve()}")
        if args.publish:
            print(f"Published contributor: {user_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
