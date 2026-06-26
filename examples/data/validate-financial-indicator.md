# Exemplo — Validar indicador financeiro

## Pedido

"Validar se o indicador de faturamento do mês está correto."

## Pipeline

```
Orchestrator → data-orchestrator → business-rule-mapper → sql-architect
  → data-validator → data-quality-reviewer* → Entrega
```

## Regras

- `rules/data/financial-data-care.md` — dupla validação
- Fonte autorizada em `context/semantic-layer/indicadores.md`
