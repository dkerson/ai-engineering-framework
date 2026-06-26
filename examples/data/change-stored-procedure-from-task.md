# Exemplo — Alterar procedure por task

## Pedido

"A task pede alteração em indicador calculado em uma procedure."

## Pipeline

```
Orchestrator → task-analyst → requirement-reviewer → business-rule-mapper
  → data-orchestrator → sql-architect → dba-reviewer → impact-analysis
  → data-validator → backend* → qa → code-review → Entrega
```

## Obrigatório antes de produção

- `rules/data/safe-database-changes.md`
- `checklists/data/production-safety.md`
