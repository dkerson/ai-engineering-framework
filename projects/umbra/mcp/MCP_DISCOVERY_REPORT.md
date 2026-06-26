# MCP Discovery Report — Umbra

> Gerado: 2026-06-26 · Skill: mcp-discovery-specialist · Sem secrets · Framework-only

## Projeto

| Campo | Valor |
|-------|-------|
| ID | umbra |
| Nome | Portal Otus7 (Umbra) |
| Monorepo | `Otus7/Umbra` |
| Stack | Angular 19 SPA + ASP.NET Core 8 API + SQL Server + Entra ID |

## Sinais detectados

| Sinal | Fonte | Plugin | MCP |
|-------|-------|--------|-----|
| SQL Server | `backend/`, `deploy/docker-compose.yml` (serviço `sql`) | sqlserver-plugin | **user-mssql** |
| Git / PRs | `.git`, regras `umbraotus7` / Otus7 | github-plugin | **github** |
| Docker deploy | `deploy/docker-compose.yml` | docker-plugin | **docker** |
| Microsoft Entra ID | `AzureAd` appsettings, MSAL frontend | azure-plugin | *(sem MCP connector v2.11)* |
| Observabilidade | — | sentry-plugin | sentry (**disabled** no projeto) |
| RAG / pgvector | planejado | postgres-plugin | *(futuro — não Umbra agora)* |

## Plugins validados para Umbra

| Plugin | Necessário | Status plugin | Prioridade | Risco |
|--------|------------|---------------|------------|-------|
| sqlserver-plugin | **Sim** | under-review | P0 | high |
| github-plugin | **Sim** | under-review | P0 | medium |
| docker-plugin | **Sim** (dev/deploy) | under-review | P1 | high |
| azure-plugin | Sim (auth) | draft | P2 | high — **config manual** |
| sentry-plugin | Opcional | active (disabled) | P3 | low |

## Plugins não necessários (Umbra)

postgres-plugin · powerbi-plugin · clickup-plugin · aws-plugin · firebase-plugin · supabase-plugin

## Capabilities envolvidas

- data-intelligence (SQL)
- development-intelligence (GitHub)
- infrastructure-intelligence (Docker, MCP)
- plugin-architecture
- rag-intelligence *(planned — sem MCP agora)*

## Modo default recomendado

| MCP | Dev local | Produção |
|-----|-----------|----------|
| user-mssql | read (+ write com aprovação) | **read-only** |
| github | read | read; push/merge com aprovação |
| docker | inspect | **blocked** / aprovação explícita |

## Artefatos gerados nesta missão

- `MCP_ACTIVATION_PLAN.md` — passos manuais
- `mcp.example.json` — Cursor (Umbra)
- `config.example.toml` — Codex (Umbra)
- Atualizações em MCP_PROFILE, MCP_SERVERS, MCP_ENV.example, MCP_RISK

## O que NÃO foi feito

- Nenhum secret configurado
- Nenhum `.cursor/mcp.json` real criado
- Nenhuma conexão testada
- Nenhum plugin promovido para `active` (exceto sentry global, disabled no Umbra)

## Referências

- `plugins/MCP_READINESS_AUDIT.md`
- `infrastructure/registry/MCP_SERVER_CATALOG.md`
