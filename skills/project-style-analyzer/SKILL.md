---
name: project-style-analyzer
description: >-
  Analisa estilo, design system, UI library, tema, tipografia, paleta e padroes visuais de um projeto. Invocado somente pelo Orchestrator antes de criar ou modernizar telas, sites, dashboards e apps.
---

# Project Style Analyzer

## Objetivo

Identificar o modo visual do projeto para orientar UX, UI, branding, assets e frontend sem quebrar consistencia.

## Quando usar

- Criar landing page, home, site, dashboard, tela ou app
- Modernizar sistema existente
- Avaliar se ha Design System, UI library, tema ou identidade visual

## Quando NAO usar

- Backend, banco ou API sem impacto visual
- Ajuste textual isolado
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Detectar CSS framework, UI library, design system, componentes, tema e icones.
2. Identificar paleta, tipografia, espacamentos, padroes visuais e identidade.
3. Classificar modo: Legacy Mode, Hybrid Mode, Greenfield Mode ou Automatic Mode.
4. Atualizar Working Context com restricoes e oportunidades.

## Orquestracao hierarquica

- **Unico contato com usuario:** Orchestrator - esta skill nunca fala diretamente com o usuario.
- **Invocacao:** somente quando o Orchestrator incluir no pipeline.
- **Working Context:** registrar resumo; skills seguintes reutilizam sem reler tudo.
- **Economia:** seguir `rules/token-economy.md`.

## Saidas esperadas

- Inventario visual do projeto
- Modo recomendado
- Regras para design/frontend
- Lacunas de Design DNA, Brand DNA, Communication DNA, Marketing DNA, Visual DNA e Product DNA

## Referencias

- `docs/PRODUCT_EXCELLENCE.md`
- `docs/GROWTH_BRAND_INTELLIGENCE.md`
