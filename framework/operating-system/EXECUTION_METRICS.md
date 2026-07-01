# Execution Metrics

> Per-execution lightweight metrics for future token savings reports.

## Method

- Real token savings require trustworthy token telemetry from the active surface.
- When real telemetry is unavailable, use operational units from `rules/execution-metrics.md`.
- Percentages in this file are estimated efficiency percentages, not measured token counts.
- Keep entries short; never store prompts, secrets, long code excerpts or private data.

## Entries

| Date | Mission | Surface | Mode | Recommended Model | Baseline Route | Actual Route | Baseline Units | Actual Units | Estimated Savings % | Retries Avoided | Errors Avoided | Confidence | Evidence |
|------|---------|---------|------|-------------------|----------------|--------------|----------------|--------------|---------------------|-----------------|----------------|------------|----------|
| 2026-07-01 | Execution Learning Loop + RAG Consumer Hardening | Codex | Review | GPT-5.5 | Keep fixes as chat summary and repeat RAG duplicate/citation debugging in future missions | Added learning loop, canonical document identity, golden questions and Stable Candidate status | 42 | 28 | 33 | 2 | 3 | Media | Umbra evidence became reusable framework rules and checklists |
| 2026-06-30 | Token Savings Report baseline | Codex | Fast | gpt-5.4-mini | Manual qualitative report without structured per-execution metrics | Added report workflow from existing ledgers | 24 | 14 | 42 | 0 | 1 | Media | Report uses ledgers and declares no real token telemetry |
| 2026-06-30 | Execution Metrics | Codex | Standard | gpt-5.5 | Future reports rely on qualitative ledgers only | Added structured operational units and report fields | 32 | 20 | 38 | 0 | 2 | Media | Baseline/actual units, retries avoided and errors avoided now recorded |
| 2026-06-30 | Pre-Execution Gate | Codex | Standard | gpt-5.4-mini | Approval requirement scattered across banner/model rules | Added blocking gate rule and wired it into bootstrap, orchestrator, process and templates | 36 | 24 | 33 | 1 | 2 | Media | Dedicated gate prevents initial do-it request from counting as plan approval |
| 2026-06-30 | Codex Model UI Names | Codex | Standard | GPT-5.4-Mini + Raciocinio Media | Codex recommendations use API-style names and omit reasoning selector | Aligned routing docs with Codex UI model names and separate reasoning levels | 18 | 12 | 33 | 0 | 1 | Media | Prevents recommending unavailable-looking model labels in the Codex UI |
| 2026-07-01 | Update local framework from dkerson | Codex | Standard | GPT-5.4-Mini + Raciocinio Media | Direct pull over dirty worktree with conflict risk | Fetched origin, stashed local edits, fast-forwarded, resolved two doc conflicts and validated status | 30 | 22 | 27 | 1 | 2 | Media | Preserved local edits while updating main to origin/main a9d160a |
| 2026-07-01 | Execution Memory & Evaluation Baseline | Codex | Review | GPT-5.5 + Raciocinio Alta | Passive ledgers plus manual review on demand | Added retrieval-first memory, evidence anchoring, post-mission evaluation and 10-mission promotion cadence | 46 | 31 | 33 | 1 | 3 | Media | Prevents repeated failed hypotheses, unsupported conclusions and stale ledger learning |
| 2026-07-01 | Legacy generator cleanup | Codex | Standard | GPT-5.5 + Raciocinio Alta | Keep stale batch generator and rely on humans not to run it | Removed generator, updated reference and template headers, validated no broken generator refs | 20 | 13 | 35 | 0 | 2 | Media | Avoids accidental stale mass regeneration and removes dead tool surface |
| 2026-07-01 | Execution Target Map Gate | Codex | Standard | GPT-5.5 + Raciocinio Alta | Plan asks approval without explicit repo/system/database/environment targets | Added target map to gate, banner, model plan, working context, AGENTS and final response | 24 | 15 | 38 | 0 | 2 | Media | Prevents approving work without knowing where changes will happen |
| 2026-07-01 | Team Telemetry Collector | Codex | Standard | GPT-5.5 + Raciocinio Alta | Manual spreadsheet/report consolidation per developer and project | Added local collector plus optional anonymized external telemetry aggregation | 34 | 22 | 35 | 0 | 2 | Media | Generates local/project/team reports from existing ledgers and avoids manual counting |
