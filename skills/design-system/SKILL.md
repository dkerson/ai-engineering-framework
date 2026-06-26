---
name: design-system
description: >-
  Aplica tokens e padrões do Design System (projeto ou framework) ao spec de interface. Invocado pelo Orchestrator após ui-designer.
---

# Design System

## Objetivo

Garantir consistência de tokens — cores, tipo, spacing, componentes padrão.

## Quando usar

- GREENFIELD ou HYBRID com tokens
- Novo módulo sem spec visual do cliente
- Alinhar interface ao DS documentado

## Quando NÃO usar

- LEGACY (preservar DS existente in-place)
- Projeto sem mudança visual
- **Nunca** auto-iniciar

## Responsabilidades

1. Carregar DS do projeto ou `design-dna-default.md`
2. Referenciar arquivos em `design-system/` aplicáveis
3. Listar tokens usados no WC (bullets)
4. Não inventar marca — princípios de qualidade apenas
5. Dark/light conforme projeto

## Checklist

- [ ] Tokens documentados no WC
- [ ] DS do projeto respeitado
- [ ] Sem cópia de produtos de referência

## Integração

- **Upstream:** ui-designer
- **Downstream:** benchmark-specialist, react

## Referências

- `design-system/README.md`
- `docs/DESIGN_SYSTEM.md`
