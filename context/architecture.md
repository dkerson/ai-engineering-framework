# Architecture Context — Umbra

> **Exemplo de consumidor** — AI Engineering Framework. Outros projetos substituem este arquivo via `context/_template/`.

## Visão geral

Monorepo **modular** — portal interno Otus7. SPA Angular 19 + API ASP.NET Core 8 + SQL Server + Microsoft Entra ID (MSAL).

```
Umbra/
├── frontend/   → Angular 19 standalone (umbra-web)
├── backend/    → .NET 8 em 4 camadas (Umbra.sln)
├── deploy/     → Docker, nginx, CapRover
├── docs/       → Arquitetura monorepo, Entra ID
└── Personal-AI/ → Framework de agentes
```

## Backend — camadas

```
Umbra.Api           → Controllers, Hubs, Middleware, Auth
Umbra.Application   → Abstractions (I*Service), DTOs
Umbra.Infrastructure → EF Core, Services, integrações
Umbra.Domain        → Entities, Enums
```

Referências: Domain ← Application ← Infrastructure ← Api.

Detalhe: [backend/ARCHITECTURE.md](../../backend/ARCHITECTURE.md)

## Frontend — camadas

```
layout/     → MainLayoutComponent, header, sidebar
features/   → admin, pmo, kb, auth, home, notifications, favorites
shared/ui/  → umbra-* (design system leve)
core/       → auth (MSAL), services HTTP, models, guards
```

100% standalone — sem NgModules. Detalhe: [frontend/ARCHITECTURE.md](../../frontend/ARCHITECTURE.md)

## Módulos principais

| Módulo | Backend | Frontend | Permissões |
|--------|---------|----------|------------|
| Admin | Users, Roles, Audit, Parameters, Notifications | `features/admin/` | `admin.*` |
| PMO (ClickUp) | Sprint reports, referências | `features/pmo/` | `pmo.read`, `pmo.manage` |
| KB (Irisys) | Menu, artigos, blob HTML | `features/kb/` | `kb.read`, `kb.manage` |
| Auth | `/api/auth/me`, RBAC | `core/auth/` | Entra + portal |

## Integrações externas

| Recurso | Config | Uso |
|---------|--------|-----|
| SQL Server (Umbra) | `DefaultConnection` | EF Core principal |
| SQL ClickUp | `ClickUpSource` | Import sprint, referências PMO |
| SQL Irisys | `IrisysSource` | Menu KB (ADO.NET) |
| Azure Blob | `Blob:*` | HTML artigos KB |
| Microsoft Graph | `Graph:*` | Directory, fotos usuários |
| Microsoft Entra ID | `AzureAd` | JWT + MSAL |

## Autenticação

1. Entra ID autentica (JWT bearer)
2. `/api/auth/me` liga pré-registro por e-mail
3. **Sem registro prévio → 403**
4. RBAC portal: roles + permissões (`perm:*`)
5. `Role.IsSystemAdmin` → `portal.*`

## Tempo real

- SignalR: `/hubs/notifications`
- Frontend: `NotificationCenterService` no MainLayout

## Deploy

- Dev: Angular `:4300` (proxy `/api` → `:5198`), API Swagger `:5198/swagger`
- Prod: Docker + nginx + CapRover — ver [deploy/CAPROVER.md](../../deploy/CAPROVER.md)

## Onde colocar código novo

| Tipo | Local |
|------|-------|
| Endpoint HTTP | `Umbra.Api/Controllers/` |
| Contrato serviço | `Umbra.Application/Abstractions/` |
| DTO | `Umbra.Application/<domínio>/` |
| Entidade | `Umbra.Domain/Entities/` |
| Implementação | `Umbra.Infrastructure/Services/` |
| API service frontend | `core/services/*-api.service.ts` |
| Página/feature | `features/<domínio>/` |
| UI reutilizável | `shared/ui/` |
