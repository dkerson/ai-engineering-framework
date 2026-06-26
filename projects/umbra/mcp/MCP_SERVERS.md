# MCP Servers — Umbra

> Discovery 2026-06-26 · Validado por mcp-discovery-specialist

## Obrigatórios (P0–P1)

| Server ID | Plugin | Status plugin | Env vars | Uso Umbra |
|-----------|--------|---------------|----------|-----------|
| user-mssql | sqlserver-plugin | under-review | `MSSQL_CONNECTION_STRING` | DB Umbra, EF migrations, queries |
| github | github-plugin | under-review | `GITHUB_TOKEN`, `GITHUB_OWNER` | Otus7/Umbra PRs, issues |
| docker | docker-plugin | under-review | `DOCKER_HOST` (opcional) | compose local sql/api/web |

## Futuro / manual

| Item | Plugin | Notas |
|------|--------|-------|
| Entra ID | azure-plugin (draft) | Config em appsettings + Entra portal — **sem MCP** |
| RAG/pgvector | postgres-plugin (draft) | Capability planned — não ativar agora |
| Sentry | sentry-plugin (active) | Disabled no projeto |

## Config examples

| Destino | Arquivo fonte |
|---------|---------------|
| Cursor | `projects/umbra/mcp/mcp.example.json` |
| Codex | `projects/umbra/mcp/config.example.toml` |
| Por plugin | `plugins/{plugin}/MCP_CONFIG_CURSOR.example.json` |

Catálogo global: `infrastructure/registry/MCP_SERVER_CATALOG.md`
