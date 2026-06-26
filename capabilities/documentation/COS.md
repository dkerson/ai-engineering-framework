# Capability Operating System (COS)

> Núcleo de administração de capabilities · v2.10.0

## Missão

Toda tecnologia, arquitetura, integração e inteligência **nasce como Capability** antes de ser usada em projetos.

## Hierarquia

```text
Capabilities → SIL → Orchestrator → Domains → Skills → Projetos
```

## Componentes

| Componente | Skill |
|------------|-------|
| Manager | capability-manager |
| Builder | capability-builder |
| Evaluator | capability-evaluator |
| Discovery | capability-discovery |
| Resolver | capability-resolver |

## Capability Intelligence (SIL)

Antes de planejar missão:

1. **Já existe Capability?** → capability-resolver
2. **Se não** → capability-evaluator: nova Capability?
3. **Se sim** → capability-discovery registra Idea; **nunca implementa sem aprovação**

## Plugin rule

> Plugin nunca existe sem Capability responsável.

## Project Registry

Projetos declaram `PROJECT_CAPABILITIES.md` — não skills.

## Referências

- `capabilities/README.md`
- `capabilities/registry/CAPABILITY_REPORT.md`
