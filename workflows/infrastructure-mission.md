# Workflow: Infrastructure Mission

> Registrar, atualizar, descobrir ou consultar infraestrutura sem armazenar credenciais reais.

## Trigger

Adicionar, cadastrar, atualizar, conectar, configurar, registrar, novo banco, novo Git, nova API, novo servico, novo MCP, nova integracao.

## Pipeline

```text
Infrastructure Mission
-> Project Resolver
-> Infrastructure Discovery*
-> Project Scanner
-> Integration Resolver*
-> Registry Update
-> Infrastructure Dashboard
-> Infrastructure Health
-> FOS Update
```

`*` Quando necessario.

## Regras

- Nunca armazenar credenciais reais.
- Nunca criar `.env` real.
- Criar/atualizar apenas placeholders e documentacao.
- Atualizar Project Registry e Infrastructure Registry.
- Atualizar FOS quando houver mudanca aprovada.

## Skills

`project-resolver`, `infrastructure-discovery`, `project-scanner`, `integration-resolver`, `security-review`, `validator`

## Referencias

- `docs/Infrastructure-Intelligence.md`
- `rules/infrastructure-secrets.md`
- `rules/infrastructure-registry.md`
