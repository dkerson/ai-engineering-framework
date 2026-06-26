---
name: capability-builder
description: >-
  Cria novas Capabilities no padrão COS: arquitetura, skills, rules, templates, checklists, knowledge, workflows, docs, roadmap e registro. Invocado somente após aprovação via Capability Mission.
---

# Capability Builder

## Objetivo

Gerar pacotes de capability completos — **framework-only**.

## Sempre gerar

| Artefato | Local |
|----------|-------|
| Arquitetura | `capabilities/{id}/ARCHITECTURE.md` |
| Skills | `skills/` (via skill-builder quando necessário) |
| Rules | `rules/{id}/` |
| Templates | `templates/{id}/`, `capabilities/templates/` |
| Checklists | `checklists/{id}/` |
| Examples | `capabilities/{id}/EXAMPLES.md` |
| Knowledge | `knowledge/capabilities/{id}/` |
| Workflows | `workflows/{id}/` |
| Documentação | README, FLOWS, SECURITY, BEST_PRACTICES |
| Roadmap | entrada em `roadmap/CAPABILITY_ROADMAP.md` |
| Registro | `registry/CAPABILITY_REGISTRY.md` |

## Processo

```
1. Copiar capabilities/templates/capability-template.md
2. Preencher manifesto (categoria, dependências)
3. Gerar artefatos mínimos
4. capability-manager valida
5. FOS: IMPLEMENTED, CHANGELOG (após aprovação)
```

## Quando NÃO usar

- Implementar em projeto consumidor
- Auto-executar sem Approved no lifecycle

## Referências

- `capabilities/templates/capability-template.md`
- `skills/skill-builder/SKILL.md`
