# Patterns Context — Umbra

> Padrões arquiteturais observados no código Umbra.

## Backend

### Layered Architecture (4 camadas)
Api → Application (interfaces) → Infrastructure (implementação) → Domain (entidades).

Domain **nunca** referencia Application ou Infrastructure.

### Service + Interface
- Contrato: `Umbra.Application/Abstractions/I*Service.cs`
- Implementação: `Umbra.Infrastructure/Services/*Service.cs`
- Registro DI: `Infrastructure/DependencyInjection.cs`

### Repository implícito via EF
Sem camada Repository explícita — serviços usam `UmbraDbContext` diretamente.

### Manual mapping
DTOs mapeados manualmente nos serviços — sem AutoMapper.

### Options pattern
Configuração tipada em `Infrastructure/Options/` (ex.: `ClickUpSourceOptions`, `KbGenerationOptions`).

### Idempotent seed
`UmbraDbSeeder.Ensure*Async` — métodos idempotentes no startup.

### Permission policies
Políticas ASP.NET `perm:*` + `PortalPermissionAuthorizationHandler` + cache em memória.

### Integração graceful degradation
Serviços expõem `IsConfigured` — controllers retornam 503 quando credenciais ausentes.

## Frontend

### Standalone + lazy loading
`loadComponent: () => import(...)` em `app.routes.ts`.

### Feature folders
`features/<domínio>/` com pages (`*-page.component.ts`) e sub-componentes.

### API service per resource
`core/services/*-api.service.ts` — um serviço HTTP por recurso REST.

### Signals for state
`signal()` / `computed()` — sem NgRx. Stores imperativos em serviços quando necessário (ex.: `ClickUpSprintReportStore`).

### Guard chain
`authGuard` → `permissionGuard('perm.code')` nas rotas protegidas.

### Shared UI prefix
Componentes reutilizáveis: `umbra-*` em `shared/ui/`.

### Safe HTML pipeline
DOMPurify antes de renderizar HTML externo (KB, notificações).

## Cross-cutting

### Audit middleware
`AuditRequestMiddleware` — log automático de requests.

### SignalR notifications
Hub `/hubs/notifications` + publisher na camada Api.

### Cursor Cloud Agent (KB)
Geração de artigos KB via agente externo — monitor worker + finalizer.

## Anti-patterns a evitar

- Referenciar Infrastructure a partir de Domain
- Lógica de negócio em Controllers (delegar a serviços)
- `ng build` por agentes (usuário usa watch)
- Commitar secrets ou apagar ConnectionStrings/AzureAd
- Permissões só no frontend (backend é autoridade)
- SELECT * ou queries sem índice em hot paths
- Abrir dezenas de arquivos sem investigação dirigida

## Referências internas

| Documento | Conteúdo |
|-----------|----------|
| [backend/ARCHITECTURE.md](../../backend/ARCHITECTURE.md) | API completa |
| [frontend/ARCHITECTURE.md](../../frontend/ARCHITECTURE.md) | SPA completa |
| [docs/architecture.md](../../docs/architecture.md) | Visão monorepo |
| [docs/entra-id.md](../../docs/entra-id.md) | Integração Entra |
| `.cursor/rules/backend-*.mdc` | Regras backend Cursor |
| `.cursor/rules/frontend-*.mdc` | Regras frontend Cursor |

## ADRs

Usar `Personal-AI/templates/adr.md` para decisões arquiteturais novas neste projeto.
