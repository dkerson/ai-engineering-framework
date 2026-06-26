# Permissions — PostgreSQL Plugin

| Escopo | Default | Write exige aprovação |
|--------|---------|----------------------|
| data:read | ✓ dev | ✓ prod |
| schema:read | ✓ | ✓ prod |
| data:write | ✗ | ✓ |
| pgvector index | ✗ | ✓ (RAG) |

**RAG gap:** requer extensão `vector` + postgres-plugin active.

Capability pai: data-intelligence, rag-intelligence
