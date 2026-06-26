# Exemplos — Plugin Architecture

> Cenários de uso natural após v2.8.0.

## Ativar plugin em projeto

**Pedido:** "Ative o plugin do GitHub para o projeto Umbra."

**Pipeline:** Plugin Manager → atualiza `infrastructure/projects/umbra/PROJECT_PLUGINS.md` → Plugin Registry → FOS.

## Listar plugins ativos

**Pedido:** "Liste plugins ativos."

**Pipeline:** Plugin Manager → lê `PLUGIN_REGISTRY.md` + Project Registry → resposta consolidada.

## Criar novo plugin

**Pedido:** "Crie um plugin para Oracle."

**Pipeline:** Plugin Builder → `PLUGIN_TEMPLATE.md` → validação Plugin Manager → Registry → FOS.

Ver: `plugins/examples/create-oracle-plugin.md`

## Resolver plugin em missão

**Pedido:** "Otimize query no PostgreSQL do Irisys."

**Pipeline:** Orchestrator → Plugin Resolver → `postgres-plugin` → verifica permissões → `data-orchestrator`.

## Infrastructure Intelligence + plugin

**Pedido:** "Cadastre o banco SQL Server do Umbra."

**Pipeline:** Infrastructure Mission → detecta SQL Server → Plugin Resolver verifica `sqlserver-plugin` → registra uso no projeto.

## Plugins com risco alto

**Pedido:** "Quais plugins têm risco alto?"

**Pipeline:** Plugin Manager → filtra Registry por `Risco: high` → inclui PLUGIN_HEALTH.

## Desativar plugin

**Pedido:** "Desative o plugin do Sentry no Irisys."

**Pipeline:** Plugin Manager → move para Disabled em `PROJECT_PLUGINS.md` → status `disabled` no projeto.

## Permissões de escrita

**Pedido:** "Quais plugins têm permissão de escrita?"

**Pipeline:** Plugin Manager → filtra `Access: read-write` ou `admin`.
