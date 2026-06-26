# Exemplo — Otimizar SQL

## Pedido

"Otimize esta consulta."

## Classificação

- Tipo: `data` / `performance`
- Domínios: Data Intelligence
- Modo: Standard

## Pipeline

```
Orchestrator → data-orchestrator → sql-architect → query-optimizer → data-validator → Entrega
```

## Working Context (resumo)

- Consulta colada pelo usuário
- Tabela principal identificada
- Join N:N causando fan-out
- Índice sugerido em coluna de filtro

## Resposta

Usar `templates/data/final-response-data.md`
