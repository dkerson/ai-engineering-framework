# Security Access Control

> Regras para autorizacao, nivel de acesso, RBAC/ABAC, tenants, escopos e acoes sensiveis.

## Principios

- Deny by default.
- Least privilege.
- Server-side authorization before protected action.
- Permission checks before data fetch, ranking, export or mutation.
- Tenant isolation before business filtering.
- UI gating never replaces backend enforcement.

## Modelo minimo

Toda decisao de acesso deve identificar:

- Subject: usuario, service account ou sistema.
- Tenant/org: contexto de isolamento.
- Resource: entidade, documento, registro, endpoint ou acao.
- Action: read, create, update, delete, approve, export, admin.
- Policy source: role, attribute, ownership, plan, feature flag ou regra explicita.
- Decision: allow/deny + motivo.

## Regras de implementacao

- Nunca confiar em claims antigas sem versao, expiracao ou revalidacao.
- Incluir `tenant_id`/org no escopo de queries e caches.
- Validar ownership no backend em toda mutacao.
- Separar permissoes administrativas de permissoes operacionais.
- Evitar roles globais quando o produto for multi-tenant.
- Acoes destrutivas devem revalidar permissao imediatamente antes da execucao.
- Exportacao, relatorio e busca precisam aplicar o mesmo filtro de permissao da tela/API.

## Sinais de risco alto

- Role `admin` ampla sem escopo.
- Permissao calculada no frontend.
- Cache compartilhado entre tenants.
- Query sem filtro de tenant.
- Endpoint protegido apenas por rota/middleware generico.
- Alteracao de permissao sem auditoria.
- Permissao baseada em nome de cargo textual sem controle de versao.
