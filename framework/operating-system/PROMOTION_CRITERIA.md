# Promotion Criteria

> Evidence thresholds for turning repeated observations into framework improvements.

## Principle

The framework may observe every execution, but it must not change itself automatically. It recommends, waits for user approval, then implements and versions the change.

## Thresholds

| Evidence | Candidate Action |
|----------|------------------|
| 2 similar missions | Add note to `LEARNING.md`. |
| 3 similar successful missions | Add candidate pattern to `PATTERNS.md`. |
| 5 similar successful missions | Propose workflow/template update in `RECOMMENDATIONS.md`. |
| 8 similar missions using same skill cluster | Review skill boundaries and possible consolidation. |
| 10 similar missions with stable outcome | Consider capability/workflow formalization. |
| 3 repeated token waste signals | Add backlog item or tighten trigger rule. |
| 2 failed/blocked missions for same cause | Add risk note and validator checklist. |

## Promotion Workflow

1. Record evidence in `MISSION_LEDGER.md`.
2. Summarize learning in `LEARNING.md`.
3. Add recommendation with impact, effort and risk.
4. Ask user approval before implementation.
5. If approved, update docs/rules/templates.
6. Update `CHANGELOG.md`, `VERSION` when release-worthy, and FOS status.
