# Workflow: DevOps

> CI/CD, Docker, pipelines. Modo padrão: **Standard**. Review se alteração de infra produção.

## Trigger
`devops` — CI/CD, pipeline, Docker, deploy

## Modo sugerido

| Condição | Modo |
|----------|------|
| Ajuste de pipeline | Standard |
| Infra produção | Review |

## Pipeline (Standard)

```
Context Builder* → DevOps → QA → Entrega
```

## Pipeline (Review)

```
Context Builder → DevOps → Validator → Entrega
```

## Skills
`context-builder`, `devops`, `qa`, `validator`

## Checklist
- `checklists/deploy.md`

## Rules
- `rules/hierarchical-orchestration.md`
