# FOS Changelog

## 2.17.0 - 2026-06-29

- Added MCP Portability & Local Secrets.
- Updated ClickUp and GitHub examples to prefer remote OAuth MCP endpoints.
- Updated MSSQL examples to use `npx -y @mcp-collection/mssql-mcp` instead of user-specific paths.
- Split MSSQL principal and fiscal environment variables.

## 2.16.0 - 2026-06-29

- Added Configuration & Hardcode Governance.
- Added no-hardcode rule, checklist, hardcode-scanner skill and hardcode-audit workflow.
- Added Working Context fields for scan findings, false positives, category and recommended configuration source.
- Integrated anti-hardcode checks into Orchestrator, backend, api, react, qa and code-review.

## 2.15.0 - 2026-06-29

- Added Execution Reliability guardrails.
- Added Attempt Ledger and loop breaker for repeated failed hypotheses.
- Added Frontend Runtime Validation for port, URL, cache, console, network and DOM/screenshot evidence.
- Added Regression Boundary and frontend canary checks to protect working screens.

## 2.14.0 - 2026-06-29

- Added Security Intelligence domain.
- Added specialists for secure architecture, authorization, permission cache, threat modeling and SI governance.
- Registered security-intelligence capability in COS.
- Expanded security rules, checklists and workflow routing.

## 2.13.0 - 2026-06-29

- Added Context Hygiene Protocol.
- Added Context Health and Compacted Snapshot to Working Context.
- Orchestrator now checks context pollution during phase transitions and before broad validation.
- Token metrics track context pollution as an avoidable waste signal.

## 2.12.1 - 2026-06-28

- Added Execution Intelligence ledgers: Mission Ledger, Skill Usage, Token Metrics and Promotion Criteria.
- Added Token Budget Policy and Fast Path before full NLME for simple low-risk requests.
- Reinforced no self-mutation: observe, measure and recommend only.

## 2.12.0 - 2026-06-26

- Natural Language Mission Engine (NLME): mission-translator, mission-builder, prompt-builder.
- Mission Memory integrada ao FOS via mission-builder.
- 9 docs NLME, workflow, templates, rules, checklist, examples.
- Mission Intelligence capability atualizada para v2.12.

## 2.11.0 - 2026-06-26

- MCP Readiness Audit; MCP_SERVER_CATALOG; connector files for 7 priority plugins.
- sentry-plugin active; sqlserver/github/docker under-review.
- Project MCP profiles; mcp-discovery-specialist; mcp-security rules.

## 2.10.0 - 2026-06-26

- Added Capability Operating System (COS): registry, roadmap, status, health, report.
- Added capability-builder, capability-evaluator, capability-discovery.
- Registered 14 Stable domain capabilities; capability-first policy; plugin requires capability parent.
- PROJECT_CAPABILITIES per project.

## 2.9.0 - 2026-06-26

- Added Capability Architecture and RAG Intelligence (Ready).
- Added 22 RAG/capability skills, rules, checklists, workflows, knowledge.
- Policy: new technologies become capabilities before project implementation.

## 2.8.0 - 2026-06-26

- Added Plugin Architecture: registry, policy, lifecycle, 11 draft plugins.
- Added plugin-manager, plugin-resolver, plugin-builder skills.
- Added PLUGIN_HEALTH.md and PROJECT_PLUGINS.md per project.
- Policy: plugins never store secrets; destructive actions require approval.

## 2.6.0 - 2026-06-26

- Added Infrastructure Intelligence and Project Registry.
- Added global Infrastructure Registry and initial project registries for irisys, umbra and rifsmart.
- Added infrastructure discovery, project scanner, project resolver and integration resolver skills.
- Added secret policy: no real credentials stored.

## 2.5.0 - 2026-06-26

- Created Framework Operating System.
- Added living documents for status, health, roadmap, backlog, decisions, learning, metrics and reports.
- Added governance policy: register and recommend; never implement automatically.
