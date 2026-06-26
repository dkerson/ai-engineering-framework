# Workflow: Procedure / View / Indicador

## Trigger

Task pede alteração em indicador em procedure/view

## Pipeline

```
Orchestrator → task-analyst → requirement-reviewer → business-rule-mapper
  → data-orchestrator → sql-architect → dba-reviewer → impact-analysis
  → data-validator → backend* → qa → code-review → Entrega
```

## Modo

Review → Council se financeiro crítico ou produção

## Obrigatório

`rules/data/safe-database-changes.md`

## Exemplo

`examples/data/change-stored-procedure-from-task.md`
