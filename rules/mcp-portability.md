# MCP Portability

> Finalidade: garantir que configuracoes MCP funcionem em qualquer maquina do time sem paths de usuario, secrets versionados ou dependencias locais ocultas.

## Principio central

Templates MCP devem ser portateis. Nunca apontar para `C:\Users\{pessoa}\...`, pastas globais de outro usuario ou arquivos locais que nao existam no computador atual.

## Regras obrigatorias

- Preferir MCP remoto OAuth quando o provedor oferecer endpoint oficial.
- Preferir `npx -y <pacote>` para MCP stdio Node quando o pacote for publico e resolvivel.
- Se um caminho absoluto for inevitavel, usar variavel de ambiente (`${MCP_SERVER_PATH}`), nunca path fixo.
- Secrets reais ficam no ambiente local, keyring, OAuth do cliente ou secret manager.
- Templates versionados usam placeholders (`${VAR_NAME}`) e exemplos `.env.example`.
- Nao commitar `.cursor/mcp.json`, `.codex/config.toml` ou `.env` reais.

## Padrao por tipo

| Tipo | Padrao recomendado |
|------|--------------------|
| Remote OAuth | `type/http + url`, sem token no arquivo |
| Remote API key | `type/http + url + header placeholder` |
| Local stdio Node | `command: npx`, `args: ["-y", "package"]` |
| Local stdio custom | `command`/`args` via variaveis de ambiente |
| Banco de dados | env vars separadas por conexao ou connection string local |

## Anti-padroes

- `C:\Users\Danie\...` em template compartilhado.
- Token `ghp_...`, senha SQL, API key ou connection string real em JSON/TOML.
- Um unico `MSSQL_PASSWORD` reutilizado para bancos diferentes.
- MCP write habilitado sem permissao documentada.

## Validacao local

Antes de promover um MCP:

- confirmar que `node`, `npm` e `npx` funcionam;
- confirmar que o template nao tem path de outro usuario;
- confirmar que variaveis exigidas existem no ambiente local;
- testar health/read-only primeiro;
- registrar risco e permissoes.
