# Token Budget Policy

> Execution budget rules for Codex/Cursor cost control.

## Default Route

Use the cheapest safe route:

```text
Fast Path -> Standard -> Review -> Technical Council
```

Escalate only when new risk or missing context justifies it.

## Fast Path

Use Fast Path before full NLME/SIL when the request is:

- A confirmation, status check or explanation.
- A simple shell command.
- A narrow documentation edit.
- A typo, label or one-file change.
- A direct Git/status question.
- A framework governance question that only needs living docs.

Fast Path may still read the project `AGENTS.md`, framework bootstrap and the directly relevant rule/doc.

## Full Mission Path

Use the full NLME/SIL/COS path when the request is:

- Ambiguous or strategic.
- Multi-domain.
- Product/design/growth/data heavy.
- Risky: auth, security, database, payments, production or architecture.
- A broad modernization, audit, roadmap or transformation.

## Hard Guards

- Do not read the whole project for orientation.
- Do not invoke a specialist just because it exists.
- Do not run full validation unless mode/risk requires it.
- Do not include raw specialist debate in user responses.
- Do not persist private content, secrets or long code excerpts in FOS ledgers.

## Required End-of-Mission Check

Before final response, answer internally:

1. Was the chosen mode the cheapest safe mode?
2. Were any files read twice unnecessarily?
3. Were any skills unnecessary?
4. Was validation scoped to risk?
5. Is there a reusable learning worth logging?
