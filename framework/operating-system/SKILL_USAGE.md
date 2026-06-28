# Skill Usage

> Tracks real skill usage by mission type so redundant or costly skills can be reviewed with evidence.

## Policy

- Update after missions when skills were materially used.
- Do not count skills merely mentioned in docs.
- Use approximate counts; exact automation can be added later if approved.
- Review monthly or after every 20 missions, whichever comes first.

## Usage Table

| Skill | Count | Mission Types | Last Used | Notes |
|-------|-------|---------------|-----------|-------|
| orchestrator | 1 | framework-operating-system | 2026-06-28 | Required entry point. |
| framework-reviewer | 1 | framework-operating-system | 2026-06-28 | Used to assess FOS health and drift. |
| framework-optimizer | 1 | framework-operating-system | 2026-06-28 | Used to design token efficiency improvements. |

## Review Heuristics

| Signal | Action |
|--------|--------|
| 0 uses after 20 relevant missions | Mark as dormant candidate. |
| Same skill pair used together in 5 missions | Consider pattern or combined workflow. |
| 3 skills produce overlapping recommendations | Review for merge, clearer boundaries or deprecation. |
| Skill frequently escalates mode without risk evidence | Review trigger rules. |
