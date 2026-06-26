# Workflows — PostgreSQL Plugin

## Workflows acionados

| Workflow | Quando |
|----------|--------|
| `workflows/plugin-mission.md` | Cadastro, ativacao, listagem |
| `workflows/infrastructure-mission.md` | Descoberta de infra database |
| Dominio especifico | Conforme tipo do plugin |

## Pipeline tipico

```text
Orchestrator -> Plugin Resolver -> postgres-plugin -> MCP -> Dominio
```
