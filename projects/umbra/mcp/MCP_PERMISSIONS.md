# MCP Permissions — Umbra

> Default: **read-only em produção** · Discovery 2026-06-26

## Por MCP

| MCP | Permitido default | Exige aprovação |
|-----|-------------------|-----------------|
| user-mssql | SELECT, schema read (dev) | INSERT, UPDATE, DELETE, DDL, migration |
| github | read repo, issues, PRs | push, merge, delete branch, admin |
| docker | ps, inspect, logs | compose up/down, deploy, rm |

## Por ambiente

| Ambiente | SQL | GitHub | Docker |
|----------|-----|--------|--------|
| dev local | read (+ write com OK explícito) | read | read |
| staging | read | read | read |
| production | **read-only** | read | **blocked** |

## Plugins disabled

- **sentry-plugin** — sem permissões MCP ativas no Umbra

## Referências

- `plugins/sqlserver-plugin/PERMISSIONS.md`
- `plugins/github-plugin/PERMISSIONS.md`
- `plugins/docker-plugin/PERMISSIONS.md`
