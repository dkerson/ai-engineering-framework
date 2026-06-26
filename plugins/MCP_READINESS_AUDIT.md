# MCP Readiness Audit

> Data: 2026-06-26 · Framework v2.11.0

## Resumo executivo

| Métrica | Valor |
|---------|-------|
| Plugins total | 11 |
| Com MCP.md | 11/11 |
| Com conector completo (v2.11) | 7 prioritários |
| Active | 1 (sentry-plugin) |
| Under-review | 3 (sqlserver, github, docker) |
| Draft | 7 |

## 1. Plugins com MCP.md

Todos os 11 plugins possuem `MCP.md` básico desde v2.8.

## 2. Plugins em draft / under-review / active

| Plugin | Status anterior | Status v2.11 | Motivo |
|--------|-----------------|--------------|--------|
| sentry-plugin | draft | **active** | read-only; checklist completo |
| sqlserver-plugin | draft | **under-review** | Umbra/Irisys; user-mssql; risco high |
| github-plugin | draft | **under-review** | Umbra/Irisys; medium risk |
| docker-plugin | draft | **under-review** | Umbra deploy; high risk |
| postgres-plugin | draft | draft | RAG pgvector futuro; conector adicionado |
| powerbi-plugin | draft | draft | Irisys planejado; conector adicionado |
| clickup-plugin | draft | draft | Irisys planejado; conector adicionado |
| azure, aws, firebase, supabase | draft | draft | fora do lote prioritário |

## 3. Plugins que podem virar active

| Plugin | Pronto? | Bloqueio |
|--------|---------|----------|
| sentry-plugin | **Sim** | Promovido v2.11 |
| sqlserver-plugin | Não | Aprovação humana + validação local MCP |
| github-plugin | Não | Aprovação + escopo token |
| docker-plugin | Não | High risk deploy |

## 4. Plugins que precisam de MCP real

Todos — framework fornece **exemplos e conectores documentados**; usuário ativa localmente com credenciais.

Prioridade Umbra: **user-mssql**, **github**, **docker**.

Prioridade Irisys: **user-mssql**, **github**, **powerbi**, **clickup**.

## 5. Projects usando plugins

| Projeto | Plugins (PROJECT_PLUGINS) | MCP profile |
|---------|---------------------------|-------------|
| umbra | sqlserver, github, docker, azure | `projects/umbra/mcp/` |
| irisys | github, sqlserver, powerbi, clickup | `projects/irisys/mcp/` |
| rifsmart | (mínimo) | `projects/rifsmart/mcp/` |

## 6. Capabilities dependentes de MCP

| Capability | MCPs |
|------------|------|
| data-intelligence | user-mssql, postgres, powerbi |
| infrastructure-intelligence | docker, sentry, azure, github |
| rag-intelligence | postgres (pgvector) — **gap documentado** |
| development-intelligence | github |

## 7. Riscos

| Risco | Mitigação |
|-------|-----------|
| SQL write em produção | read-only default; aprovação explícita |
| GitHub push/merge | PERMISSIONS.md; orchestrator gate |
| Docker deploy acidental | under-review; não active |
| Secrets no repo | mcp-security rules; *.example only |
| ClickUp status change | regra explícita; read default |

## 8. Arquivos que faltavam (corrigidos v2.11)

- PERMISSIONS.md, USAGE.md, HEALTH.md, ENV.example por plugin prioritário
- MCP_CONFIG_CURSOR.example.json, MCP_CONFIG_CODEX.example.toml
- MCP_SERVER_CATALOG.md
- Project MCP profiles (`projects/*/mcp/`)
- `.cursor/mcp.example.json`, `.codex/config.example.toml`
- mcp-discovery-specialist skill
- PLUGIN_STATUS_POLICY.md, rules/mcp-security.md

## Conexão RAG + pgvector

**Gap:** postgres-plugin draft + extensão pgvector não configurada.

**Plano:** postgres-plugin active → MCP postgres → rag capability indexação. Ver RECOMMENDATIONS.md.
