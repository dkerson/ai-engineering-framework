# MCP Servers - Umbra

> Discovery 2026-06-26. Atualizado v2.17 para portabilidade local.

## Portabilidade v2.17

- Nao usar paths `C:\Users\{pessoa}\...` em templates compartilhados.
- Preferir MCP remoto OAuth para ClickUp e GitHub.
- Usar `npx -y @mcp-collection/mssql-mcp` para MSSQL local.
- Separar `MSSQL_*` e `MSSQL_FISCAL_*`.
- Context7 usa MCP remoto com `CONTEXT7_API_KEY` por ambiente/header placeholder.

## Obrigatorios (P0-P1)

| Server ID | Plugin | Status plugin | Env vars | Uso Umbra |
|-----------|--------|---------------|----------|-----------|
| context7 | external/context7 | draft | `CONTEXT7_API_KEY` | Docs/contexto de bibliotecas |
| github | github-plugin | under-review | OAuth remoto / `GITHUB_TOKEN` fallback | Otus7/Umbra PRs, issues |
| clickup | clickup-plugin | draft | OAuth remoto | tasks, sprints, listas |
| mssql | sqlserver-plugin | under-review | `MSSQL_*` | DB principal dev |
| mssql-fiscal | sqlserver-plugin | under-review | `MSSQL_FISCAL_*` | DB fiscal dev |
| docker | docker-plugin | under-review | `DOCKER_HOST` opcional | compose local sql/api/web |

## Legado

| Server ID | Status | Nota |
|-----------|--------|------|
| user-mssql | legacy alias | Preferir `mssql` nos templates novos |

## Futuro / manual

| Item | Plugin | Notas |
|------|--------|-------|
| Entra ID | azure-plugin (draft) | Config em appsettings + Entra portal; sem MCP |
| RAG/pgvector | postgres-plugin (draft) | Capability planned; nao ativar agora |
| Sentry | sentry-plugin (active) | Disabled no projeto |

## Config examples

| Destino | Arquivo fonte |
|---------|---------------|
| Cursor | `projects/umbra/mcp/mcp.example.json` |
| Codex | `projects/umbra/mcp/config.example.toml` |
| Agregado Cursor | `.cursor/mcp.example.json` |
| Agregado Codex | `.codex/config.example.toml` |
| Por plugin | `plugins/{plugin}/MCP_CONFIG_CURSOR.example.json` |

Catalogo global: `infrastructure/registry/MCP_SERVER_CATALOG.md`
