# Umbra Project MCP

> Perfil governado: `Personal-AI/projects/umbra/mcp/`  
> **Discovery:** 2026-06-26 (mcp-discovery-specialist)

## Servidores validados

| MCP | Plugin | Prioridade | Status plugin |
|-----|--------|------------|---------------|
| user-mssql | sqlserver-plugin | P0 | under-review |
| github | github-plugin | P0 | under-review |
| docker | docker-plugin | P1 | under-review |

## Documentação discovery

| Documento | Conteúdo |
|-----------|----------|
| [MCP_DISCOVERY_REPORT.md](../../projects/umbra/mcp/MCP_DISCOVERY_REPORT.md) | Análise completa |
| [MCP_ACTIVATION_PLAN.md](../../projects/umbra/mcp/MCP_ACTIVATION_PLAN.md) | Passos manuais |
| [mcp.example.json](../../projects/umbra/mcp/mcp.example.json) | Template Cursor |

## Ativação (manual)

1. `projects/umbra/mcp/MCP_ENV.example` → `.env` na raiz do monorepo
2. `projects/umbra/mcp/mcp.example.json` → `.cursor/mcp.json`
3. Preencher env vars no OS — **nunca commitar**
4. Reiniciar Cursor; validar checklist em `MCP_ACTIVATION_PLAN.md`

## Pendências manuais

- [ ] `MSSQL_CONNECTION_STRING` para DB Umbra dev
- [ ] `GITHUB_TOKEN` (PAT umbraotus7, escopo mínimo)
- [ ] Validar MCP user-mssql com query read-only
- [ ] Azure Entra — config manual (azure-plugin sem MCP)
- [ ] Promoção sqlserver/github/docker → `active` após validação

Ver `docs/MCP_GOVERNANCE.md`
