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
