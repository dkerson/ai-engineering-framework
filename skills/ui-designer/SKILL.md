---
name: ui-designer
description: >-
  Define layout, composição visual, componentes e densidade respeitando Design DNA. Invocado pelo Orchestrator após ux-designer.
---

# UI Designer

## Objetivo

Traduzir UX em layout e componentes — tokens visuais, densidade, hierarquia.

## Quando usar

- Após ux-designer no pipeline
- Ajustes visuais HYBRID
- GREENFIELD layout

## Quando NÃO usar

- LEGACY sem permissão visual
- Implementação → `react`/`flutter`
- **Nunca** auto-iniciar

## Responsabilidades

1. Estrutura de layout (grid, seções)
2. Mapear componentes existentes (`component-library`)
3. Aplicar tokens: DS projeto ou `design-system/`
4. Densidade e hierarquia tipográfica
5. LEGACY: zero mudança de componente/cor

## Checklist

- [ ] Layout em wireframe textual
- [ ] Componentes mapeados para reuso
- [ ] Tokens alinhados ao DNA
- [ ] WC atualizado

## Integração

- **Upstream:** ux-designer
- **Downstream:** design-system, visual-designer*

## Referências

- `design-system/`
- `rules/design/component-reuse.md`
