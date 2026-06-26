# Capability Template

Copiar para nova capability via `capability-builder`.

## Estrutura

```text
capabilities/{id}/
├── README.md
├── ARCHITECTURE.md
├── FLOWS.md
├── EXAMPLES.md
├── SECURITY.md
├── BEST_PRACTICES.md
└── CHANGELOG.md
```

## Manifesto

| Campo | Valor |
|-------|-------|
| ID | {kebab-id} |
| Nome | {Nome Legível} |
| Versão | 0.1.0 |
| Categoria | {CAPABILITY_CATEGORIES} |
| Status | Idea |
| Health Score | — |

## Artefatos framework

- Skills em `skills/`
- Rules em `rules/{id}/`
- Templates em `templates/{id}/`
- Checklists em `checklists/{id}/`
- Workflows em `workflows/{id}/`
- Knowledge em `knowledge/{id}/` ou `knowledge/capabilities/{id}/`

## Registro COS

1. `registry/CAPABILITY_REGISTRY.md`
2. `roadmap/CAPABILITY_ROADMAP.md`
3. FOS IMPLEMENTED, CHANGELOG, DECISIONS (se Approved)
