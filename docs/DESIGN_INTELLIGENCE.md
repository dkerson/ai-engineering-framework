# Product & Design Intelligence — Guia do Domínio

> AI Engineering Framework v2.2+ — qualidade de produto, UX, UI e Design System.

## Visão

Domínio **Product & Design Intelligence** complementa Development e Data Intelligence. O **Orchestrator** detecta criação/alteração de interface e aplica o pipeline de design antes da implementação.

```
Orchestrator
    ↓ Identificar Design Mode (LEGACY | HYBRID | GREENFIELD)
    ↓ Analisar Design DNA
    ↓ product-designer → ux-designer → ui-designer → design-system
    ↓ benchmark-specialist
    ↓ react / flutter (implementação)
    ↓ design-reviewer → product-aesthetic-director
    ↓ qa → entrega
```

## Regra mais importante

**Nunca** alterar identidade visual de sistema existente sem solicitação explícita do usuário.

## Design Modes

| Modo | Quando | Doc |
|------|--------|-----|
| LEGACY | Legado, bug, manutenção | `docs/DESIGN_MODES.md` |
| HYBRID | Evolução gradual | idem |
| GREENFIELD | Novo módulo/produto | idem |

## Skills do domínio

| Skill | Papel |
|-------|-------|
| product-designer | Objetivo, escopo, fluxo de produto |
| ux-researcher | Necessidades, personas, jobs-to-be-done |
| ux-designer | Fluxos, wireframes, estados |
| ui-designer | Layout, componentes, tokens visuais |
| design-system | Tokens e padrões do DS |
| visual-designer | Composição, hierarquia, estética |
| mobile-designer | Layout mobile |
| desktop-designer | Layout desktop denso |
| interaction-designer | Microinterações, feedback |
| component-library | Inventário e reuso |
| benchmark-specialist | Padrões de qualidade (sem cópia) |
| design-reviewer | Checklist de interface |
| product-aesthetic-director | Scores 0–10; gate ≥ 8 |
| dashboard-designer | Dashboards, KPIs, BI |
| report-designer | Relatórios web/PDF/Excel/PBI |
| accessibility | WCAG, a11y |

### Preservadas (não substituídas)

`ux` · `mobile-ux` · `report-ux-reviewer` · `dashboard-designer` (evoluída)

## Design DNA

Todo projeto deve ter Design DNA em `context/design-dna.md` ou preenchido via `templates/design/design-dna.md`. Sem identidade → `design-system/design-dna-default.md`.

## Artefatos

| Tipo | Caminho |
|------|---------|
| Design System | `design-system/` |
| Rules | `rules/design/` |
| Checklists | `checklists/design/` |
| Templates | `templates/design/` |
| Exemplos | `examples/design/` |
| Workflow | `workflows/product-design.md` |

## Documentação

- `docs/DESIGN_GUIDE.md` — guia operacional
- `docs/DESIGN_SYSTEM.md` — tokens e componentes
- `docs/DESIGN_MODES.md` — LEGACY / HYBRID / GREENFIELD
- `docs/PRODUCT_DESIGN.md` — fluxo de produto

## Gate de qualidade

`product-aesthetic-director` — qualquer nota < 8 → revisão antes da entrega final.

## Economia de tokens

`rules/design/token-economy-design.md` — checklists e tokens, não prosa longa.
