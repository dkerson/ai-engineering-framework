# Infrastructure Registry

> Registry global de infraestrutura usada pelos projetos.

## Arquivos

- `projects.md`
- `repositories.md`
- `databases.md`
- `services.md`
- `providers.md`
- `cloud.md`
- `queues.md`
- `storage.md`
- `apis.md`
- `mcps.md`
- `integrations.md`
- `connections.md`

## Uso

O Orchestrator consulta esses registros para responder perguntas naturais como:

- Quais bancos existem no Irisys?
- Quais projetos usam Redis?
- Qual Git pertence ao Umbra?
- Qual MCP utilizamos para SQL?
- Quais conexoes existem?

## Segurança

Nenhum arquivo do registry deve conter token, senha, connection string, certificate, private key ou secret real.
