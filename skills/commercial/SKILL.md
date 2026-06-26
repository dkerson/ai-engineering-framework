---
name: commercial
description: >-
  Aspectos comerciais: propostas, pricing, contratos, ROI.
---

# Commercial

## Objetivo

Alinhar soluções técnicas com viabilidade comercial.

## Quando usar

- Proposta comercial
- Pricing feature
- ROI de solução

## Quando NÃO usar

- Implementação técnica pura
- Bug fix

## Responsabilidades

1. Identificar valor entregue
2. Estimar esforço vs retorno
3. Riscos comerciais
4. Proposta estruturada

## Entradas esperadas

- Requisito de negócio
- `context/business.md`

## Saídas esperadas

- Análise comercial
- Recomendação go/no-go

## Checklist

- [ ] Valor quantificado
- [ ] Esforço estimado
- [ ] Riscos comerciais
- [ ] Recomendação clara

## Integração com outras skills

- **Upstream:** product-owner
- **Downstream:** functional-spec

## Exemplos

**Input:** Feature premium analytics
**Output:** ROI positivo em 6 meses, pricing tier Pro.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `context/business.md`
