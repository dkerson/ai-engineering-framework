# Plugin Health Report — MCP Readiness

> v2.11.0 · Atualizado após MCP Readiness Audit

## Resumo

| Métrica | Valor |
|---------|-------|
| Total plugins | 11 |
| **active** | 1 (sentry-plugin) |
| **under-review** | 3 (sqlserver, github, docker) |
| draft | 7 |
| Com MCP.md | 11/11 |
| Com conector v2.11 (7 prioritários) | 7/7 |

## MCP connector completeness

| Plugin | MCP.md | PERMS | ENV | Cursor | Codex | USAGE | HEALTH |
|--------|--------|-------|-----|--------|-------|-------|--------|
| sentry | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| sqlserver | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| github | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| docker | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| postgres | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| powerbi | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| clickup | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| azure, aws, firebase, supabase | ✓ | — | — | — | — | — | — |

## Project MCP profiles

| Projeto | Perfil | Servidores |
|---------|--------|------------|
| umbra | ✓ | 3 under-review |
| irisys | ✓ | 4 (2 draft) |
| rifsmart | ✓ | 0 |

## Recomendações

1. Validar user-mssql localmente → promover sqlserver under-review → active
2. RAG+pgvector: postgres-plugin draft → under-review após Postgres disponível
3. Não promover docker/github active sem aprovação explícita

Ver `plugins/MCP_READINESS_AUDIT.md`
