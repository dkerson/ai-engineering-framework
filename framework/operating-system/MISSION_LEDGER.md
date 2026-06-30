# Mission Ledger

> Lightweight execution log for real missions. Use this to learn from usage without increasing runtime cost.

## Policy

- Register only short metadata, never full prompts, code blocks, secrets or private user data.
- One mission should cost at most 3-8 bullets of ledger work.
- Prefer approximate counts over expensive measurement.
- Do not update framework behavior from this file automatically.
- Promote improvements only through FOS recommendation and user approval.

## Fields

| Field | Description |
|-------|-------------|
| Date | Mission date. |
| Project | Consumer project or framework-only. |
| Mission | Short mission name. |
| Type | Demand or mission type. |
| Mode | Fast, Standard, Review or Technical Council. |
| Domains | Main domains involved. |
| Skills | Skills actually invoked. |
| Files Read | Approximate count and key files. |
| Files Changed | Approximate count and key files. |
| Validation | Commands or checks executed. |
| Token Notes | Any obvious waste or savings. |
| Outcome | Done, partial, blocked or recommendation-only. |

## Entries

| Date | Project | Mission | Type | Mode | Domains | Skills | Files Read | Files Changed | Validation | Token Notes | Outcome |
|------|---------|---------|------|------|---------|--------|------------|---------------|------------|-------------|---------|
| 2026-06-29 | framework/umbra | MCP Portability & Local Secrets | mcp-mission | Review | Infrastructure, Plugins, Security | orchestrator, plugin-resolver | MCP configs/plugins/registry | mcp templates, rules/mcp-portability, docs/MCP_PORTABILITY, FOS | rg/git diff | Removed machine-specific paths and kept secrets as env/OAuth placeholders | Done |
| 2026-06-29 | framework | Configuration & Hardcode Governance | framework-operating-system | Review | FOS, Orchestrator, Development, QA | orchestrator, hardcode-scanner, code-review | no-hardcode analysis and framework docs | rules/no-hardcode, hardcode-scanner, hardcode-audit, checklists, docs, orchestrator, FOS | rg/git diff | Added scanable anti-hardcode governance for configurable values | Done |
| 2026-06-29 | framework | Execution Reliability Guardrails | framework-operating-system | Review | FOS, Orchestrator, QA, Frontend | orchestrator, bug-hunter, qa | runtime/loop/regression analysis | rules/execution-loop-control, frontend-runtime-validation, regression-boundary, frontend-regression, working-context | rg/git diff | Added guardrails to stop repeated failed attempts, validate frontend runtime and protect canary routes | Done |
| 2026-06-29 | framework | Security Intelligence Domain | framework-operating-system | Review | Security, FOS, COS, Orchestrator | orchestrator, skill-creator | security/rules/workflows/FOS docs | security intelligence docs, skills, rules, checklists, workflows, FOS | diff/status | Reused existing security-review and split only high-risk responsibilities | Done |
| 2026-06-29 | framework | Context Hygiene Protocol | framework-operating-system | Review | FOS, Orchestrator, Token Economy | orchestrator | context/rules/orchestrator/FOS docs | rules/context-hygiene, working-context, orchestrator, token rules, FOS docs | diff/status | Added compacted snapshot to avoid polluted context in long missions | Done |
| 2026-06-28 | rifsmart/framework | Execution Intelligence setup | framework-operating-system | Review | FOS, Orchestrator, Token Economy | orchestrator, framework-reviewer, framework-optimizer | FOS docs, token rules, orchestrator | FOS docs/rules/templates | diff/status | Implemented as lightweight docs, no runtime script | Done |
| 2026-06-30 | framework | Surface Routing & Execution Banner | framework-operating-system | Standard | FOS, Orchestrator, Token Economy | orchestrator | model/surface rules, process, context, templates | rules/surface-routing, rules/execution-banner, model-routing, orchestrator, workflow, context | rg/git diff | Split Cursor/Codex guidance and added execution banner before tasks | Done |
| 2026-06-30 | framework | Token Savings Report | token-savings-report | Standard | FOS, Token Economy | orchestrator | TOKEN_METRICS, MISSION_LEDGER, SKILL_USAGE, workflow index | rules/token-savings-report, workflow, template, report, ledgers | rg/git diff | Report uses estimated savings when real token telemetry is unavailable | Done |
| 2026-06-30 | framework | Execution Metrics | framework-operating-system | Standard | FOS, Token Economy | orchestrator | token report rules, context, templates, ledgers | rules/execution-metrics, EXECUTION_METRICS, report/template updates | rg/git diff | Added baseline/actual units, estimated savings %, retries avoided and errors avoided | Done |
