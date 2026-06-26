# Permissions — SQL Server Plugin

| Escopo | Default | Write exige aprovação |
|--------|---------|----------------------|
| schema:read | ✓ dev/staging | ✓ produção |
| data:read | ✓ | ✓ produção |
| schema:write | ✗ | ✓ explícita |
| data:write | ✗ | ✓ explícita |
| DDL/DROP | ✗ | ✓ Council |

## MCP tools

- `execute_sql` (user-mssql) — **read-only por padrão em produção**

## Capability pai

- data-intelligence
- infrastructure-intelligence

## Projetos

umbra, irisys
