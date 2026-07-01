# Evaluation Intelligence

| Campo | Valor |
|-------|-------|
| Status | Planned (operational baseline) |
| Lifecycle | Idea -> Planned |
| Dependencias | RAG Intelligence |

Avaliacao de LLM, RAG e agentes.

## Baseline operacional

O framework agora possui avaliacao leve pos-missao:

- regra: `rules/post-mission-evaluation.md`
- template: `templates/mission/post-mission-evaluation.md`
- integracao: Orchestrator avalia outcome, validacao, eficiencia e aprendizado reutilizavel antes da resposta final

Isto nao substitui uma suite completa de avaliacao automatizada. E um baseline governado pelo FOS para fechar o ciclo de aprendizado.

> Capability placeholder. Implementacao futura via Capability Template.

Ver `capabilities/CAPABILITY_REGISTRY.md`.
