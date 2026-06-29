# MCP - SQL Server Plugin

## Supported MCP Servers

| ID | Uso |
|----|-----|
| mssql | SQL Server principal por env local |
| mssql-fiscal | SQL Server fiscal por env local |
| user-mssql | Alias legado |
| sqlserver | Alias generico documentacao |

## Portabilidade

- Usar `npx -y @mcp-collection/mssql-mcp` nos templates compartilhados.
- Nunca usar path fixo como `C:\Users\Danie\...`.
- Separar variaveis por conexao (`MSSQL_*`, `MSSQL_FISCAL_*`) para evitar mistura de credenciais.

## Required Environment Variables

- `MSSQL_HOST`, `MSSQL_PORT`, `MSSQL_USER`, `MSSQL_PASSWORD`, `MSSQL_DATABASE`
- `MSSQL_FISCAL_HOST`, `MSSQL_FISCAL_PORT`, `MSSQL_FISCAL_USER`, `MSSQL_FISCAL_PASSWORD`, `MSSQL_FISCAL_DATABASE`

## Connector files

| Arquivo | Proposito |
|---------|-----------|
| `ENV.example` | Variaveis sem valores |
| `MCP_CONFIG_CURSOR.example.json` | Template Cursor |
| `MCP_CONFIG_CODEX.example.toml` | Template Codex |
| `PERMISSIONS.md` | Escopo read/write |
| `USAGE.md` | Ativacao local |
| `HEALTH.md` | Checklist saude |

## Status

**under-review** - conector documentado; validacao MCP local pelo usuario.

> Nunca incluir valores reais.
