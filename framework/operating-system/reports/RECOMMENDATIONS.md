# Framework Recommendations

> Gerado: 2026-06-26 · v2.11.0

## MCP Readiness v2.11

1. Validar **user-mssql** localmente → sqlserver active (read-only prod).
2. **postgres + pgvector** para RAG quando Postgres disponível.
3. docker/github: manter under-review até aprovação.

## Capability Architecture

1. **Adotar capability-first** em toda missão de tecnologia nova (OCR, voice, agents).
2. **RAG Stable** após primeiro projeto consumidor validar guardrails em produção.
3. **OCR Capability** — próximo candidato Planned → In Development (depende de RAG ingestão).

## COS v2.10

1. **Capability-first** é política — não convenção.
2. **PROJECT_CAPABILITIES** substitui listagem de skills por projeto.
3. **OCR** próxima capability Planned → Approved.

## RAG Intelligence

1. Definir vector DB plugin (postgres pgvector ou dedicado) quando projeto consumir RAG.
2. Benchmark com rag-evaluator antes de go-live.
3. Confidence threshold por projeto via template configurável.

## Geral

1. Manter distinção knowledge-engine (Hub) vs knowledge-architect (KB RAG).
2. Não implementar RAG em Umbra/Irisys/SmartRifa até missão explícita de produto aprovada.
