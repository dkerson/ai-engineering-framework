# MCP Activation Plan — Umbra

> Configuração **manual** pelo desenvolvedor. O framework não grava credenciais.

## Pré-requisitos

- [ ] Node.js/npx disponível (MCP servers via npx)
- [ ] Docker Desktop (opcional — stack `deploy/docker-compose.yml`)
- [ ] SQL Server acessível (local `:1433` via compose ou instância dev)
- [ ] Conta GitHub `umbraotus7` com PAT de escopo mínimo

---

## Passo 1 — Variáveis de ambiente

```powershell
# Na raiz do monorepo UMBRA (c:\...\UMBRA)
copy Personal-AI\projects\umbra\mcp\MCP_ENV.example .env
```

Editar `.env` **localmente** (nunca commitar):

| Variável | O que preencher |
|----------|-----------------|
| `MSSQL_CONNECTION_STRING` | Connection string do SQL dev (Database=Umbra; TrustServerCertificate=True) |
| `GITHUB_TOKEN` | PAT GitHub — scopes: `repo` read (write só se necessário) |
| `GITHUB_OWNER` | `Otus7` |
| `DOCKER_HOST` | Vazio = default local (Windows: Docker Desktop) |

> Use a mesma connection string que a API usa em dev, **sem** copiar para o repositório.

---

## Passo 2 — Cursor MCP

```powershell
mkdir .cursor -ErrorAction SilentlyContinue
copy Personal-AI\projects\umbra\mcp\mcp.example.json .cursor\mcp.json
```

1. Garantir que `MSSQL_CONNECTION_STRING` e `GITHUB_TOKEN` existem no **ambiente do OS** (ou conforme suporte do Cursor a env vars).
2. Reiniciar Cursor.
3. Verificar em Settings → MCP que `user-mssql`, `github`, `docker` aparecem.

Alternativa agregada: `Personal-AI/.cursor/mcp.example.json` (equivalente).

---

## Passo 3 — Codex (opcional)

```powershell
mkdir .codex -ErrorAction SilentlyContinue
copy Personal-AI\projects\umbra\mcp\config.example.toml .codex\config.toml
```

Preencher env vars no shell antes de usar Codex.

---

## Passo 4 — Validar (checklist)

| MCP | Teste sugerido | Plugin HEALTH |
|-----|----------------|---------------|
| user-mssql | `SELECT 1` ou listar tabelas Umbra | `plugins/sqlserver-plugin/HEALTH.md` |
| github | Listar issues/PRs do repo Umbra | `plugins/github-plugin/HEALTH.md` |
| docker | `docker ps` (read-only) | `plugins/docker-plugin/HEALTH.md` |

---

## Passo 5 — Azure Entra ID (sem MCP)

`azure-plugin` está em **draft** — sem conector MCP v2.11.

Configurar manualmente:

- `backend/Umbra.Api/appsettings.Development.json` — seção `AzureAd`
- Variáveis de build frontend (`NG_APP_AZURE_*` em docker-compose)
- Portal Azure / Entra ID — **não** versionar secrets

---

## Passo 6 — Sentry (opcional)

Plugin **active** globalmente, mas **disabled** no Umbra (`PROJECT_PLUGINS.md`).

Para habilitar: mover para Active Plugins + copiar `plugins/sentry-plugin/ENV.example`.

---

## Promoção de plugins (requer aprovação)

| Plugin | Pode promover active? | Bloqueio |
|--------|----------------------|----------|
| sqlserver | Após Passo 4 OK | Validação humana + read-only prod |
| github | Após Passo 4 OK | push/merge sempre com aprovação |
| docker | Recomendado manter under-review | Risco deploy |

Pedir ao agente: *"Promova sqlserver-plugin para active se estiver pronto"* — somente após validação local.

---

## RAG futuro

`rag-intelligence` + `postgres-plugin` + pgvector — **não** faz parte desta ativação Umbra.

Ver `PROJECT_CAPABILITIES.md` (Planned).
