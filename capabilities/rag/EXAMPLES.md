# RAG Intelligence — Examples

> Exemplos de **framework capability** — não implementam código em Umbra/Irisys/SmartRifa.

## Exemplo 1 — Consultar capabilities

**Pedido:** "Quais Capabilities nosso Framework possui?"

**Pipeline:** Orchestrator → capability-manager → CAPABILITY_REGISTRY.md

## Exemplo 2 — Arquitetura RAG para help center (futuro)

**Pedido:** "Como estruturar um assistente de FAQ para um portal?"

**Pipeline:** rag-orchestrator → rag-architect → knowledge-architect → chunking-specialist

**Saída:** Plano de KB, chunk strategy, fluxo Q&A — **sem código no projeto**.

## Exemplo 3 — Pipeline Q&A com guardrails

**Pedido:** "Defina o fluxo de pergunta e resposta com citações."

**Pipeline:** rag-architect → citation-engine → hallucination-guard → confidence-reviewer

## Exemplo 4 — Indexação de manual PDF

**Pedido:** "Como indexar manuais PDF na base de conhecimento?"

**Pipeline:** document-parser → chunking-specialist → embedding-specialist → knowledge-indexing-specialist

## Exemplo 5 — Resposta sem contexto

**Comportamento esperado:** hallucination-guard retorna *"Não encontrei informação suficiente na base de conhecimento para responder com confiança."*

## Referências

- `examples/rag-capability-mission.md`
