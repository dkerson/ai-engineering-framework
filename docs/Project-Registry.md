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

## Regras

- Registrar infraestrutura conhecida.
- Usar placeholders para segredos.
- Atualizar registry global quando projeto mudar.
- Registrar pendencias e lacunas.
- Nunca apagar historico sem justificativa.
