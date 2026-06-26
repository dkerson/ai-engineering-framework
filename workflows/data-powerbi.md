# Workflow: Power BI lento

## Trigger

Dashboard lento, dataset pesado, medida DAX

## Pipeline

```
Orchestrator → data-orchestrator → powerbi-specialist → dax-specialist → query-optimizer → data-validator → Entrega
```

## Modo

Standard / Review

## Exemplo

`examples/data/create-powerbi-report.md`
