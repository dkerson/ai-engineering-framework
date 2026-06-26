# Project Registry

> Registro vivo de projetos e sua infraestrutura.

## Estrutura por projeto

Cada projeto em `infrastructure/projects/<project>/` deve possuir:

- `PROJECT_CONTEXT.md`
- `PROJECT_ARCHITECTURE.md`
- `PROJECT_INFRASTRUCTURE.md`
- `PROJECT_SERVICES.md`
- `PROJECT_DATABASES.md`
- `PROJECT_REPOSITORIES.md`
- `PROJECT_APIS.md`
- `PROJECT_ENVIRONMENTS.md`
- `PROJECT_MCP.md`
- `PROJECT_SECURITY.md`
- `PROJECT_VALIDATION.md`
- `PROJECT_DEPENDENCIES.md`
- `PROJECT_METADATA.md`
- `PROJECT_PLUGINS.md`
- `PROJECT_CAPABILITIES.md`

## Project Plugins

Cada projeto declara plugins ativos e desativados em `PROJECT_PLUGINS.md`:

```markdown
# Project Plugins — Irisys

## Active Plugins
- github-plugin
- sqlserver-plugin
- powerbi-plugin
- clickup-plugin

## Disabled Plugins
- sentry-plugin
```

Plugin Manager atualiza este arquivo; Plugin Resolver consulta antes de missões com integração externa.

## Project Capabilities (COS v2.10+)

Cada projeto declara **capabilities** (não skills) em `PROJECT_CAPABILITIES.md`:

```markdown
## Active Capabilities
- development-intelligence
- data-intelligence
- rag-intelligence
```

Orchestrator escolhe skills com base nas capabilities ativas.

Ver: `docs/CAPABILITY_OPERATING_SYSTEM.md` · `capabilities/registry/CAPABILITY_REGISTRY.md`

## Regras

- Registrar infraestrutura conhecida.
- Usar placeholders para segredos.
- Atualizar registry global quando projeto mudar.
- Registrar pendencias e lacunas.
- Nunca apagar historico sem justificativa.
