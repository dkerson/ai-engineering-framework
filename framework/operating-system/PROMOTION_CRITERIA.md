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
| 1 high-severity production correction | Add immediate recommendation and risk note. |
| 1 real consumer project validates a capability | Mark capability as Stable Candidate, not Stable. |
| 1 duplicate-data/RAG citation bug in production | Add canonical identity requirement to RAG checklists. |

## Active Review Cadence

Run a promotion review every 10 real missions.

Early review is allowed when any critical signal appears:

- 2 failed or blocked missions for the same cause;
- 3 repeated token waste signals;
- 2 repeated hallucination/evidence failures;
- 2 repeated validations that passed but did not prove the real outcome;
- 1 high-risk security, data, production or authorization anti-pattern.

The review must inspect `EXECUTION_MEMORY_INDEX.md`, `MISSION_LEDGER.md`, `EXECUTION_METRICS.md`, `TOKEN_METRICS.md`, `LEARNING.md`, `PATTERNS.md` and `ANTI_PATTERNS.md`.

Outcome must be one of:

- no action;
- learning note;
- pattern candidate;
- anti-pattern update;
- recommendation;
- backlog item;
- approved implementation plan for user confirmation.

## Promotion Workflow

1. Record evidence in `MISSION_LEDGER.md`.
2. Summarize learning in `LEARNING.md`.
3. Add recommendation with impact, effort and risk.
4. Ask user approval before implementation.
5. If approved, update docs/rules/templates.
6. Update `CHANGELOG.md`, `VERSION` when release-worthy, and FOS status.

## Promotion Status

| Status | Meaning |
|--------|---------|
| observed | Evidence captured; no framework behavior change yet. |
| recommended | Concrete improvement proposed for user approval. |
| approved | User approved implementation. |
| implemented | Framework artifact changed and validated. |
| rejected | Not adopted or superseded. |

## Capability Promotion

Capabilities move through:

```text
Idea -> Planned -> In Development -> Ready -> Stable Candidate -> Stable
```

`Ready` means the framework has a design and guardrails.
`Stable Candidate` means at least one real consumer project produced evidence.
`Stable` requires reusable checklists, validation examples and no open critical lessons from the consumer evidence.
