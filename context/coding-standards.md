# Coding Standards Context — Umbra

> Convenções de código observadas no monorepo Umbra.

## Geral

- Idioma UI e mensagens ao usuário: **pt-BR**
- Commits: conventional commits; identidade git **umbraotus7** (Umbra / umbra@otus7.com)
- Não commitar salvo pedido explícito do usuário
- Menor alteração possível — evitar refatorações não solicitadas

## Backend (.NET 8)

### Estrutura
```
Umbra.Api/Controllers/     → endpoints HTTP
Umbra.Application/Abstractions/ → I*Service
Umbra.Application/<domínio>/      → DTOs
Umbra.Domain/Entities/     → entidades EF
Umbra.Infrastructure/Services/ → implementações
Umbra.Infrastructure/Data/   → DbContext, migrations, seeder
```

### Convenções
- `Nullable` e `ImplicitUsings` ativos
- Classes serviço/DTO frequentemente `sealed`
- Namespaces espelham pastas: `Umbra.Api.Controllers`, etc.
- JSON API: camelCase
- Autorização: `[Authorize(Policy = "perm:...")]`

### EF Core
- Config fluente: `UmbraModelConfiguration`
- Migrations em `Infrastructure/Data/Migrations/`
- Nunca alterar migration já aplicada — criar nova

### Limites agentes
- `dotnet build` permitido; ignorar file-lock se API rodando
- Preservar `ConnectionStrings` e `AzureAd` em appsettings

## Frontend (Angular 19)

### Estrutura
```
core/services/    → *-api.service.ts
core/models/      → *.models.ts
core/constants/   → constantes domínio
features/<dom>/   → pages + components
shared/ui/        → umbra-* components
layout/           → shell
```

### Convenções
- 100% standalone — sem NgModules
- Páginas rota: `*-page.component.ts`
- API services: `providedIn: 'root'`
- Control flow: `@if`, `@for` (não `*ngIf`/`*ngFor`)
- State: `signal()` / `computed()` preferidos
- SCSS por componente; tokens globais `--umbra-*`

### Limites agentes
- **Nunca** `npm run build` / `ng build`
- Usuário executa `npm start` (watch, porta 4300)

## Naming

| Contexto | Convenção |
|----------|-----------|
| C# classes | PascalCase |
| C# interfaces | `I` + PascalCase |
| C# private fields | `_camelCase` |
| API routes | kebab-case ou camelCase conforme existente |
| Angular components | PascalCase class, kebab-case selector `app-*` |
| Shared UI | selector `umbra-*` |
| Arquivos Angular | kebab-case |
| Permissões | `modulo.acao` (ex.: `kb.read`) |

## Testing

- Backend: testes unitários quando existirem no módulo
- Frontend: preferir testes do módulo alterado
- E2E: Playwright quando fluxo crítico
- Rodar apenas testes relacionados à mudança

## Security

- Validar input em endpoints
- Parameterized queries — nunca SQL concat
- Secrets em env/appsettings — nunca no código
- DOMPurify para HTML externo no frontend
- Autorização real no backend — guards frontend são UX only

## Documentação

- Arquitetura: manter `ARCHITECTURE.md` por área atualizado quando mudança estrutural
- Novas features KB: considerar screen-doc skill se aplicável
- ADRs significativos: `Personal-AI/templates/adr.md`

## Precedência de regras

1. Instrução explícita do usuário
2. `AGENTS.md` mais próximo do arquivo editado (`frontend/`, `backend/`)
3. `.cursor/rules/*.mdc` específico da área
4. `Personal-AI/rules/*`
5. Este arquivo
