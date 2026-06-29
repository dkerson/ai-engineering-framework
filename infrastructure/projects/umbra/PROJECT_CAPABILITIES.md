# Project Capabilities — Umbra

> Projetos declaram **Capabilities**, não Skills. Orchestrator decide skills.

## Active Capabilities

- development-intelligence
- data-intelligence
- product-design-intelligence
- infrastructure-intelligence
- plugin-architecture
- security-intelligence
- knowledge-quality-governance

## Planned Capabilities

- rag-intelligence (fase futura: depende de Azure OpenAI e banco vetorial/Postgres provisionados)
- semantic-retrieval (fase futura: embeddings, citações e avaliação de respostas)

## Disabled Capabilities

- (nenhum)

## Notas

- Plugins (sqlserver, github, docker, azure) via plugin-architecture capability
- RAG semântico não ativo — aguarda credenciais Azure OpenAI e banco vetorial/Postgres
- Enquanto isso, Umbra usa índice lexical (`KbContentChunks`) e relatório administrativo de saúde da KB

## Referências

- `capabilities/registry/CAPABILITY_REGISTRY.md`
- `PROJECT_PLUGINS.md`
