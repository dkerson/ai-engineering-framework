# Framework Roadmap

| Title | Description | Category | Impact | Effort | Priority | Dependencies | Status | Target Version |
|-------|-------------|----------|--------|--------|----------|--------------|--------|----------------|
| Framework Operating System | Add governance, living docs, metrics, health, backlog and recommendations. | Governance | High | Medium | P0 | v2.4 SIL | Implemented | 2.5.0 |
| Infrastructure Intelligence | Add project and infrastructure registries with safe secret policy. | Infrastructure | High | Medium | P0 | FOS | Implemented | 2.6.0 |
| MCP Governance | MCP Readiness, connectors, project profiles, discovery skill. | Infrastructure | High | Medium | P0 | Plugin Architecture | Implemented | 2.11.0 |
| Capability Operating System | Unified governance for all capabilities. | Architecture | High | Medium | P0 | RAG Ready | Implemented | 2.10.0 |
| RAG Intelligence | Full RAG capability: retrieval, citations, confidence, guardrails. | Capability | High | High | P0 | Capability Architecture | Implemented (Ready) | 2.9.0 |
| Plugin Architecture | Extract integrations as independent plugin packs with registry and lifecycle. | Extensibility | High | Medium | P0 | Infrastructure Intelligence | Implemented | 2.8.0 |
| Execution Intelligence Baseline | Mission ledger, skill usage, token metrics, promotion criteria and token budget policy. | Metrics | High | Low | P0 | FOS adoption | Implemented | 2.12.1 |
| Context Hygiene Protocol | Detect polluted execution context and continue from a compacted operational snapshot. | Metrics | High | Low | P0 | Execution Intelligence baseline | Implemented | 2.13.0 |
| Security Intelligence Domain | Add SI specialists for secure architecture, authorization, permission cache, threat modeling and governance. | Security | High | Medium | P0 | FOS, COS | Implemented | 2.14.0 |
| Execution Reliability Guardrails | Prevent repeated failed attempts, frontend runtime false positives and collateral regressions. | Quality | High | Low | P0 | Context Hygiene, Execution Intelligence | Implemented | 2.15.0 |
| Usage Metrics Automation | Add approved scripts to compute mission and skill usage from logs. | Metrics | Medium | Medium | P1 | Execution Intelligence baseline | Backlog | TBD |
| Pattern Library | Promote repeated mission outcomes into reusable patterns. | Knowledge | Medium | Medium | P1 | Real mission history | Backlog | TBD |
| Redundancy Review | Identify overlapping skills/workflows after usage data exists. | Quality | Medium | Low | P2 | Usage metrics | Backlog | TBD |
