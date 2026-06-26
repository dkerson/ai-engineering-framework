---
name: accessibility
description: >-
  Valida e especifica requisitos WCAG — contraste, teclado, ARIA, touch. Invocado pelo Orchestrator antes da entrega de interface.
---

# Accessibility

## Objetivo

Garantir interface acessível (mín. WCAG AA) conforme Design Mode.

## Quando usar

- Antes de entrega de UI
- LEGACY melhorias a11y permitidas
- Formulários e tabelas

## Quando NÃO usar

- Só API
- **Nunca** auto-iniciar

## Responsabilidades

1. Aplicar `checklists/design/accessibility.md`
2. Listar gaps e correções no WC
3. LEGACY: a11y sem mudar visual
4. Não gerar relatório longo

## Checklist

- [ ] Contraste AA
- [ ] Keyboard + focus
- [ ] Labels/ARIA
- [ ] WC atualizado

## Integração

- **Upstream:** ux-designer, react
- **Downstream:** design-reviewer, qa

## Referências

- `checklists/design/accessibility.md`
