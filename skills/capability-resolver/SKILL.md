---
name: capability-resolver
description: >-
  Identifica capability necessária na missão e verifica readiness. Invocado somente pelo Orchestrator antes de tecnologias RAG, OCR, voice, etc.
---

# Capability Resolver

## Objetivo

Mapear demanda → capability correta via `capabilities/registry/CAPABILITY_REGISTRY.md`.

## Quando usar

- Assistente inteligente, RAG, FAQ, busca semântica
- Tecnologia que deve ser capability-first (nunca direto no projeto)

## Algoritmo

```
1. Extrair sinais (RAG, OCR, voice, agent, eval)
2. Consultar CAPABILITY_REGISTRY
3. SE status < Ready → documentar/planejar; bloquear impl em produto
4. SE Ready → encaminhar sub-orquestrador (ex.: rag-orchestrator)
5. Retornar capability_id, skills sugeridas, readiness
```

## Referências

- `capabilities/registry/CAPABILITY_REGISTRY.md`
- `docs/CAPABILITY_ARCHITECTURE.md`
