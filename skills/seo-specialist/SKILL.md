---
name: seo-specialist
description: >-
  Define SEO tecnico e semantico para paginas publicas. Invocado somente pelo Orchestrator em sites, landing pages, conteudo publico e social preview.
---

# SEO Specialist

## Objetivo

Preparar paginas publicas para descoberta organica, compartilhamento e leitura semantica.

## Quando usar

- Landing pages, sites e paginas publicas
- Metadados, headings, alt text e Open Graph
- Auditoria SEO de conteudo ou assets

## Quando NAO usar

- Tela interna protegida sem indexacao
- Performance tecnica ampla (usar `performance`)
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Definir title, description, headings e estrutura semantica.
2. Orientar alt text, URLs, links e social previews.
3. Evitar keyword stuffing e duplicidade de H1.
4. Atualizar Working Context com requisitos SEO.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- Estrutura de pagina e copy
- Assets e rotas publicas

## Saidas esperadas

- Title, description e headings
- Requisitos Open Graph
- Recomendacoes SEO para imagens e links

## Checklist

- [ ] Title e description definidos
- [ ] H1 unico
- [ ] Hierarquia de headings coerente
- [ ] Open Graph previsto quando publico
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** landing-page-specialist, copywriter, image-optimizer
- **Downstream:** react, qa, marketing-reviewer

## Referencias

- `rules/marketing/seo.md`
- `checklists/marketing/seo.md`
