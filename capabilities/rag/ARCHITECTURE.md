# RAG Intelligence — Architecture

## Visão em camadas

```text
Usuário / Aplicação (projeto consumidor — futuro)
              ↓
Master Orchestrator
              ↓
Capability Resolver → rag
              ↓
RAG Orchestrator
              ↓
┌─────────────────────────────────────────────────────────┐
│ Ingestão          │ Indexação         │ Retrieval       │
│ document-parser   │ chunking          │ semantic-search │
│ document-ingestion│ embedding         │ retrieval       │
│ knowledge-architect│ knowledge-indexing│ permission-aware│
└─────────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────────┐
│ Geração & Guardrails  │ Memória & Gov    │ Observability │
│ citation-engine       │ conversation-mem │ knowledge-obs │
│ hallucination-guard   │ knowledge-curator│ rag-evaluator │
│ confidence-reviewer   │ versioning       │               │
│ prompt-injection      │ knowledge-quality│               │
└─────────────────────────────────────────────────────────┘
```

## Decisões de arquitetura (rag-architect)

| Área | Responsabilidade do architect | Não implementa |
|------|------------------------------|----------------|
| Fluxo | Pipeline ingestão → index → retrieve → cite → respond | Código de produto |
| Banco | Vector store vs híbrido (SQL + vector) | Deploy |
| Embeddings | Modelo, dimensão, versionamento | Treinamento de modelo |
| Busca | Vetorial, híbrida, reranking | — |
| Permissões | Filtros por perfil/tenant | Auth do produto |
| Versionamento | Política de reindex e rollback | — |
| Escalabilidade | Sharding, cache, batch index | Infra real |

## Pipeline Q&A

```text
Pergunta
  → permission-aware-retrieval (filtros)
  → semantic-search-specialist + retrieval-specialist
  → confidence-reviewer (score)
  → SE score < limite → pedir contexto / recusar
  → citation-engine (montar citações)
  → hallucination-guard (validar ancoragem)
  → prompt-injection-reviewer (input)
  → Resposta + citações
```

## Pipeline indexação

```text
Documento
  → document-parser (MD, HTML, PDF, DOCX, TXT)
  → chunking-specialist
  → embedding-specialist
  → knowledge-indexing-specialist
  → knowledge-observability (métricas)
```

## Integração com Plugin Architecture

Vector DB e storage podem usar plugins futuros (postgres-plugin com pgvector, etc.). RAG define **o quê**; plugins definem **conexão**.

## Referências

- `capabilities/rag/FLOWS.md`
- `rules/rag/`
