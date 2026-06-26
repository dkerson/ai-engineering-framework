# Exemplo — Dashboard Power BI lento

## Pedido

"Esse dashboard está lento."

## Pipeline

```
Orchestrator → data-orchestrator → powerbi-specialist → dax-specialist → query-optimizer → data-validator → Entrega
```

## Pontos de atenção

- Medir se gargalo é DAX, modelo ou SQL DirectQuery
- Não refatorar modelo inteiro se uma medida é o problema
