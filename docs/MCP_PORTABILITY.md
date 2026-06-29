# MCP Portability & Local Secrets

> Guia para configurar MCPs em maquinas diferentes sem depender do computador de outra pessoa e sem versionar secrets.

## Objetivo

Garantir que templates MCP funcionem no computador do usuario atual, em vez de apontar para paths locais como `C:\Users\Danie\...`.

## Padrao recomendado

| Conexao | Padrao |
|---------|--------|
| ClickUp | MCP remoto `https://mcp.clickup.com/mcp` com OAuth |
| GitHub | MCP remoto `https://api.githubcopilot.com/mcp/` com OAuth quando suportado |
| Context7 | MCP remoto `https://mcp.context7.com/mcp` com API key por env/header |
| MSSQL | `npx -y @mcp-collection/mssql-mcp` com env vars locais |

## Nunca versionar

- Tokens `ghp_...`
- API keys
- Senhas SQL
- Connection strings reais
- `.cursor/mcp.json` real
- `.codex/config.toml` real
- `.env` real

## MSSQL

Usar variaveis separadas por conexao:

- `MSSQL_*` para banco principal
- `MSSQL_FISCAL_*` para banco fiscal

Isso evita misturar usuarios, bancos e senhas.

## Validacao local

1. Confirmar `node -v`, `npm -v` e `npx`.
2. Copiar o template para config local.
3. Preencher variaveis reais fora do repo.
4. Testar health/read-only primeiro.
5. Promover status do MCP somente apos validacao.
