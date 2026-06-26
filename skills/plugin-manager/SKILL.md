---
name: plugin-manager
description: >-
  Cadastra, atualiza, lista, desativa e valida plugins do AI Engineering Framework. Mantém Plugin Registry e integra com FOS e Project Registry. Invocado somente pelo Orchestrator em missões de plugin ou infraestrutura.
---

# Plugin Manager

## Objetivo

Administrar o ciclo de vida operacional dos plugins sem inflar o núcleo do framework.

## Quando usar

- Cadastrar, ativar ou desativar plugin
- Listar plugins (ativos, por projeto, por risco, por permissão)
- Validar estrutura e política de plugin
- Impedir duplicação de responsabilidade
- Atualizar `PLUGIN_REGISTRY.md` e FOS

## Quando NÃO usar

- Selecionar plugin para uma missão técnica (usar `plugin-resolver`)
- Criar estrutura de novo plugin (usar `plugin-builder`)
- Implementar integração MCP real

## Responsabilidades

1. Cadastrar plugins no Registry (status, versão, metadados).
2. Atualizar plugins existentes (versão, status, permissões).
3. Listar plugins globais ou por projeto (`PROJECT_PLUGINS.md`).
4. Desativar plugins (status `disabled` no projeto ou global).
5. Sugerir plugins quando Infrastructure Intelligence detectar lacuna.
6. Validar plugin contra `PLUGIN_POLICY.md` e `PLUGIN_TEMPLATE.md`.
7. Impedir duplicação — consultar Registry antes de aprovar.
8. Atualizar `plugins/PLUGIN_REGISTRY.md`.
9. Promover status (`draft` → `under-review` → `active`) via `PLUGIN_STATUS_POLICY.md` + `checklists/mcp-readiness.md`.
10. Atualizar FOS e `MCP_SERVER_CATALOG.md`.

## Orquestração hierárquica

- **Único contato com usuário:** Orchestrator
- **Invocação:** somente via pipeline aprovado
- **Working Context:** registrar plugins afetados em bullets concisos
- **Modo Council:** máx. 150 palavras se consultado
- **Economia:** ler só entradas relevantes do Registry

## Entradas esperadas

- Pedido natural (ativar, listar, desativar, validar)
- Working Context com projeto resolvido (se aplicável)

## Saídas esperadas

- Registry atualizado
- `PROJECT_PLUGINS.md` atualizado (se por projeto)
- Entrada FOS quando mudança de status
- Resumo para Orchestrator (plugins afetados, status, riscos)

## Checklist

- [ ] Sem secrets nos arquivos alterados
- [ ] Status e lifecycle coerentes com `PLUGIN_LIFECYCLE.md`
- [ ] Duplicação verificada
- [ ] FOS atualizado se transição de status
- [ ] Working Context atualizado

## Integração com outras skills

- **Upstream:** orchestrator, plugin-builder
- **Downstream:** plugin-resolver (Registry como fonte)
- **Paralelo:** project-resolver (projeto), infrastructure-discovery

## Exemplos

**Input:** "Ative o plugin do GitHub para o projeto Umbra."

**Output:** `umbra/PROJECT_PLUGINS.md` → Active: github-plugin; Registry atualizado; FOS changelog.

**Input:** "Quais plugins têm risco alto?"

**Output:** Lista filtrada do Registry: postgres, sqlserver, docker, supabase, firebase, azure, aws.

## Referências

- `plugins/PLUGIN_POLICY.md`
- `plugins/PLUGIN_REGISTRY.md`
- `plugins/PLUGIN_LIFECYCLE.md`
- `workflows/plugin-mission.md`
- `plugins/PLUGIN_STATUS_POLICY.md`
- `plugins/MCP_READINESS_AUDIT.md`
- `infrastructure/registry/MCP_SERVER_CATALOG.md`
- `checklists/mcp-readiness.md`
