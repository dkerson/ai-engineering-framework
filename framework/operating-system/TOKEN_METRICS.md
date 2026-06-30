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
| 2026-06-29 | MCP Portability & Local Secrets | Review | 12 | 2 | rg/git diff | MCP examples used older local/package assumptions | Remote OAuth and npx templates reduce local setup failures |
| 2026-06-29 | Configuration & Hardcode Governance | Review | 16 | 4 | rg/git diff | Existing rules covered secrets but not functional hardcode | Hardcode scanner and checklist reduce repeated manual review and future rework |
| 2026-06-29 | Execution Reliability Guardrails | Review | 14 | 3 | rg/git diff | Repeated frontend attempts lacked hard loop breaker and runtime proof | Attempt Ledger and Boundary Map reduce repeated commands, wrong-port validation and collateral regressions |
| 2026-06-29 | Context Hygiene Protocol | Review | 12 | 1 | diff/status | Context pollution lacked explicit operational handling | Compacted Snapshot prevents stale outputs from guiding later phases |
| 2026-06-28 | Execution Intelligence setup | Review | 8 | 3 | diff/status | Inventory drift found; no script yet | No code scan beyond framework docs |
| 2026-06-30 | Surface Routing & Execution Banner | Standard | 8 | 1 | rg/git diff | Model routing still used Cursor-only language in some paths | Surface split prevents wrong model guidance between Cursor and Codex |
| 2026-06-30 | Token Savings Report | Standard | 7 | 1 | rg/git diff | Token metrics were qualitative and had no report workflow | Adds report generation with confidence level and avoids fake exact token counts |
| 2026-06-30 | Execution Metrics | Standard | 6 | 1 | rg/git diff | Token savings reports lacked structured percentage/retry/error fields | Adds baseline vs actual units for estimated savings reports |

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
