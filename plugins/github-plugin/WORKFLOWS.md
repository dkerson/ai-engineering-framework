# Workflows — GitHub Plugin

## Workflows acionados

| Workflow | Quando |
|----------|--------|
| `workflows/plugin-mission.md` | Cadastro, ativacao, listagem |
| `workflows/infrastructure-mission.md` | Descoberta de infra vcs |
| Dominio especifico | Conforme tipo do plugin |

## Pipeline tipico

```text
Orchestrator -> Plugin Resolver -> github-plugin -> MCP -> Dominio
```
