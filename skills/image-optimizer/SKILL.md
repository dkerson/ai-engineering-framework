---
name: image-optimizer
description: >-
  Revisa peso, formato, compressao, responsividade, lazy loading e SEO de imagens. Invocado somente pelo Orchestrator quando assets visuais entram em produto ou pagina publica.
---

# Image Optimizer

## Objetivo

Garantir imagens leves, responsivas e semanticamente corretas.

## Quando usar

- Imagens em site, landing page, portal, app ou dashboard
- Conversao para WebP/AVIF
- Lazy loading, dimensoes, alt text e SEO

## Quando NAO usar

- Icones vetoriais simples que nao precisam otimizacao raster
- Analise de performance geral (usar `performance`)
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Definir formato ideal (SVG, WebP, AVIF, PNG/JPEG quando necessario).
2. Checar peso, compressao e dimensoes.
3. Orientar lazy/eager loading conforme posicao.
4. Atualizar Working Context com requisitos de otimizacao.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- Lista de assets e contexto de uso
- Stack frontend

## Saidas esperadas

- Recomendacoes de formato/peso
- Requisitos de responsividade e loading
- Alt text e SEO quando aplicavel

## Checklist

- [ ] Formato adequado
- [ ] Peso controlado
- [ ] Dimensoes responsivas
- [ ] Loading definido
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** image-curator, illustration-curator, logo-manager
- **Downstream:** seo-specialist, react, brand-reviewer

## Referencias

- `rules/marketing/assets.md`
- `rules/marketing/seo.md`
