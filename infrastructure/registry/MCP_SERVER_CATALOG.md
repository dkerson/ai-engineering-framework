# MCP Server Catalog

> Catálogo global · v2.11.0 · Sem credenciais reais.

| Server ID | Plugin | Capability | Escopo default | Read | Write | Risco | Status plugin | Projetos |
|-----------|--------|------------|----------------|------|-------|-------|---------------|----------|
| user-mssql | sqlserver-plugin | data-intelligence | SQL Server local/dev | ✓ | Aprovação | high | under-review | umbra |
| github | github-plugin | development-intelligence | repos, PRs, issues | ✓ | Aprovação | medium | under-review | umbra, irisys |
| docker | docker-plugin | infrastructure-intelligence | containers, compose | ✓ | Aprovação | high | under-review | umbra |
| postgres | postgres-plugin | data-intelligence, rag | PostgreSQL + pgvector | ✓ | Aprovação | high | draft | — |
| powerbi | powerbi-plugin | data-intelligence | workspaces, datasets | ✓ | Aprovação | medium | draft | irisys (planejado) |
| clickup | clickup-plugin | growth-brand-intelligence | tasks, lists | ✓ | Aprovação | medium | draft | irisys (planejado) |
| sentry | sentry-plugin | infrastructure-intelligence | events, issues | ✓ | — | low | **active** | — |
| azure | azure-plugin | infrastructure-intelligence | Entra, resources | ✓ | Aprovação | high | draft | umbra |
| aws | aws-plugin | infrastructure-intelligence | S3, Lambda | ✓ | Aprovação | high | draft | — |

## Notas

- **user-mssql:** MCP local observado no workspace Umbra; config via env.
- **mssql/mssql-fiscal:** usar `npx -y @mcp-collection/mssql-mcp`; nunca path absoluto de usuario.
- **context7:** MCP remoto com API key por env/header placeholder.
- **clickup:** preferir MCP remoto oficial `https://mcp.clickup.com/mcp` com OAuth no cliente.
- **github:** preferir MCP remoto `https://api.githubcopilot.com/mcp/` com OAuth no cliente.
- **postgres + RAG:** pgvector requer postgres-plugin active + extensão — ver MCP_READINESS_AUDIT.
- **sentry:** único plugin **active** — read-only global.

## Referências

- `plugins/PLUGIN_REGISTRY.md`
- `projects/*/mcp/MCP_SERVERS.md`
