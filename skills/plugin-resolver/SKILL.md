---
name: plugin-resolver
description: >-
  Identifica quando uma missão precisa de plugin, seleciona o plugin correto, verifica permissões e riscos, aciona Security Policy Check e entrega contexto ao Master Orchestrator. Invocado somente pelo Orchestrator antes de integrações externas.
---

# Plugin Resolver

## Objetivo

Conectar missões do Orchestrator ao plugin certo, com governança de segurança e economia de tokens.

## Quando usar

- Missão envolve serviço externo (Git, DB, BI, cloud, observabilidade)
- Infrastructure Mission detectou recurso com plugin disponível
- Usuário menciona ferramenta integrada (Sentry, ClickUp, Power BI, etc.)
- Antes de acionar MCP relacionado a plugin

## Quando NÃO usar

- Cadastro ou listagem de plugins (usar `plugin-manager`)
- Criação de novo plugin (usar `plugin-builder`)
- Missão puramente local sem integração externa

## Responsabilidades

1. Identificar se a missão requer plugin (sinais no pedido + Project Registry).
2. Selecionar plugin correto via `PLUGIN_REGISTRY.md` e `PROJECT_PLUGINS.md`.
3. Verificar status (`active`/`draft`/`disabled` — draft permite doc-only).
4. Verificar permissões declaradas vs ação solicitada.
5. Verificar nível de risco e `access_mode`.
6. Verificar MCP relacionado disponível (`MCP.md` do plugin).
7. Acionar `security-review` + `risk-reviewer` se ação destrutiva ou risco high/critical.
8. Entregar ao Orchestrator: plugin ID, MCP, env vars necessárias (nomes), aprovações pendentes.

## Ações destrutivas (sempre exigem aprovação)

push · merge · deploy · migration · delete · update em banco · alteração em task · alteração em produção · exclusão de recurso · alteração de permissão

## Orquestração hierárquica

- **Nunca** fala com usuário — Orchestrator consolida
- **Invocação:** Orchestrator ou `integration-resolver` em Infrastructure Mission
- **Working Context:** plugin selecionado + checks de segurança
- **Economia:** carregar só `PLUGIN.md`, `MCP.md`, `SECURITY.md` do plugin escolhido

## Algoritmo

```
1. Extrair sinais (serviço, MCP, projeto) do pedido
2. Consultar PROJECT_PLUGINS.md do projeto
3. Mapear sinal → plugin via PLUGIN_REGISTRY.md
4. SE plugin disabled/removed → informar Orchestrator; sugerir alternativa
5. SE plugin planned/draft → permitir documentação; bloquear execução real
6. Verificar access_mode vs ação
7. SE destrutiva OU risco high+ → security-review + risk-reviewer → flag aprovação
8. Retornar pacote de resolução ao Orchestrator
```

## Entradas esperadas

- Working Context com missão classificada
- Projeto resolvido (project-resolver)

## Saídas esperadas

- `plugin_id`, `mcp_servers[]`, `env_vars[]`, `risk`, `access_mode`
- `approval_required: true/false`
- Skills de domínio sugeridas downstream

## Integração com outras skills

- **Upstream:** orchestrator, integration-resolver, infrastructure-discovery
- **Downstream:** skills de domínio + MCP (quando implementado)
- **Governança:** security-review, risk-reviewer

## Exemplos

**Input:** "Otimize query no SQL Server do Umbra."

**Output:** `sqlserver-plugin`, MCP `user-mssql`, risco high, read OK; write exige aprovação.

**Input:** "Veja erros no Sentry."

**Output:** `sentry-plugin`, read-only, risco low, sem aprovação.

## Referências

- `plugins/PLUGIN_REGISTRY.md`
- `plugins/PLUGIN_POLICY.md`
- `skills/integration-resolver/SKILL.md`
- `docs/PLUGIN_ARCHITECTURE.md`
