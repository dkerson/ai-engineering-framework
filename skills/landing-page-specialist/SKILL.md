---
name: landing-page-specialist
description: >-
  Estrutura landing pages modernas orientadas a conversao. Invocado somente pelo Orchestrator em paginas publicas, campanhas, sites e funis.
---

# Landing Page Specialist

## Objetivo

Montar paginas publicas completas com hierarquia, narrativa e conversao.

## Quando usar

- Landing page, home publica, site ou pagina institucional
- Campanha de aquisicao ou validacao de produto
- Revisao de estrutura de pagina publica

## Quando NAO usar

- Tela interna operacional sem objetivo de marketing
- Implementacao frontend final (usar `react`/`flutter`)
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Estruturar hero, beneficios, funcionalidades, prova social, estatisticas, CTA, FAQ, contato e rodape.
2. Aplicar narrativa de conversao sem perder clareza.
3. Parametrizar secoes que dependem de dados reais.
4. Atualizar Working Context com estrutura da pagina.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- Estrategia de marca, conteudo e copy
- Objetivo de conversao

## Saidas esperadas

- Estrutura de landing page
- Requisitos para UI/frontend
- Pontos de prova social e CTAs

## Checklist

- [ ] Hero completo
- [ ] Beneficios e funcionalidades conectados
- [ ] Prova social prevista
- [ ] FAQ e contato incluidos
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** content-strategist, copywriter, social-proof-specialist
- **Downstream:** seo-specialist, asset-intelligence, react, conversion-optimizer

## Referencias

- `rules/marketing/landing-pages.md`
- `templates/marketing/landing-page.md`
