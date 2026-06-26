---
name: component-library
description: >-
  Inventaria componentes reutilizáveis do projeto e bloqueia duplicação desnecessária. Invocado pelo Orchestrator antes de implementar UI.
---

# Component Library

## Objetivo

Mapear e priorizar reuso de componentes existentes antes de criar novos.

## Quando usar

- Qualquer implementação de UI
- GREENFIELD em monorepo com `shared/ui`
- Review de duplicação

## Quando NÃO usar

- Só lógica backend
- **Nunca** auto-iniciar

## Responsabilidades

1. Buscar em `shared/`, `ui/`, lib do framework
2. Listar componentes reutilizáveis no WC
3. Justificar novos componentes (gap real)
4. Aplicar `rules/design/component-reuse.md`
5. LEGACY: somente componentes existentes

## Checklist

- [ ] Inventário no WC
- [ ] Novos componentes justificados
- [ ] Paths referenciados

## Integração

- **Upstream:** ui-designer, design-system
- **Downstream:** react, flutter

## Referências

- `design-system/components.md`
