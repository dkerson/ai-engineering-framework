---
name: task-analyst
description: >-
  Analisa tasks (ClickUp, suporte, backlog): extrai objetivo, escopo, dependências e domínios envolvidos. Invocado no início de fluxos híbridos ou quando há ticket/task anexada.
---

# Task Analyst

## Objetivo

Extrair de uma task ou ticket o que realmente precisa ser feito — objetivo, escopo, domínios e lacunas — antes de planejar execução.

## Quando usar

- Task ClickUp ou ticket de suporte anexado
- Pedido ambíguo referenciando card/tarefa
- Início de fluxo híbrido (banco + frontend, procedure + tela)
- "A task pede alteração em indicador..."

## Quando NÃO usar

- Pedido claro sem task → Orchestrator classifica direto
- Triagem pura de suporte → `support` (complementar)

## Responsabilidades

1. Ler task: título, descrição, anexos, comentários
2. Extrair objetivo, critérios implícitos e fora de escopo
3. Identificar domínios: dev, dados, BI, QA, suporte
4. Sinalizar informação faltante
5. Popular Working Context: objetivo da task
6. Recomendar hybrid-flow-planner se múltiplos domínios

## Diferença de skills existentes

- `support`: triagem e comunicação de ticket
- `product-owner`: valor e escopo de produto/feature
- **task-analyst**: leitura estruturada de task existente para execução técnica/híbrida

## Integração

- **Upstream:** orchestrator, support, context-builder
- **Downstream:** requirement-reviewer, business-rule-mapper, hybrid-flow-planner

## Referências

- `workflows/hybrid-flows.md`
- `examples/data/hybrid-task-database-frontend.md`
