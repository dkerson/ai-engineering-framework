# Product Design — Fluxo

## Objetivo

Garantir que interfaces tenham qualidade de **produto** — não apenas código funcional.

## Fluxo

```
Orchestrator
  → Design Mode + Design DNA
  → product-designer (objetivo, escopo, sucesso)
  → ux-researcher* (evidências)
  → ux-designer (fluxos, estados)
  → ui-designer (layout, componentes)
  → design-system (tokens)
  → benchmark-specialist (padrões qualidade)
  → react | flutter
  → design-reviewer
  → product-aesthetic-director (gate ≥8)
  → qa
```

## Artefatos

- `templates/design/design-dna.md`
- `templates/design/interface-spec.md`
- `templates/design/aesthetic-review.md`

## Relação com skills legadas

| Legada | Nova / complementar |
|--------|-------------------|
| ux | ux-designer (pipeline design); ux em fluxos simples |
| mobile-ux | mobile-designer + mobile-ux |
| product-owner | product-designer em interface |
| dashboard-designer | dashboards e BI |
| report-ux-reviewer | revisão; report-designer para spec |

## Dashboards e relatórios

- Dashboard/BI/KPI → `dashboard-designer`
- Relatório web/PDF/Excel → `report-designer` → `report-ux-reviewer`

Workflow: `workflows/product-design.md`
