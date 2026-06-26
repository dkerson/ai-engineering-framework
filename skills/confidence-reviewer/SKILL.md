---
name: confidence-reviewer
description: >-
  Atribui Confidence Score à resposta RAG. Abaixo do limite: não responder ou solicitar mais contexto. Invocado pelo rag-orchestrator.
---

# Confidence Reviewer

## Objetivo

Confidence Engine — gate de qualidade antes da resposta.

## Comportamento

| Score | Ação |
|-------|------|
| ≥ limite (default 0.7) | Prosseguir para citation + guard |
| < limite | Não responder; pedir contexto ou informar baixa confiança |

## Fatores

- Score médio dos chunks recuperados
- Cobertura da pergunta
- Consistência entre chunks

## Referências

- `rules/rag/confidence-rules.md`
- `templates/rag/confidence-threshold.md`
