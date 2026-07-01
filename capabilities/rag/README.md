# RAG Intelligence

> Capability **Stable Candidate** v1.1.0 - validated by the Umbra KB/RAG consumer project, with additional canonical identity, curation and golden-question guardrails.


## Objetivo

Permitir que **qualquer projeto** implemente assistentes inteligentes baseados em conhecimento próprio: documentação, FAQs, manuais, artigos, bases internas.

## Componentes

| Componente | Skill responsável |
|------------|-------------------|
| Knowledge Retrieval | retrieval-specialist |
| Semantic Search | semantic-search-specialist |
| Embedding Management | embedding-specialist |
| Chunk Management | chunking-specialist |
| Document Indexing | knowledge-indexing-specialist |
| Document Loader | document-ingestion-specialist, document-parser |
| Permission Aware Retrieval | permission-aware-retrieval |
| Citation Engine | citation-engine |
| Confidence Engine | confidence-reviewer |
| Hallucination Guard | hallucination-guard |
| Conversation Memory | conversation-memory-specialist |
| Knowledge Versioning | knowledge-architect, knowledge-curator |
| Knowledge Refresh | knowledge-indexing-specialist |
| Knowledge Metrics | knowledge-observability |
| Knowledge Audit | knowledge-quality-reviewer, rag-evaluator |

## Arquitetura

Ver `ARCHITECTURE.md`.

## Fluxos

Ver `FLOWS.md` e `workflows/rag/`.

## Sub-orquestrador

`rag-orchestrator` coordena o pipeline RAG sem substituir o Master Orchestrator.

## Guardrails obrigatórios

1. **Hallucination Guard** — sem contexto recuperado: *"Não encontrei informação suficiente."*
2. **Citation Engine** — toda resposta cita fonte, documento, trecho e score.
3. **Confidence Engine** — abaixo do limite: não responder; pedir contexto ou informar baixa confiança.
4. **Permission Aware Retrieval** — nunca recuperar documento sem autorização.

## Referências

- `docs/RAG_INTELLIGENCE.md`
- `capabilities/CAPABILITY_REGISTRY.md`
- `rules/rag/`

## Consumer Evidence Guardrails

5. **Canonical Document Identity** - never confuse chunks, records and user-facing documents.
6. **Golden Questions** - validate representative questions before production.
7. **Curation Loop** - route unanswered, low-confidence and wrong-citation questions to review.

## Additional References

- `rules/rag/canonical-document-identity.md`
- `checklists/rag/golden-questions.md`
