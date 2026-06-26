# Workflows — Docker Plugin

## Workflows acionados

| Workflow | Quando |
|----------|--------|
| `workflows/plugin-mission.md` | Cadastro, ativacao, listagem |
| `workflows/infrastructure-mission.md` | Descoberta de infra devops |
| Dominio especifico | Conforme tipo do plugin |

## Pipeline tipico

```text
Orchestrator -> Plugin Resolver -> docker-plugin -> MCP -> Dominio
```
