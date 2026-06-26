---
name: logo-manager
description: >-
  Gerencia variantes de logo, favicon, app icons, PWA icons e social previews. Invocado somente pelo Orchestrator em demandas de identidade visual e assets de marca.
---

# Logo Manager

## Objetivo

Garantir um conjunto completo e consistente de assets de marca.

## Quando usar

- Logo principal, horizontal, vertical ou responsivo
- Favicon, app icon, PWA icon, Apple Touch Icon e Android Icon
- Open Graph e social preview

## Quando NAO usar

- Iconografia funcional da interface (usar `icon-curator`)
- Criacao de identidade estrategica (usar `brand-strategist`)
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Inventariar logos existentes e lacunas.
2. Sugerir estrutura completa quando nao houver identidade.
3. Definir formatos, tamanhos e usos.
4. Atualizar Working Context com mapa de assets de marca.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- Brand kit ou assets existentes
- Plataformas alvo

## Saidas esperadas

- Inventario de logos/icons
- Requisitos de exportacao
- Lacunas e recomendacoes

## Checklist

- [ ] Favicon definido
- [ ] App/PWA icons definidos quando aplicavel
- [ ] Open Graph/social preview previsto
- [ ] Variantes coerentes
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** asset-intelligence, brand-strategist
- **Downstream:** image-optimizer, seo-specialist, brand-reviewer

## Referencias

- `rules/marketing/assets.md`
- `checklists/marketing/branding.md`
