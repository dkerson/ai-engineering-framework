# Workflow: Product & Design

## Guardrails para tela existente

- Definir tela alvo e telas fora de escopo antes de editar.
- Preservar identidade visual e comportamento de telas vizinhas em LEGACY.
- Aplicar `rules/frontend-runtime-validation.md` para confirmar porta/URL, cache, console, network e evidencia visual/DOM.
- Aplicar `rules/regression-boundary.md` se tocar layout, router, provider, CSS global, componente base, hook compartilhado ou cliente API.
- Validar rotas canario quando componente compartilhado for alterado.

> Criação ou evolução significativa de interface. Modo: **Standard** → **Review** se escopo grande.

## Trigger

`product` · `ux` · `feature` com UI · `mobile` com tela · relatório web · dashboard

## Pré-requisito

Orchestrator define **Design Mode** e carrega **Design DNA**.

## Pipeline

```
Design Mode + Design DNA
  → product-designer
  → ux-researcher* 
  → ux-designer
  → ui-designer
  → design-system
  → benchmark-specialist*
  → component-library
  → react | flutter | mobile-designer*
  → design-reviewer
  → product-aesthetic-director
  → accessibility*
  → qa
  → validator*
```

\* Condicional — Orchestrator decide.

## LEGACY (atalho)

Bug/typo/a11y pontual:

```
Design Mode LEGACY → react → design-reviewer* → qa
```

Sem redesign. Checklist: `checklists/design/legacy.md`

## Escalonamento

- Nova área grande → Review
- Auth/pagamentos UI → Review + security-review
- Nota estética < 8 → loop revisão (ui-designer / design-reviewer)

## Skills

Ver `docs/DESIGN_INTELLIGENCE.md`

## Rules

- `rules/design/design-modes.md`
- `rules/design/visual-identity.md`
- `rules/design/component-reuse.md`
