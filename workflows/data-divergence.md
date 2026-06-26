# Workflow: Divergência de dados

## Trigger

Relatório/tela/API divergente do banco

## Pipeline

```
Orchestrator → context-builder* → task-analyst* → business-rule-mapper
  → data-orchestrator → sql-architect → data-validator
  → backend* → bug-hunter → qa → cross-domain-decision-maker → Entrega
```

\* Condicional

## Modo

Standard / Review

## Exemplo

`examples/data/investigate-report-divergence.md`
