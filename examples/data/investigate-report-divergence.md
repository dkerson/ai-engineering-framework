# Exemplo — Divergência relatório Irisys

## Pedido

"O relatório do Irisys está divergente do banco."

## Pipeline

```
Orchestrator → context-builder → task-analyst* → business-rule-mapper → data-orchestrator
  → sql-architect → data-validator → backend* → bug-hunter → qa → cross-domain-decision-maker → Entrega
```

\* Se aplicável

## Investigação

1. Período e filtros da tela vs query de validação
2. Procedure/view por trás do relatório
3. Regra de exclusão de status
4. API transformando resultado?

## Template

`templates/data/data-divergence-analysis.md`
