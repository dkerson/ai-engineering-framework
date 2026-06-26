# Usage — SQL Server Plugin

## Ativação local (Umbra / Irisys)

1. Copiar `ENV.example` → `.env` local (nunca commitar)
2. Copiar `MCP_CONFIG_CURSOR.example.json` → `.cursor/mcp.json` (ajustar paths)
3. Definir variáveis no OS ou `.env` carregado pelo Cursor
4. Reiniciar Cursor; verificar `HEALTH.md`

## Via Orchestrator

- Pedido: "Consulte tabelas do SQL Server do Umbra"
- Pipeline: plugin-resolver → sqlserver-plugin → **read-only** por default

## Escrita

Exige aprovação explícita: migration, UPDATE, DELETE, DDL.

## Referências

- `MCP.md` · `SECURITY.md` · `projects/umbra/mcp/`
