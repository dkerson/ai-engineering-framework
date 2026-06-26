# Workflow: Code Review

> Revisão de PR/código. Modo padrão: **Fast** (só review) ou **Standard** (com security).

## Trigger
`review` — revisar PR, code review, feedback de código

## Modo sugerido

| Condição | Modo |
|----------|------|
| Review simples | **Fast** |
| Auth, PII, endpoints públicos | Standard |

## Pipeline (Fast)

```
Code Review → Entrega
```

## Pipeline (Standard)

```
Code Review → Security Review → Entrega
```

## Passos

| # | Skill | Ação |
|---|-------|------|
| 1 | code-review | Qualidade, lógica, testes, convenções |
| 2 | security-review | OWASP, secrets, injection (se aplicável) |

## Checklists
- `checklists/review.md`
- `checklists/security.md` (condicional)

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/clean-code.md`
