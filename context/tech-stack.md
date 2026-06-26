# Tech Stack Context — Umbra

> Stack tecnológica do monorepo Umbra.

## Backend

| Item | Tecnologia |
|------|------------|
| Linguagem | C# / .NET 8 |
| Framework | ASP.NET Core 8 (Minimal hosting + Controllers) |
| ORM | Entity Framework Core (SQL Server) |
| Auth | Microsoft.Identity.Web (JWT Entra ID) |
| Tempo real | SignalR |
| API docs | Swagger (Development) |
| JSON | camelCase |
| DI | Built-in (`DependencyInjection.cs`) |

**Sem:** MediatR, FluentValidation, AutoMapper — serviços + EF LINQ + mapeamento manual.

Solução: `backend/Umbra.sln`

## Frontend

| Item | Tecnologia |
|------|------------|
| Framework | Angular 19 |
| Estilo | Standalone components (sem NgModules) |
| Auth | `@azure/msal-angular` + `@azure/msal-browser` |
| State | Signals (`signal`, `computed`) — sem NgRx |
| HTTP | `HttpClient` + `MsalInterceptor` |
| Tempo real | `@microsoft/signalr` |
| CSS | SCSS, tokens `--umbra-*`, DM Sans |
| i18n | `LOCALE_ID: 'pt-BR'` |
| Sanitização HTML | DOMPurify (`SafeHtmlRenderComponent`) |

Projeto CLI: `umbra-web`, prefix `app`.

## Banco de dados

| Banco | Uso | Acesso |
|-------|-----|--------|
| SQL Server (DefaultConnection) | Umbra principal | EF Core + migrations |
| SQL Server (ClickUpSource) | Dados ClickUp | ADO.NET / repositório |
| SQL Server (IrisysSource) | Menu KB legacy | ADO.NET |

## Infra / DevOps

| Item | Tecnologia |
|------|------------|
| Container | Docker (frontend nginx + backend API) |
| Orquestração prod | CapRover |
| Proxy dev | `proxy.conf.json` (`/api` → `:5198`) |
| CI | GitHub Actions (imagens Docker) |

## Comandos (agentes)

| Área | Comando | Notas |
|------|---------|-------|
| Frontend dev | `npm start` (porta 4300) | **Nunca** `ng build` / `npm run build` |
| Backend dev | `dotnet run --project Umbra.Api` | Swagger `:5198` |
| Backend build | `dotnet build` | Ignorar file-lock se API rodando |
| Docker local | `docker compose -f deploy/docker-compose.yml up --build` | |
| EF migration | `dotnet ef migrations add` (Infrastructure) | |

## Portas

| Serviço | Porta |
|---------|-------|
| Angular dev | 4300 |
| API dev | 5198 |
| Swagger | 5198/swagger |

## Environment

| Arquivo | Uso |
|---------|-----|
| `environment.development.ts` | Dev local + IDs Entra |
| `environment.production.ts` | Gerado no Docker build |
| `appsettings.Development.json` | Connection strings dev |
| `appsettings.Production.json` | Prod (preservar credenciais) |

`apiUrl: ''` em prod → requests relativos via nginx/proxy.

## Git

- Repositório: `https://github.com/Otus7/Umbra.git`
- Branch produção: `main`
- Conta: **umbraotus7** (nunca dkerson pessoal)
