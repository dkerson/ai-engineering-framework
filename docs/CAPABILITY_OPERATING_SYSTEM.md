# Capability Operating System

> v2.10.0 — núcleo de administração de todas as capabilities.

## Objetivo

Transformar o framework em plataforma **modular, escalável, reutilizável e auditável** — evolução por Capabilities, nunca por funcionalidades isoladas.

## COS vs FOS

| | FOS | COS |
|---|-----|-----|
| Escopo | Framework como um todo | Capabilities individuais |
| Registro | FRAMEWORK_STATUS, ROADMAP | CAPABILITY_REGISTRY, CAPABILITY_ROADMAP |
| Skills | framework-reviewer, etc. | capability-manager, builder, evaluator, discovery |

FOS e COS cooperam; toda mudança de capability atualiza FOS.

## Filosofia

```text
Capabilities
      ↓
Usuario (linguagem natural)
      ↓
Natural Language Mission Engine (NLME)
      ↓
Strategic Intelligence Layer  ← "Capability existe?"
      ↓
Capability Operating System (resolver)
      ↓
Master Orchestrator
      ↓
Domains → Skills → Projetos
```

## Framework Capability Mission

- Evolui **somente** o framework
- **Nunca** altera Umbra, Irisys, SmartRifa ou negócio
- Workflow: `workflows/capability-mission.md`

## Artefatos COS

| Artefato | Local |
|----------|-------|
| Registry | `capabilities/registry/CAPABILITY_REGISTRY.md` |
| Status | `capabilities/registry/CAPABILITY_STATUS.md` |
| Health | `capabilities/registry/CAPABILITY_HEALTH.md` |
| Report | `capabilities/registry/CAPABILITY_REPORT.md` |
| Roadmap | `capabilities/roadmap/CAPABILITY_ROADMAP.md` |
| Categories | `capabilities/CAPABILITY_CATEGORIES.md` |
| Lifecycle | `capabilities/CAPABILITY_LIFECYCLE.md` |
| Templates | `capabilities/templates/` |

## Referências

- `docs/CAPABILITY_ARCHITECTURE.md` (v2.9 — conceito)
- `docs/RAG_INTELLIGENCE.md`
- `plugins/PLUGIN_POLICY.md` (plugin → capability)
