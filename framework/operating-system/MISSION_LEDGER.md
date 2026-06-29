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
| 2026-06-29 | framework | Context Hygiene Protocol | framework-operating-system | Review | FOS, Orchestrator, Token Economy | orchestrator | context/rules/orchestrator/FOS docs | rules/context-hygiene, working-context, orchestrator, token rules, FOS docs | diff/status | Added compacted snapshot to avoid polluted context in long missions | Done |
| 2026-06-28 | rifsmart/framework | Execution Intelligence setup | framework-operating-system | Review | FOS, Orchestrator, Token Economy | orchestrator, framework-reviewer, framework-optimizer | FOS docs, token rules, orchestrator | FOS docs/rules/templates | diff/status | Implemented as lightweight docs, no runtime script | Done |
