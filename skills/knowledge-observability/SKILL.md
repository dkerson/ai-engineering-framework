---
name: knowledge-observability
description: >-
  Métricas RAG: documentos, chunks, latência, confidence, citações e uso. Invocado pelo rag-orchestrator.
---

# Knowledge Observability

## Objetivo

Observabilidade da base e do pipeline RAG.

## Métricas

| Métrica | Descrição |
|---------|-----------|
| doc_count | Documentos indexados |
| chunk_count | Chunks totais |
| index_latency | Tempo de indexação |
| search_latency | Tempo de busca |
| avg_confidence | Confidence médio |
| citation_rate | Respostas com citação |
| refusal_rate | Taxa de recusa (guard) |
| usage | Consultas por período |

## Referências

- `framework/operating-system/health/CAPABILITY_HEALTH.md`
