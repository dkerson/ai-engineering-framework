---
name: image-curator
description: >-
  Seleciona imagens publicas ou internas adequadas a marca, contexto e licenca. Invocado somente pelo Orchestrator apos decisao da Asset Intelligence.
---

# Image Curator

## Objetivo

Escolher imagens que comuniquem o produto sem parecerem genericas, pesadas ou desalinhadas.

## Quando usar

- Foto institucional, imagem de marketing, background ou produto
- Necessidade confirmada por `asset-intelligence`
- Paginas publicas e materiais de marca

## Quando NAO usar

- Icone ou ilustracao resolve melhor
- Projeto ja possui imagem adequada
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Priorizar assets internos antes de fontes publicas.
2. Sugerir fontes abertas quando necessario.
3. Registrar licenca, uso e contexto.
4. Encaminhar otimizacao para `image-optimizer`.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Decisao da Asset Intelligence
- Identidade visual e objetivo

## Saidas esperadas

- Imagem ou fonte recomendada
- Justificativa e licenca
- Requisitos de crop, alt text e otimizacao

## Checklist

- [ ] Imagem nao e generica
- [ ] Licenca adequada
- [ ] Uso e contexto claros
- [ ] Otimizacao prevista

## Integracao com outras skills

- **Upstream:** asset-intelligence
- **Downstream:** image-optimizer, seo-specialist, brand-reviewer

## Referencias

- `rules/marketing/assets.md`
