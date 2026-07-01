# Token Budget Policy

> Execution budget rules for Codex/Cursor cost control.

Complementos obrigatorios: `rules/pre-execution-gate.md`, `rules/surface-routing.md`, `rules/model-routing.md`, `rules/execution-banner.md`.

## Default Route

Use the cheapest safe route:

```text
Fast Path -> Standard -> Review -> Technical Council
```

Escalate only when new risk or missing context justifies it.

Default model recommendation for cost-sensitive usage:

```text
Cursor: Composer 2.5 Standard -> Auto -> stronger explicit model
Codex: GPT-5.3-Codex-Spark -> GPT-5.4-Mini -> GPT-5.4 -> GPT-5.5
Codex reasoning: Baixa -> Média -> Alta -> Altíssimo
```

The Orchestrator must detect the active surface, choose the cheapest safe model/reasoning
pair using `docs/CODEX_MODEL_SELECTION.md` and `rules/model-routing.md`, present the
execution banner, recommended model and approval question, then stop until explicit
approval before running an executable task.

## Fast Path

Use Fast Path before full NLME/SIL when the request is:

- A confirmation, status check or explanation.
- A simple shell command.
- A narrow documentation edit.
- A typo, label or one-file change.
- A direct Git/status question.
- A framework governance question that only needs living docs.

Fast Path may still read the project `AGENTS.md`, framework bootstrap and the directly relevant rule/doc.

Fast Path can answer without an approval gate only when it is pure question/answer and does not require broad file reading, shell commands, edits or validation.

## Full Mission Path

Use the full NLME/SIL/COS path when the request is:

- Ambiguous or strategic.
- Multi-domain.
- Product/design/growth/data heavy.
- Risky: auth, security, database, payments, production or architecture.
- A broad modernization, audit, roadmap or transformation.

Full Mission Path must include an explicit model recommendation. Prefer `Auto` on Cursor
when the task has high ambiguity, auth/security/database/production risk, multi-domain
scope or repeated failure risk.

For high-risk full missions in Codex, prefer `GPT-5.5` with `Alta` reasoning. Use
`Altíssimo` for Technical Council, production, security, database migrations, RAG
architecture, permission-aware retrieval or deploy decisions.

## Hard Guards

- Do not read the whole project for orientation.
- Do not invoke a specialist just because it exists.
- Do not run full validation unless mode/risk requires it.
- Do not include raw specialist debate in user responses.
- Do not persist private content, secrets or long code excerpts in FOS ledgers.
- Do not execute an approved task plan silently; ask the user to confirm the plan and recommended model first.
- Do not treat the user's initial "do it" request as approval for a plan that has not been shown yet.
- Do not continue after discovering a model escalation trigger; pause and ask the user to switch the model in the active surface.

## Required End-of-Mission Check

Before final response, answer internally:

1. Was the chosen mode the cheapest safe mode?
2. Were any files read twice unnecessarily?
3. Were any skills unnecessary?
4. Was validation scoped to risk?
5. Is there a reusable learning worth logging?
