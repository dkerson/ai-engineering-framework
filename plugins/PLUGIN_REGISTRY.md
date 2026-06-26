# Plugin Registry — Registro Central

> Última atualização: 2026-06-26 · Framework v2.11.0

Registro canônico de todos os plugins. Plugin Manager mantém este arquivo; Plugin Resolver consulta antes de cada missão.

## Legenda

| Campo | Valores |
|-------|---------|
| **Status** | `planned` · `draft` · `under-review` · `active` · `deprecated` · `disabled` · `removed` |
| **Lifecycle** | `proposed` · `reviewed` · `approved` · `implemented` · `active` · `deprecated` · `removed` |
| **Tipo** | `vcs` · `database` · `bi` · `productivity` · `observability` · `devops` · `backend` · `cloud` |
| **Access** | `read-only` · `read-write` · `admin` |
| **Risco** | `low` · `medium` · `high` · `critical` |

---

## github-plugin

| Campo | Valor |
|-------|-------|
| Status | under-review |
| Lifecycle | implemented |
| Versão | 0.2.0 |
| Tipo | vcs |
| MCP Readiness | Conector v2.11 completo |
| Projetos associados | umbra, irisys |
| Dependências | — |
| MCP relacionado | github |
| Permissões | repos:read, repos:write, pull_requests, issues |
| Access | read-write |
| Risco | medium |
| Owner | framework |
| Documentação | `plugins/github-plugin/` |
| Exemplos | `plugins/github-plugin/EXAMPLES.md` |

---

## postgres-plugin

| Campo | Valor |
|-------|-------|
| Status | draft |
| MCP Readiness | Conector v2.11 · RAG pgvector gap |
| Lifecycle | implemented |
| Versão | 0.2.0 |
| Tipo | database |
| Projetos associados | — |
| Dependências | — |
| MCP relacionado | postgres |
| Permissões | schema:read, schema:write, data:read, data:write |
| Access | read-write |
| Risco | high |
| Owner | framework |
| Documentação | `plugins/postgres-plugin/` |
| Exemplos | `plugins/postgres-plugin/EXAMPLES.md` |

---

## sqlserver-plugin

| Campo | Valor |
|-------|-------|
| Status | under-review |
| Lifecycle | implemented |
| Versão | 0.2.0 |
| Tipo | database |
| MCP Readiness | Conector v2.11 · user-mssql |
| Projetos associados | umbra, irisys |
| Dependências | — |
| MCP relacionado | sqlserver, user-mssql |
| Permissões | schema:read, schema:write, data:read, data:write |
| Access | read-write |
| Risco | high |
| Owner | framework |
| Documentação | `plugins/sqlserver-plugin/` |
| Exemplos | `plugins/sqlserver-plugin/EXAMPLES.md` |

---

## powerbi-plugin

| Campo | Valor |
|-------|-------|
| Status | draft |
| Lifecycle | implemented |
| Versão | 0.1.0 |
| Tipo | bi |
| Projetos associados | irisys (planejado) |
| Dependências | sqlserver-plugin ou postgres-plugin (fonte de dados) |
| MCP relacionado | powerbi |
| Permissões | workspace:read, dataset:read, dataset:write, report:publish |
| Access | read-write |
| Risco | medium |
| Owner | framework |
| Documentação | `plugins/powerbi-plugin/` |
| Exemplos | `plugins/powerbi-plugin/EXAMPLES.md` |

---

## clickup-plugin

| Campo | Valor |
|-------|-------|
| Status | draft |
| Lifecycle | implemented |
| Versão | 0.1.0 |
| Tipo | productivity |
| Projetos associados | irisys (planejado) |
| Dependências | — |
| MCP relacionado | clickup |
| Permissões | tasks:read, tasks:write, lists:read |
| Access | read-write |
| Risco | medium |
| Owner | framework |
| Documentação | `plugins/clickup-plugin/` |
| Exemplos | `plugins/clickup-plugin/EXAMPLES.md` |

---

## sentry-plugin

| Campo | Valor |
|-------|-------|
| Status | **active** |
| Lifecycle | active |
| Versão | 0.2.0 |
| Tipo | observability |
| MCP Readiness | Conector v2.11 · read-only global |
| Projetos associados | — |
| Dependências | — |
| MCP relacionado | sentry |
| Permissões | events:read, issues:read, projects:read |
| Access | read-only |
| Risco | low |
| Owner | framework |
| Documentação | `plugins/sentry-plugin/` |
| Exemplos | `plugins/sentry-plugin/EXAMPLES.md` |

---

## docker-plugin

| Campo | Valor |
|-------|-------|
| Status | under-review |
| Lifecycle | implemented |
| Versão | 0.2.0 |
| Tipo | devops |
| MCP Readiness | Conector v2.11 completo |
| Projetos associados | umbra |
| Dependências | — |
| MCP relacionado | docker |
| Permissões | containers:read, containers:write, images:read, compose:read |
| Access | read-write |
| Risco | high |
| Owner | framework |
| Documentação | `plugins/docker-plugin/` |
| Exemplos | `plugins/docker-plugin/EXAMPLES.md` |

---

## supabase-plugin

| Campo | Valor |
|-------|-------|
| Status | draft |
| Lifecycle | implemented |
| Versão | 0.1.0 |
| Tipo | backend |
| Projetos associados | — |
| Dependências | postgres-plugin (opcional) |
| MCP relacionado | supabase |
| Permissões | auth:read, database:read, database:write, storage:read |
| Access | read-write |
| Risco | high |
| Owner | framework |
| Documentação | `plugins/supabase-plugin/` |
| Exemplos | `plugins/supabase-plugin/EXAMPLES.md` |

---

## firebase-plugin

| Campo | Valor |
|-------|-------|
| Status | draft |
| Lifecycle | implemented |
| Versão | 0.1.0 |
| Tipo | backend |
| Projetos associados | — |
| Dependências | — |
| MCP relacionado | firebase |
| Permissões | firestore:read, firestore:write, auth:read, storage:read |
| Access | read-write |
| Risco | high |
| Owner | framework |
| Documentação | `plugins/firebase-plugin/` |
| Exemplos | `plugins/firebase-plugin/EXAMPLES.md` |

---

## azure-plugin

| Campo | Valor |
|-------|-------|
| Status | draft |
| Lifecycle | implemented |
| Versão | 0.1.0 |
| Tipo | cloud |
| Projetos associados | umbra (Entra ID) |
| Dependências | — |
| MCP relacionado | azure |
| Permissões | resources:read, resources:write, identity:read |
| Access | read-write |
| Risco | high |
| Owner | framework |
| Documentação | `plugins/azure-plugin/` |
| Exemplos | `plugins/azure-plugin/EXAMPLES.md` |

---

## aws-plugin

| Campo | Valor |
|-------|-------|
| Status | draft |
| Lifecycle | implemented |
| Versão | 0.1.0 |
| Tipo | cloud |
| Projetos associados | — |
| Dependências | — |
| MCP relacionado | aws |
| Permissões | s3:read, s3:write, lambda:read, iam:read |
| Access | read-write |
| Risco | high |
| Owner | framework |
| Documentação | `plugins/aws-plugin/` |
| Exemplos | `plugins/aws-plugin/EXAMPLES.md` |

---

## Índice rápido

| Plugin | Status | Risco | Access | MCP |
|--------|--------|-------|--------|-----|
| github-plugin | under-review | medium | read-write | github |
| postgres-plugin | draft | high | read-write | postgres |
| sqlserver-plugin | under-review | high | read-write | user-mssql |
| powerbi-plugin | draft | medium | read-write | powerbi |
| clickup-plugin | draft | medium | read-write | clickup |
| sentry-plugin | **active** | low | read-only | sentry |
| docker-plugin | under-review | high | read-write | docker |
| supabase-plugin | draft | high | read-write | supabase |
| firebase-plugin | draft | high | read-write | firebase |
| azure-plugin | draft | high | read-write | azure |
| aws-plugin | draft | high | read-write | aws |

## Saúde do registry

Ver `framework/operating-system/health/PLUGIN_HEALTH.md`.
