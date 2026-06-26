# Workflow: Framework Capability Mission

> Evoluir **somente** o AI Engineering Framework. **Nunca** alterar projetos consumidores ou funcionalidades de negócio.

## Trigger

Quais capabilities, evolução do framework, suporta RAG/OCR, deveria virar capability, próxima capability, capability report.

## Pipeline

```text
Framework Capability Mission
→ capability-resolver (capability existe?)
→ capability-evaluator* (skill vs workflow vs plugin vs capability?)
→ capability-discovery* (registrar Idea)
→ capability-builder* (se Approved)
→ capability-manager (registry, status, health, report)
→ FOS Update
```

`*` Quando necessário.

## Modo

| Cenário | Modo |
|---------|------|
| Consultar registry, report | Fast |
| Avaliar nova extensão | Standard |
| Criar capability | Standard → Review |
| Promover Stable | Review |

## Skills

capability-manager, capability-resolver, capability-evaluator, capability-discovery, capability-builder, validator

## Regras

- Zero implementação em Umbra, Irisys, SmartRifa
- Toda mudança de status → FOS + COS registry
- Plugin exige capability pai

## Referências

- `docs/CAPABILITY_OPERATING_SYSTEM.md`
- `capabilities/registry/CAPABILITY_REPORT.md`
