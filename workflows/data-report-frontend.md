# Workflow: Relatório frontend (Umbra / Irisys)

## Trigger

Criar ou alterar relatório web com dados de banco

## Pipeline

```
Orchestrator → hybrid-flow-planner → task-analyst* → business-data-analyst
  → semantic-layer-specialist → report-implementation-planner
  → sql-architect → backend → api → react → report-ux-reviewer
  → qa → data-validator → code-review* → Entrega
```

\* Condicional

## Modo

Standard → Review se financeiro ou produção

## Exemplo

`examples/data/create-frontend-report.md`
