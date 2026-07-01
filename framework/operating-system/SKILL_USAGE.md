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
| orchestrator | 6 | framework-operating-system, token-savings-report | 2026-07-01 | Required entry point; added routing, reporting, metrics, learning loop and governance protocols. |
| rag-evaluator | 1 | framework-operating-system, capability-mission | 2026-07-01 | Used conceptually to promote Umbra RAG evidence into Stable Candidate guardrails. |
| knowledge-curator | 1 | framework-operating-system, knowledge-mission | 2026-07-01 | Used conceptually to define unanswered-question and wrong-citation curation loop. |
| skill-creator | 1 | framework-operating-system | 2026-06-29 | Used to guide creation of Security Intelligence skills. |
| security-review | 1 | security-intelligence | 2026-06-29 | Refined into general reviewer that delegates SI depth to specialists. |
| framework-reviewer | 1 | framework-operating-system | 2026-06-28 | Used to assess FOS health and drift. |
| framework-optimizer | 1 | framework-operating-system | 2026-06-28 | Used to design token efficiency improvements. |

## Review Heuristics

| Signal | Action |
|--------|--------|
| 0 uses after 20 relevant missions | Mark as dormant candidate. |
| Same skill pair used together in 5 missions | Consider pattern or combined workflow. |
| 3 skills produce overlapping recommendations | Review for merge, clearer boundaries or deprecation. |
| Skill frequently escalates mode without risk evidence | Review trigger rules. |
