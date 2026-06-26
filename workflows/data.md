# Workflow: Dados (Data Intelligence)

> Analytics, SQL, BI, validação. Modo padrão: **Standard** → **Review** se produção/procedure.

## Trigger

`data` — SQL, Power BI, DAX, ETL, divergência, relatório com dados, validação

## Detecção de domínio

Orchestrator identifica domínio **Data Intelligence** → invoca `data-orchestrator` como sub-orquestrador.

## Pipeline base

```
data-orchestrator → [skills de dados] → data-validator → Entrega
```

## Sub-workflows

| Cenário | Arquivo |
|---------|---------|
| SQL simples | `workflows/data-sql.md` |
| Power BI lento | `workflows/data-powerbi.md` |
| Relatório frontend | `workflows/data-report-frontend.md` |
| Divergência | `workflows/data-divergence.md` |
| Procedure/view | `workflows/data-procedure.md` |
| Híbrido | `workflows/hybrid-flows.md` |

## Skills

`data-orchestrator`, `data-analyst`, `sql-architect`, `query-optimizer`, `powerbi-specialist`, `dax-specialist`, `data-validator`, ...

Legado: `data` (redireciona para especializadas)

## Rules

- `rules/hierarchical-orchestration.md`
- `rules/data/query-performance.md`
- `rules/data/safe-database-changes.md`

## Resposta

Demandas predominantemente de dados: `templates/data/final-response-data.md`
