---
name: finance
description: >-
  Aspectos financeiros: billing, custos cloud, invoicing.
---

# Finance

## Objetivo

Avaliar impacto financeiro de decisões técnicas.

## Quando usar

- Billing feature
- Cost optimization
- Pricing técnico

## Quando NÃO usar

- UI/UX pura
- Bug fix sem impacto financeiro

## Responsabilidades

1. Identificar fluxo monetário
2. Compliance (PCI, etc.) se pagamentos
3. Estimar custos infra
4. Documentar requisitos financeiros

## Entradas esperadas

- Commercial analysis
- Feature requirements

## Saídas esperadas

- Requisitos financeiros
- Estimativa de custos

## Checklist

- [ ] Fluxo monetário mapeado
- [ ] Compliance verificada
- [ ] Custos estimados

## Integração com outras skills

- **Upstream:** commercial, product-owner
- **Downstream:** functional-spec, security-review

## Exemplos

**Input:** Stripe integration
**Output:** PCI scope, webhook idempotency required.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `context/business.md`
