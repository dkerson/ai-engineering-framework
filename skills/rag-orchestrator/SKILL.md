---
name: rag-orchestrator
description: >-
  Sub-orquestrador do domínio RAG Intelligence. Classifica subtipo, escolhe skills mínimas e aplica guardrails. Invocado somente pelo Orchestrator em missões RAG.
---

# RAG Orchestrator

## Objetivo

Coordenar pipeline RAG (ingestão, indexação, retrieval, Q&A) **sem substituir** o Master Orchestrator.

## Quando usar

- Assistente, FAQ, base de conhecimento, Q&A, indexação, reindex
- Capability Resolver selecionou `rag`

## Subtipos

| Subtipo | Pipeline resumido |
|---------|-------------------|
| Arquitetura | rag-architect → knowledge-architect |
| Indexação | document-parser → chunking → embedding → indexing |
| Q&A | permission-aware → retrieval → confidence → citation → guard |
| Audit/Eval | knowledge-quality → rag-evaluator → observability |

## Guardrails obrigatórios

- citation-engine em toda resposta
- hallucination-guard se sem contexto
- confidence-reviewer antes de responder
- prompt-injection-reviewer no input

## Orquestração hierárquica

- Não fala com usuário — Orchestrator consolida
- Economia: menor conjunto de skills por subtipo

## Referências

- `capabilities/rag/FLOWS.md`
- `docs/RAG_INTELLIGENCE.md`
