---
name: knowledge-architect
description: >-
  Estrutura base de conhecimento: tipos, categorias, metadados, tags, permissões e versionamento. Distinto de knowledge-engine (Knowledge Hub). Invocado pelo rag-orchestrator.
---

# Knowledge Architect

## Objetivo

Modelar a base de conhecimento indexável para RAG.

## Responsabilidades

- Tipos: FAQ, artigo, manual, PDF, doc interno
- Categorias, tags, metadados obrigatórios
- Matriz de permissões (perfil, org, tenant)
- Política de versionamento e rollback

## Distinção

| Skill | Escopo |
|-------|--------|
| **knowledge-engine** | Consulta `knowledge/` do framework (boas práticas) |
| **knowledge-architect** | Estrutura KB do **projeto consumidor** (futuro) |

## Referências

- `templates/rag/knowledge-metadata.md`
- `rules/rag/knowledge-governance.md`
