# MCP Risk — Umbra

> Discovery 2026-06-26

| MCP | Risco | Mitigação Umbra |
|-----|-------|-----------------|
| user-mssql | **high** | SELECT default; DDL/DML prod bloqueado sem aprovação |
| github | medium | Sem push/merge automático; PR review read-first |
| docker | **high** | Inspect only; sem `docker compose up` via agente sem pedido |
| azure (manual) | high | Secrets só appsettings local / CI — nunca repo |
| sentry | low | Disabled no projeto |

## Ações que exigem aprovação explícita

- INSERT/UPDATE/DELETE/DDL em SQL (especialmente produção)
- git push, merge, delete branch
- docker deploy, compose down, image push
- Alteração Entra ID / permissões Azure

Ver `rules/mcp-security.md` · `MCP_PERMISSIONS.md`
