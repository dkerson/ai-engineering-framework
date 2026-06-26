---
name: hallucination-guard
description: >-
  Bloqueia respostas sem ancoragem em contexto recuperado. Mensagem padrão quando insuficiente. Invocado pelo rag-orchestrator em todo pipeline Q&A.
---

# Hallucination Guard

## Objetivo

**Nunca** permitir resposta baseada apenas no conhecimento do modelo.

## Regra

Se retrieval vazio ou irrelevante:

> Não encontrei informação suficiente na base de conhecimento para responder com confiança.

## Validações

- Chunks recuperados existem e correspondem à pergunta
- Citações presentes (citation-engine)
- Confidence acima do limite (confidence-reviewer)

## Referências

- `rules/rag/hallucination-rules.md`
- `checklists/rag/hallucination-prevention.md`
