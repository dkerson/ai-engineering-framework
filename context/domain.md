# Domain Context — Umbra

> Entidades, módulos e regras de domínio do portal Umbra.

## Entidades principais (Umbra DB)

| Entidade | Descrição |
|----------|-----------|
| `User` | Usuário portal — `ExternalId` (oid Entra), e-mail, roles |
| `Role` | Papel com permissões — `IsSystemAdmin` → `portal.*` |
| `Permission` | Código `perm:modulo.acao` |
| `Module` | Agrupamento de permissões (rh, legal, pmo, kb, …) |
| `AuditLog` | Registro de ações auditadas |
| `SystemParameter` | Parâmetros configuráveis (alguns com segredo) |
| `Notification` | Notificações inbox + envio admin |
| `KbArticle` | Metadados artigo KB (conteúdo HTML em blob) |
| `KbSupplementaryDocument` | Documentos auxiliares KB |
| `ClickUpTask` | Tasks importadas/referência PMO |
| `ClickUpStatusGroup` | Grupos de status ClickUp |
| `ClickUpPriorityMapping` | Mapeamento prioridades |
| `ClickUpClientTier` | Tiers de cliente |
| `ClickUpStatusDescription` | Descrições de status |
| `ClickUpImportSnapshot` | Snapshot de import sprint |

## Domínios HTTP

### Auth (`/api/auth`)
- `GET /me` — usuário atual, roles, permissões; 403 se não registrado

### Admin (`/api/admin/*`)
- Users, Roles, Directory (Graph), AuditLogs, Parameters, Notifications

### PMO (`/api/pmo/*`)
- `clickup-sprint` — import Excel, dashboard, histórico, drilldown
- `clickup-references` — CRUD tabelas referência

### KB (`/api/kb`)
- Menu árvore (SQL Irisys)
- Artigos por menu/articleId (EF)
- Conteúdo HTML via Azure Blob
- Geração IA via Cursor Cloud Agent (artigos)

## Regras de negócio críticas

| ID | Regra |
|----|-------|
| RN01 | Sem pré-registro por e-mail → 403 em `/api/auth/me` |
| RN02 | `IsSystemAdmin` expande para permissão `portal.*` |
| RN03 | Permissão `manage` implica `view` na hierarquia admin |
| RN04 | Artigos KB não publicados exigem `kb.manage` |
| RN05 | Menu KB inativo oculto para usuários sem `kb.manage` |
| RN06 | Integrações externas retornam 503 ou DTO vazio se não configuradas |
| RN07 | Migrations EF aplicadas automaticamente no startup |
| RN08 | Seed idempotente (`UmbraDbSeeder`) — não duplica dados |

## Permissões observadas

```
admin.users.view / admin.users.manage
admin.roles.view / admin.roles.manage
admin.audit.view
admin.parameters.view / admin.parameters.manage
pmo.read / pmo.manage
kb.read / kb.manage
portal.*  (system admin)
```

## Eventos / side effects

- Alteração usuário/papel → invalida cache de permissões
- Envio notificação → persist + push SignalR (`user-{userId}`)
- Import sprint → snapshot + recálculo dashboard
- Audit middleware → append log em requests auditados

## KB — origens e tipos

- Origens: `KbArticleOrigins` (manual, geração IA, …)
- Tipos documento: `KbDocumentTypes`

Ver `Umbra.Domain/Kb/` e `Umbra.Infrastructure/Kb/`.
