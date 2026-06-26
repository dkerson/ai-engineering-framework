---
name: citation-engine
description: >-
  Gera citações obrigatórias: fonte, documento, trecho e score. Invocado pelo rag-orchestrator em toda resposta RAG.
---

# Citation Engine

## Objetivo

Toda resposta RAG deve incluir citações rastreáveis.

## Formato

| Campo | Descrição |
|-------|-----------|
| source | ID ou URL da fonte |
| document | Título ou path lógico |
| excerpt | Trecho relevante do chunk |
| score | Relevância (0–1) |

## Template

Ver `templates/rag/citation-template.md`.

## Referências

- `rules/rag/citation-rules.md`
- `checklists/rag/citation-quality.md`
