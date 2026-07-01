# Memory Intelligence

| Campo | Valor |
|-------|-------|
| Status | Planned (operational baseline) |
| Lifecycle | Idea -> Planned |
| Dependencias | RAG Intelligence |

Memoria de longo prazo para agentes.

## Baseline operacional

O framework agora possui uma memoria leve de execucao:

- regra: `rules/execution-memory.md`
- indice: `framework/operating-system/EXECUTION_MEMORY_INDEX.md`
- integracao: Orchestrator consulta aprendizados antes de tasks nao triviais

Isto nao substitui a capability completa de memoria de longo prazo. E um baseline governado pelo FOS para evitar repetir erros e leituras desnecessarias.

> Capability placeholder. Implementacao futura via Capability Template.

Ver `capabilities/CAPABILITY_REGISTRY.md`.
