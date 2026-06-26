# Health — SQL Server Plugin

## Checklist

- [ ] MCP server `user-mssql` listado no Cursor
- [ ] Env vars definidas localmente (não no repo)
- [ ] Query SELECT de teste OK
- [ ] Write bloqueado sem aprovação
- [ ] Plugin status: under-review

## Sinais saudável

- Latência query < 5s dev
- Sem erros auth no log MCP

## Sinais unhealthy

- Connection refused → verificar MSSQL_SERVER / connection string
- Login failed → credenciais locais
