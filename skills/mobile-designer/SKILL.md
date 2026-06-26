---
name: mobile-designer
description: >-
  Adapta layout e padrões para mobile (touch, densidade, navegação). Invocado pelo Orchestrator em interfaces mobile. Complementa mobile-ux.
---

# Mobile Designer

## Objetivo

Garantir qualidade visual e layout mobile — touch targets, stack, navegação.

## Quando usar

- Telas mobile ou responsive crítico
- App Flutter/RN
- HYBRID melhoria mobile

## Quando NÃO usar

- Só desktop admin
- Fluxos/gestos → skill legada `mobile-ux`
- **Nunca** auto-iniciar

## Responsabilidades

1. Breakpoints e layout stack
2. Touch ≥ 44px, thumb zone
3. Navegação mobile (bottom nav, drawer)
4. Aplicar `design-system/grid.md` mobile
5. LEGACY: preservar padrão mobile existente

## Checklist

- [ ] Layout mobile definido
- [ ] Touch targets ok
- [ ] WC atualizado

## Integração

- **Upstream:** ui-designer
- **Downstream:** flutter, mobile-ux*, design-reviewer

## Referências

- `skills/mobile-ux/SKILL.md`
- `design-system/grid.md`
