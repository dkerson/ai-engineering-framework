# Workflow: Segurança

> Análise e correção de vulnerabilidades. Modo padrão: **Review**. Council se auth/autorização em produção.

## Trigger
`security` — vulnerabilidade, auth, OWASP

## Modo sugerido

| Condição | Modo |
|----------|------|
| Revisão pontual | Review |
| Auth, autorização, produção | **Technical Council** |

## Pipeline (Review)

```
Security Review → Risk Reviewer → [fix] → Critic → Validator → Entrega
```

## Pipeline (Council)

```
Conselho (security-review, software-architect, backend) → Decision Maker
    → Implementation Planner → [fix] → Validator → Entrega
```

## Skills
`security-review`, `risk-reviewer`, `critic`, `validator`, `backend`

## Checklist
- `checklists/security.md`
- `checklists/review.md`

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/security.md`
