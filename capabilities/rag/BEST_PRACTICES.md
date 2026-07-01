# RAG Intelligence — Best Practices

## Chunking

- Tamanho típico: 256–512 tokens; overlap 10–20%.
- Respeitar limites semânticos (seções, parágrafos, headings).
- FAQs: um par pergunta/resposta por chunk.

## Embeddings

- Versionar modelo; reindex ao trocar modelo.
- Documentar dimensão e provider em metadata.

## Retrieval

- Preferir busca híbrida (vetorial + BM25) quando disponível.
- Top-k inicial 5–10; rerank para top 3–5.
- Sempre filtrar por permissão antes do ranking.

## Respostas

- Citar fonte, documento, trecho e score.
- Confidence mínimo sugerido: 0.7 (configurável por projeto).
- Sem contexto relevante: recusar com mensagem padrão.

## Observabilidade

- Medir: latência index, latência search, confidence médio, taxa de recusa, citações por resposta.

## Referências

- `knowledge/rag/`
- `checklists/rag/`

## Consumer Project Lessons

Lessons from the Umbra KB/RAG consumer project:

- Separate chunk, database record, document and canonical document.
- Never report chunk count as document count.
- Deduplicate by canonical document before answer context and citation display.
- Use business intent routing for process, screen, regulation, presentation, integration and error questions.
- Validate production readiness with golden questions, including duplicate-record cases.
- Start broad answers with a short explanation of the term, then offer deeper paths.
- Keep unanswered questions, low-confidence answers and wrong citations in a curation queue.
- Track latency by retrieval stage: lexical, vector, rerank and generation.
