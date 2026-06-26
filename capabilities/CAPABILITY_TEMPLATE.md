# Capability Template

> Use com evolução incremental. Não implementar em projetos consumidores na fase de framework.

## Estrutura mínima

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

## Artefatos framework (por capability)

| Tipo | Local |
|------|-------|
| Skills | `skills/{nome}/SKILL.md` |
| Rules | `rules/{id}/` |
| Templates | `templates/{id}/` |
| Checklists | `checklists/{id}/` |
| Workflows | `workflows/{id}/` |
| Knowledge | `knowledge/{id}/` |

## Registro

1. Entrada em `CAPABILITY_REGISTRY.md`
2. FOS: IMPLEMENTED, CHANGELOG, FRAMEWORK_STATUS
3. Orchestrator + AGENTS.md se novo domínio

## Referências

- `capabilities/CAPABILITY_LIFECYCLE.md`
- `capabilities/rag/` — referência completa
