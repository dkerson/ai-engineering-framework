# Framework Decisions

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
