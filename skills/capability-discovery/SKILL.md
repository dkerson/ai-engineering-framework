---
name: capability-discovery
description: >-
  Identifica oportunidades de novas Capabilities durante uso do framework. Apenas registra em backlog/COS — nunca implementa. Invocado pelo Orchestrator ou FOS Recommendation Engine.
---

# Capability Discovery

## Objetivo

Detectar gaps e registrar oportunidades — **registrar only**.

## Sinais

- Pedido repetido sem capability no Registry
- Nova tecnologia mencionada (OCR, voice, agents)
- Plugin proposto sem capability pai
- capability-evaluator conclui "nova Capability"

## Ações permitidas

1. Registrar Idea em `registry/CAPABILITY_REGISTRY.md` (status Idea)
2. Entrada em `planned/{id}.md`
3. Sugestão em `roadmap/CAPABILITY_ROADMAP.md`
4. FOS BACKLOG + RECOMMENDATIONS

## Proibido

- Implementar código ou docs completos
- Alterar projetos consumidores
- Promover status sem capability-manager + aprovação

## Referências

- `capabilities/CAPABILITY_LIFECYCLE.md`
- `framework/operating-system/BACKLOG.md`
