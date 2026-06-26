# Framework Decisions

## ADR-0004: Capability Operating System

- Date: 2026-06-26
- Context: Capabilities v2.9 exist but lack unified governance layer.
- Decision: Add COS as nucleus; capability-first; plugins require capability parent; PROJECT_CAPABILITIES.
- Impact: All technology evolves as Capability before projects; SIL checks registry first.

## ADR-0003: Capability-First Technology

- Date: 2026-06-26
- Context: New technologies (RAG, OCR, voice) risk being implemented ad-hoc per project.
- Decision: All new technologies become Framework Capabilities first; projects consume via Orchestrator.
- Impact: RAG Intelligence Ready; zero product implementation in consumer repos.

## ADR-0002: Plugin Architecture

- Date: 2026-06-26
- Context: Framework core growing with each new integration (Git, DB, BI, cloud, MCP).
- Problem: Integrations in core increase coupling, token cost and maintenance burden.
- Alternatives:
  - Keep all integrations as core skills.
  - Extract integrations as independent plugin packs with registry and governance.
- Decision: Adopt Plugin Architecture with Plugin Manager, Resolver and Builder.
- Justification: Core stays clean; plugins are versioned, documented, secure and FOS-governed.
- Impact: New integrations go to `plugins/`; Orchestrator uses Plugin Resolver before external actions.

## ADR-0001: FOS Is Governance, Not Execution

- Date: 2026-06-26
- Context: Framework needs to understand and manage its own evolution.
- Problem: Automatic self-modification would create risk and reduce user control.
- Alternatives:
  - Allow automatic framework edits.
  - Restrict FOS to recording, measuring and recommending.
- Decision: FOS never modifies the framework automatically.
- Justification: Keeps user as final decision maker and preserves compatibility.
- Impact: FOS creates records, recommendations and reports; Orchestrator implements only after user approval.
