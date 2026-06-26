---
name: context-builder
description: >-
  Monta contexto mínimo do projeto lendo AGENTS.md, context/ e estrutura de pastas. Usar quando o projeto é desconhecido ou o escopo precisa de mapeamento inicial.
---

# Context Builder

## Objetivo

Fornecer contexto suficiente para execução sem leitura excessiva de arquivos.

## Quando usar

- Projeto novo ou desconhecido
- Início de bug/feature sem contexto claro
- Orchestrator solicita contexto

## Quando NÃO usar

- Contexto já carregado na sessão
- Tarefa pontual em arquivo único conhecido

## Responsabilidades

1. Ler AGENTS.md do projeto
2. Ler `context/` do projeto ou Personal-AI
3. Mapear estrutura (pastas principais, stack)
4. Identificar área afetada pelo pedido
5. Resumir em bullets (máx. 10)
6. **Popular Working Context** com stack, área e arquivos candidatos

## Entradas esperadas

- Pedido do usuário
- AGENTS.md do repo
- `Personal-AI/context/*`

## Saídas esperadas

- Resumo de contexto (stack, arquitetura, área)
- Lista de arquivos candidatos a investigação

## Checklist

- [ ] AGENTS.md lido
- [ ] Stack identificada
- [ ] Área afetada mapeada
- [ ] Resumo conciso produzido

## Integração com outras skills

- **Upstream:** orchestrator
- **Downstream:** bug-hunter, tech-lead, software-architect

## Exemplos

**Input:** Bug em API desconhecida
**Output:** "Monorepo .NET 8 + Angular 19. Erro em Umbra.Api/Controllers/OrdersController."


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `rules/token-economy.md`
- `context/architecture.md`
