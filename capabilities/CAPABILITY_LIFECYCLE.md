# Capability Lifecycle — COS

> Toda transição atualiza FOS + COS registry.

## Ciclo de vida

```text
Idea
  ↓
Analysis
  ↓
Planned
  ↓
Approved
  ↓
In Development
  ↓
Ready
  ↓
Stable
  ↓
Deprecated
  ↓
Removed
```

| Estado | Descrição | Quem registra |
|--------|-----------|---------------|
| **Idea** | Oportunidade identificada | capability-discovery |
| **Analysis** | Impacto, esforço, dependências analisados | capability-evaluator |
| **Planned** | No roadmap COS | capability-manager |
| **Approved** | Usuário aprovou | FOS DECISIONS |
| **In Development** | Builder ativo | capability-builder |
| **Ready** | Documentado; uso em projetos permitido | capability-manager |
| **Stable** | Maduro; produção recomendada | capability-manager |
| **Deprecated** | Substituído | capability-manager |
| **Removed** | Histórico preservado | FOS |

## FOS — atualização obrigatória

- `FRAMEWORK_STATUS.md` · `FRAMEWORK_HEALTH.md` · `ROADMAP.md` · `BACKLOG.md`
- `IMPLEMENTED.md` · `LEARNING.md` · `RETROSPECTIVES.md` · `CHANGELOG.md`
- `VERSION` · `NEXT_STEPS.md` · `reports/RECOMMENDATIONS.md`
- `capabilities/registry/CAPABILITY_*`

## Referências

- `skills/capability-manager/SKILL.md`
- `docs/CAPABILITY_OPERATING_SYSTEM.md`
