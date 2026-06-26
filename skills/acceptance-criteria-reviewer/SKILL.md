---
name: acceptance-criteria-reviewer
description: >-
  Revisa e define critérios de aceite testáveis para entregas com componente de dados ou relatório. Complementa product-owner com foco em validação mensurável.
---

# Acceptance Criteria Reviewer

## Objetivo

Garantir critérios de aceite claros, testáveis e cobrindo dados, não só interface.

## Quando usar

- Relatório novo (web ou Power BI)
- Alteração de indicador com impacto em negócio
- Fechamento de fluxo híbrido antes de QA
- Task com critérios vagos

## Quando NÃO usar

- Escopo de produto inicial → `product-owner`
- Validação executada → `data-validator` / `qa`

## Responsabilidades

1. Escrever/revisar Given/When/Then incluindo dados esperados
2. Incluir totais de referência, períodos e filtros nos critérios
3. Cobrir casos limite (zero, null, período sem dados)
4. Alinhar com `data-validator` para casos de teste de dados

## Diferença de product-owner

`product-owner` define valor e escopo; esta skill foca em **critérios testáveis** para entrega, especialmente com dados.

## Integração

- **Upstream:** requirement-reviewer, business-data-analyst
- **Downstream:** qa, data-validator

## Referências

- `templates/test-plan.md`
- `checklists/data/report-validation.md`
