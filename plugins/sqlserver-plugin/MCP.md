# MCP — SQL Server Plugin

## Supported MCP Servers

| ID | Uso |
|----|-----|
| user-mssql | MCP local SQL Server (workspace Umbra) |
| sqlserver | Alias genérico documentação |

## Required Environment Variables

- `MSSQL_CONNECTION_STRING` (preferido) ou `SQLSERVER_CONNECTION_STRING`
- `MSSQL_SERVER`
- `MSSQL_DATABASE`

## Connector files

| Arquivo | Propósito |
|---------|-----------|
| `ENV.example` | Variáveis sem valores |
| `MCP_CONFIG_CURSOR.example.json` | Template Cursor |
| `MCP_CONFIG_CODEX.example.toml` | Template Codex |
| `PERMISSIONS.md` | Escopo read/write |
| `USAGE.md` | Ativação local |
| `HEALTH.md` | Checklist saúde |

## Status

**under-review** — conector documentado; validação MCP local pelo usuário.

> Nunca incluir valores reais.
