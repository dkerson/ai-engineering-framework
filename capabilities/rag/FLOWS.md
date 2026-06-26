# RAG Intelligence — Flows

## Fluxos operacionais

| Fluxo | Workflow | Skills principais |
|-------|----------|---------------------|
| Document Index | `workflows/rag/document-index.md` | document-parser → chunking → embedding → indexing |
| Document Update | `workflows/rag/document-update.md` | knowledge-curator → reindex parcial |
| Reindex | `workflows/rag/reindex.md` | embedding → indexing → observability |
| Question Answer | `workflows/rag/question-answer.md` | retrieval → confidence → citation → guard |
| Knowledge Search | `workflows/rag/knowledge-search.md` | semantic-search → permission-aware |
| Permission Check | `workflows/rag/permission-check.md` | permission-aware-retrieval |
| Citation Generation | `workflows/rag/citation-generation.md` | citation-engine |
| Confidence Validation | `workflows/rag/confidence-validation.md` | confidence-reviewer |
| Conversation History | `workflows/rag/conversation-history.md` | conversation-memory-specialist |
| Knowledge Refresh | `workflows/rag/knowledge-refresh.md` | knowledge-indexing → observability |

## Modos Orchestrator

| Cenário | Modo |
|---------|------|
| Consultar capability / arquitetura RAG | Fast |
| Desenhar KB para projeto (futuro) | Standard → Review |
| Pipeline Q&A com permissões | Review |
| Alteração em base indexada produção | Council |

## Referências

- `workflows/rag/`
- `skills/rag-orchestrator/SKILL.md`
