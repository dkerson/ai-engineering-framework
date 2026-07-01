# Framework Backlog

> Improvements identified by the framework. Do not implement automatically.

| Title | Description | Source | Impact | Effort | Priority | Status |
|-------|-------------|--------|--------|--------|----------|--------|
| MCP Connector Validation | User validates local MCP before plugin active promotion. | MCP Governance | High | Low | P0 | Proposed |
| RAG Golden Question Evaluator | Create a repeatable evaluator for domain golden questions and expected canonical documents. | RAG + Evaluation Intelligence | High | Medium | P0 | Proposed |
| RAG Duplicate Cluster Report | Provide a standard report/checklist for duplicate document clusters by canonical title/hash. | RAG Governance | High | Medium | P0 | Proposed |
| RAG pgvector Path | postgres-plugin + vector extension for RAG indexing. | RAG + MCP | High | Medium | P1 | Proposed |
| OCR Capability | Extract text from images and scanned PDFs. | Capability Architecture | Medium | Medium | P2 | RAG Ready | Proposed |
| Plugin MCP Connectors | Implement real MCP integration for draft plugins incrementally. | Plugin Architecture | High | High | P1 | Plugin registry v2.8 | Proposed |
| Skill Usage Ledger | Track when each skill is invoked by mission type. | FOS | High | Medium | P1 | Implemented baseline |
| Pattern Promotion Criteria | Define thresholds for turning repeated flows into patterns. | FOS | Medium | Low | P1 | Implemented baseline |
| Token Waste Review | Add retrospective field for unnecessary context loading. | FOS | Medium | Low | P2 | Implemented baseline |
| Automated Usage Metrics Script | Optional script to compute skill/workflow inventory and drift from files/logs. | FOS | Medium | Medium | P2 | Proposed |
| Skill Boundary Audit | Review overlapping design/growth/reviewer skills after usage data exists. | FOS | Medium | Low | P2 | Proposed |
| Execution Memory Retrieval | Consult prior execution learning before non-trivial plans to avoid repeated errors and unnecessary reads. | Execution Intelligence | High | Low | P0 | Implemented baseline |
| Evidence Anchoring | Require observed/inferred/hypothesis separation before conclusions and final responses. | Execution Intelligence | High | Low | P0 | Implemented baseline |
| Post-Mission Evaluation | Add lightweight end-of-mission review to update memory only when learning is reusable. | Execution Intelligence | High | Low | P0 | Implemented baseline |
| Active Promotion Review | Review promotion candidates every 10 real missions or earlier on critical signals. | FOS | High | Low | P0 | Implemented baseline |
| Team Telemetry Collector | Generate local/project/team usage reports from sanitized ledgers and optional external telemetry repo. | FOS / Team Operations | High | Low | P0 | Implemented baseline |
