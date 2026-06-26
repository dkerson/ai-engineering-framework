---
name: knowledge-engine
description: >-
  Seleciona entradas relevantes do Knowledge Hub para a demanda atual. Invocado somente pelo Orchestrator quando uma tarefa se beneficia de boas praticas internas.
---

# Knowledge Engine

## Objetivo

Conectar a demanda do usuario ao conhecimento resumido do framework antes de planejar ou implementar.

## Quando usar

- Landing pages, dashboards, apps, sites, auditorias e modernizacoes
- Demandas de stack ou dominio especifico
- Review/Council quando ha risco de decisao inconsistente

## Quando NAO usar

- Perguntas triviais ou alteracoes minimas
- Quando o Working Context ja contem a referencia necessaria
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Mapear demanda para areas em `knowledge/`.
2. Ler apenas documentos relevantes.
3. Resumir principios aplicaveis no Working Context.
4. Evitar colar documentacao extensa.

## Orquestracao hierarquica

- **Unico contato com usuario:** Orchestrator.
- **Invocacao:** somente via pipeline definido.
- **Working Context:** adicionar bullets curtos com referencias consultadas.
- **Economia:** consultar o menor conjunto de areas.

## Exemplos

- Landing page -> `knowledge/copywriting`, `knowledge/branding`, `knowledge/seo`, `knowledge/design`, `knowledge/ux`
- Dashboard -> `knowledge/dashboard`, `knowledge/analytics`, `knowledge/design-system`, `knowledge/ux`
- Flutter -> `knowledge/flutter`, `knowledge/mobile`, `knowledge/performance`, `knowledge/design-system`

## Referencias

- `docs/KNOWLEDGE_HUB.md`
- `docs/KNOWLEDGE_ENGINE.md`
