# MCP Profile — Umbra

> Portal Otus7 · Discovery 2026-06-26 · Sem secrets no repo.

## Resumo discovery

| Prioridade | MCP | Plugin | Status |
|------------|-----|--------|--------|
| P0 | user-mssql | sqlserver-plugin | under-review |
| P0 | github | github-plugin | under-review |
| P1 | docker | docker-plugin | under-review |
| P2 | — | azure-plugin | draft (Entra — manual) |
| — | sentry | sentry-plugin | disabled |

Relatório completo: `MCP_DISCOVERY_REPORT.md`  
Plano manual: `MCP_ACTIVATION_PLAN.md`

## Stack detectada

- **Backend:** ASP.NET Core 8, EF Core, SQL Server (`Umbra` DB)
- **Frontend:** Angular 19, proxy `/api` → `:5198`
- **Deploy:** `deploy/docker-compose.yml` (sql, api, web)
- **Auth:** Microsoft Entra ID (MSAL) — sem MCP connector ainda

## Arquivos de exemplo (Umbra)

| Arquivo | Uso |
|---------|-----|
| `MCP_ENV.example` | Template `.env` local |
| `mcp.example.json` | Template `.cursor/mcp.json` |
| `config.example.toml` | Template `.codex/config.toml` |

## Ativação rápida

Ver `MCP_ACTIVATION_PLAN.md` — 6 passos, zero secrets no git.

## Referências

- `MCP_SERVERS.md` · `MCP_PERMISSIONS.md` · `MCP_RISK.md`
- `infrastructure/projects/umbra/PROJECT_PLUGINS.md`
