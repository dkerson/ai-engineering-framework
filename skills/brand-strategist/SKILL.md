---
name: brand-strategist
description: >-
  Define posicionamento, tom de voz, personalidade e padroes de comunicacao de marca. Invocado somente pelo Orchestrator em demandas de branding, marketing, landing pages e produto.
---

# Brand Strategist

## Objetivo

Definir a base estrategica de marca para que copy, UX, UI e assets comuniquem a mesma identidade.

## Quando usar

- Nova landing page, site, portal ou produto publico
- Rebranding, reposicionamento ou tom de voz
- Projeto sem identidade visual/textual clara

## Quando NAO usar

- Ajuste isolado de texto sem impacto de marca
- Validacao visual final (usar `brand-reviewer`)
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Identificar publico, categoria, promessa e diferenciais.
2. Definir tom de voz, personalidade e principios de linguagem.
3. Mapear restricoes de identidade existentes no projeto.
4. Atualizar Working Context com decisoes de marca.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras (diagnostico, risco, recomendacao, validacao)
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- Briefing do produto, publico e objetivo
- Identidade visual/textual existente, se houver

## Saidas esperadas

- Posicionamento
- Tom de voz
- Personalidade da marca
- Regras de linguagem para copy e UX writing

## Checklist

- [ ] Publico e categoria claros
- [ ] Tom de voz aplicavel
- [ ] Diferenciais nao genericos
- [ ] Identidade existente respeitada
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** orchestrator, product-owner
- **Downstream:** content-strategist, copywriter, ux-writer, brand-reviewer

## Referencias

- `rules/marketing/branding.md`
- `docs/GROWTH_BRAND_INTELLIGENCE.md`
