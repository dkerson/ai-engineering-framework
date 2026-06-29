# Token Metrics

> Lightweight metrics for reducing Codex/Cursor cost without weakening delivery quality.

## Budget Bands

| Mode | Target Behavior | Cost Guardrail |
|------|-----------------|----------------|
| Fast | Answer, inspect or edit minimally. | No full NLME unless ambiguity/risk requires it. |
| Standard | Targeted implementation with module validation. | Read only direct files, imports and related tests. |
| Review | Multi-file or risky work with critic/validator. | Justify every extra specialist and broad validation. |
| Technical Council | High-risk architecture, auth, database, production or incident. | Council only when criteria are met; max 150 words per specialist. |

## Mission Metrics

| Date | Mission | Mode | Files Read | Skills Used | Validation | Waste Signals | Savings |
|------|---------|------|------------|-------------|------------|---------------|---------|
| 2026-06-29 | Context Hygiene Protocol | Review | 12 | 1 | diff/status | Context pollution lacked explicit operational handling | Compacted Snapshot prevents stale outputs from guiding later phases |
| 2026-06-28 | Execution Intelligence setup | Review | 8 | 3 | diff/status | Inventory drift found; no script yet | No code scan beyond framework docs |

## Waste Signals

- NLME full path used for a simple command or confirmation.
- More than 5 skills used in Standard mode without hybrid/risk reason.
- More than 12 files read before first hypothesis.
- Build or full suite run for a small documentation/framework edit.
- Same file re-read by multiple skills instead of using Working Context.
- Long execution continues from stale plans, raw outputs or invalidated hypotheses.

## Savings Signals

- Fast Path selected before full mission pipeline.
- Registry answered infrastructure/plugin/capability question.
- Search narrowed files before reading.
- Validation scoped to changed module.
- Final response summarized instead of replaying all analysis.
- Compacted Snapshot becomes the active context source after pollution is detected.
