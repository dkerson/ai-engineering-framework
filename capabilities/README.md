# Capability Operating System (COS)

> Caminho canônico: `.ai/capabilities/` · Framework v2.10.0+

## Objetivo

Administrar **todas** as capabilities do AI Engineering Framework. Nenhuma tecnologia nova entra diretamente em projetos — primeiro torna-se Capability; depois é consumida via Master Orchestrator.

## Filosofia — nova hierarquia

```text
Capabilities
      ↓
Strategic Intelligence Layer
      ↓
Master Orchestrator
      ↓
Domains
      ↓
Skills
      ↓
Projetos (consumidores)
```

## O que é uma Capability

Competência completa do framework. Pode conter:

Skills · Rules · Templates · Patterns · Workflows · Checklists · Knowledge · Plugins · MCPs · Infrastructure · Policies · Examples · Architecture · Learning · Metrics

## Estrutura COS

```text
capabilities/
├── README.md                    ← este arquivo (COS)
├── CAPABILITY_CATEGORIES.md
├── CAPABILITY_LIFECYCLE.md
├── CAPABILITY_REGISTRY.md       ← índice → registry/
├── registry/
│   ├── CAPABILITY_REGISTRY.md   ← registro canônico
│   ├── CAPABILITY_STATUS.md
│   ├── CAPABILITY_HEALTH.md
│   └── CAPABILITY_REPORT.md
├── roadmap/
│   └── CAPABILITY_ROADMAP.md
├── implemented/                 ← capabilities entregues
├── planned/                     ← capabilities planejadas
├── deprecated/
├── templates/                   ← templates COS
├── examples/
└── documentation/
    └── COS.md
```

## Componentes COS

| Componente | Skill | Papel |
|------------|-------|-------|
| **Capability Manager** | capability-manager | Criar, atualizar, versionar, documentar, registrar, planejar — **nunca implementar automaticamente** |
| **Capability Builder** | capability-builder | Criar novas capabilities no padrão |
| **Capability Evaluator** | capability-evaluator | Skill? Workflow? Plugin? Rule? Nova Capability? |
| **Capability Discovery** | capability-discovery | Identificar oportunidades; registrar; nunca implementar |
| **Capability Resolver** | capability-resolver | Selecionar capability na missão |

## Integrações

| Sistema | Integração |
|---------|------------|
| **FOS** | Toda mudança atualiza FRAMEWORK_STATUS, ROADMAP, IMPLEMENTED, etc. |
| **SIL** | Primeira pergunta: já existe Capability? |
| **Plugins** | Plugin sempre pertence a uma Capability |
| **Project Registry** | `PROJECT_CAPABILITIES.md` — não skills |

## Referências

- `docs/CAPABILITY_OPERATING_SYSTEM.md`
- `capabilities/registry/CAPABILITY_REGISTRY.md`
- `workflows/capability-mission.md`
