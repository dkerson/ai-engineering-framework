# Infrastructure Intelligence

> Dominio responsavel por conhecer projetos, repositorios, bancos, servicos, APIs, filas, storage, cloud, MCPs, ambientes, dependencias e conexoes.

## Objetivo

Permitir que o usuario converse naturalmente para cadastrar, atualizar, consultar e auditar infraestrutura sem editar manualmente arquivos do framework.

## Escopo

- Projetos
- Repositorios
- Bancos
- Servicos
- APIs
- Filas
- Storage
- Cloud
- MCP Servers
- Observabilidade
- Ferramentas
- Credenciais por referencia
- Ambientes
- Dependencias

## Principios

- Nunca armazenar credenciais reais.
- Sempre usar placeholders, environment variables ou Secret Managers.
- Descobrir e registrar; nao modificar codigo.
- Atualizar Project Registry e Infrastructure Registry.
- Integrar com Framework Operating System.

## Infrastructure Mission

Acionada por termos como: adicionar, cadastrar, atualizar, conectar, configurar, registrar, novo banco, novo Git, nova API, novo servico, novo MCP ou nova integracao.

Pipeline:

```text
Infrastructure Mission -> Project Resolver -> Infrastructure Discovery
-> Plugin Resolver* -> Project Scanner -> Integration Resolver
-> Registry Update -> Dashboard/Health -> FOS update
```

`*` Plugin Resolver: antes de sugerir conexão, verificar se existe plugin para a tecnologia detectada (ex.: PostgreSQL → `postgres-plugin`). Se não existir, sugerir criação via Plugin Builder; se existir, registrar uso em `PROJECT_PLUGINS.md`.

## Referencias

- `rules/infrastructure-secrets.md`
- `workflows/infrastructure-mission.md`
- `infrastructure/registry/`
- `infrastructure/projects/`
