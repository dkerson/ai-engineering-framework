---
name: conversion-optimizer
description: >-
  Avalia e melhora CTAs, fluxo, prova social, confianca e reducao de friccao. Invocado somente pelo Orchestrator em paginas e fluxos orientados a conversao.
---

# Conversion Optimizer

## Objetivo

Aumentar a chance de acao do usuario sem sacrificar clareza ou confianca.

## Quando usar

- Landing pages, funis, formularios, onboarding e checkout
- Revisao de CTA, prova social, autoridade e friccao
- Product Audit com nota de conversao

## Quando NAO usar

- Pagina puramente informativa sem acao esperada
- Testes tecnicos ou analytics reais sem dados disponiveis
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Avaliar CTA, posicionamento, fluxo e friccao.
2. Checar credibilidade, autoridade e prova social.
3. Sugerir melhorias acionaveis.
4. Atualizar Working Context com hipoteses e prioridades.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- Estrutura, copy e objetivo de conversao
- Dados reais, se existirem

## Saidas esperadas

- Diagnostico de conversao
- Melhorias priorizadas
- Nota de Conversao quando aplicavel

## Checklist

- [ ] CTA primario claro
- [ ] Friccoes identificadas
- [ ] Prova social posicionada
- [ ] Recomendacoes priorizadas
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** landing-page-specialist, marketing-reviewer
- **Downstream:** qa, validator

## Referencias

- `rules/marketing/conversion.md`
- `checklists/marketing/conversion.md`
