---
name: product-excellence
description: >-
  Define e avalia o padrao minimo de excelencia de produto: UX, UI, mobile, desktop, performance, conversao, clareza, produtividade, escalabilidade e consistencia. Invocado somente pelo Orchestrator em auditorias e entregas de produto.
---

# Product Excellence

## Objetivo

Garantir que produtos entregues pelo framework sejam completos, modernos, consistentes e prontos para producao.

## Quando usar

- Auditoria de produto
- Modernizacao ampla
- Entregas com interface, marketing, dados ou fluxo critico

## Quando NAO usar

- Tarefa pontual de baixo risco
- Ajuste tecnico sem impacto de produto
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Avaliar UX, UI, mobile, desktop, performance, conversao, clareza, produtividade, escalabilidade e consistencia.
2. Aplicar notas 0-10 quando for auditoria.
3. Sinalizar categorias abaixo de 8.
4. Encaminhar melhorias para `product-evolution-planner`.

## Orquestracao hierarquica

- **Unico contato com usuario:** Orchestrator.
- **Working Context:** consolidar notas e riscos.
- **Economia:** avaliar apenas categorias aplicaveis.

## Referencias

- `docs/PRODUCT_EXCELLENCE.md`
- `checklists/marketing/product-audit.md`
