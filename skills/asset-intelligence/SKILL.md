---
name: asset-intelligence
description: >-
  Decide o tipo de recurso visual mais adequado antes de buscar, gerar ou reutilizar assets. Invocado somente pelo Orchestrator em demandas de imagem, icone, logo, ilustracao, mockup, screenshot ou branding.
---

# Asset Intelligence

## Objetivo

Escolher o menor asset visual necessario para comunicar bem sem criar dependencia desnecessaria.

## Quando usar

- Imagens, icones, logos, backgrounds, mockups, avatars, Lottie ou screenshots
- Landing pages, apps, dashboards e portais com necessidade visual
- Revisao de assets existentes

## Quando NAO usar

- Ajustes puramente textuais
- Busca automatica de imagens sem analise previa
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Verificar assets existentes e biblioteca interna.
2. Decidir entre logo, icone, SVG, ilustracao, imagem, mockup ou outro recurso.
3. Acionar curadoria especifica somente quando necessario.
4. Atualizar Working Context com decisao, fonte e restricoes de licenca.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- Identidade visual existente
- Objetivo do asset

## Saidas esperadas

- Tipo de asset recomendado
- Fonte ou biblioteca sugerida
- Riscos de licenca/peso/consistencia

## Checklist

- [ ] Assets existentes verificados
- [ ] Tipo de asset justificado
- [ ] Licenca considerada
- [ ] Otimizacao prevista
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** landing-page-specialist, brand-strategist, ux
- **Downstream:** logo-manager, icon-curator, image-curator, illustration-curator, image-optimizer, brand-reviewer

## Referencias

- `rules/marketing/assets.md`
- `checklists/marketing/assets.md`
