# Exemplo — Task híbrida (banco + frontend)

## Pedido

Task ClickUp: "Adicionar coluna de custo por viagem no relatório operacional Irisys."

## Pipeline

```
Orchestrator → hybrid-flow-planner → task-analyst → requirement-reviewer
  → business-data-analyst → semantic-layer-specialist (viagem, financeiro)
  → data-orchestrator → sql-architect → backend → react
  → data-validator → qa → Entrega
```

## Critérios híbridos atendidos

- task + banco
- banco + frontend
- indicador + operação

## Economia

- Não ler projeto Irisys inteiro — começar pela tela do relatório e procedure citada na task
