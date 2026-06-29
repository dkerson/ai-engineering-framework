# Implemented

| Date | Version | Responsible | What | Motivation | Impact | Files |
|------|---------|-------------|------|------------|--------|-------|
| 2026-06-29 | 2.15.0 | Codex | Execution Reliability Guardrails | Stop long loops, frontend runtime false positives and collateral regressions | Attempt Ledger, Loop Control, Frontend Runtime Validation, Regression Boundary, canary checks | rules, context, orchestrator, bug-hunter, qa, workflows, checklists, docs, FOS |
| 2026-06-29 | 2.14.0 | Codex | Security Intelligence Domain | Separate SI, authorization, permission cache and threat modeling from generic security review | 5 skills, workflow, rules, checklists, COS registry | docs, skills, rules, checklists, workflows, FOS |
| 2026-06-29 | 2.13.0 | Codex | Context Hygiene Protocol | Reduce context pollution during long executions | Context Health, Compacted Snapshot, Orchestrator checkpoints | rules, context, orchestrator, workflows, FOS |
| 2026-06-28 | 2.12.1 | Codex | Execution Intelligence & Token Budget | Reduce Codex/Cursor cost while preserving governance | Fast Path, ledgers, token metrics, promotion criteria | FOS docs, rules, orchestrator, workflows |
| 2026-06-26 | 2.12.0 | Codex | Natural Language Mission Engine (NLME) | Linguagem natural → missões autônomas | 3 skills, 9 docs, workflow, templates | docs/, skills/, workflows/, rules/ |
| 2026-06-26 | 2.11.0 | Codex | MCP Readiness & Connectors | Safe MCP by plugin/project | 7 connector packs, profiles, sentry active | plugins/, projects/, FOS |
| 2026-06-26 | 2.10.0 | Codex | Capability Operating System (COS) | Govern all capabilities; capability-first | COS registry, builder/evaluator/discovery, PROJECT_CAPABILITIES | `.ai/capabilities/`, docs, FOS |
| 2026-06-26 | 2.9.0 | Codex | Capability Architecture & RAG Intelligence | Extensible capabilities; RAG ready for future projects | 22 skills, registry, 10 workflows, guardrails | `.ai/capabilities/rag/`, docs, FOS |
| 2026-06-26 | 2.8.0 | Codex | Plugin Architecture & Integration Packs | Extender framework sem inflar o nucleo | 11 plugins draft, 3 skills, registry, policy, PROJECT_PLUGINS | `.ai/plugins/`, docs, skills, workflows, FOS |
| 2026-06-26 | 2.5.0 | Codex | Framework Operating System | Govern framework evolution without automatic changes | Adds governance, health, roadmap, backlog, metrics and recommendations | `.ai/framework/operating-system/`, docs, rules, skills, workflows |
| 2026-06-26 | 2.6.0 | Codex | Infrastructure Intelligence & Project Registry | Register project infrastructure safely | Adds infrastructure registries, project registry, discovery skills and secret policy | `.ai/infrastructure/`, docs, rules, skills, workflows |
