# Exemplo: Plugin Mission

## Ativar plugin em projeto

**Pedido:** "Ative o plugin do GitHub para o projeto Umbra."

**Modo:** Standard

**Pipeline:**
```text
Orchestrator → project-resolver → plugin-manager → PROJECT_PLUGINS.md → FOS
```

**Resultado:** `github-plugin` em Active Plugins do Umbra.

## Listar plugins com risco alto

**Pedido:** "Quais plugins têm risco alto?"

**Modo:** Fast

**Pipeline:** Orchestrator → plugin-manager → PLUGIN_REGISTRY.md (filtro)

**Resultado:** postgres, sqlserver, docker, supabase, firebase, azure, aws.

## Criar novo plugin

**Pedido:** "Crie um plugin para Oracle."

**Modo:** Standard

**Pipeline:** Orchestrator → plugin-builder → plugin-manager → FOS

Ver: `plugins/examples/create-oracle-plugin.md`

## Resolver em missão de dados

**Pedido:** "Consulte o SQL Server do Umbra."

**Modo:** Standard

**Pipeline:**
```text
Orchestrator → plugin-resolver → sqlserver-plugin → data-orchestrator
```

**Nota:** Plugin em draft — documentação OK; MCP real pendente.
