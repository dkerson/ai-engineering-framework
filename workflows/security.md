# Workflow: Seguranca

> Analise e correcao de vulnerabilidades. Modo padrao: **Review**. Council se auth/autorizacao em producao, arquitetura sensivel ou risco de SI alto.

## Trigger

`security` - vulnerabilidade, auth, OWASP, permissao, nivel de acesso, SI, ataque, cache de permissao.

## Modo sugerido

| Condicao | Modo |
|----------|------|
| Revisao pontual | Review |
| Auth, autorizacao, producao | **Technical Council** |
| Cache de permissao, multi-tenant, SI ou threat model | Review/**Technical Council** |

## Pipeline (Review)

```text
Security Review -> [Security Intelligence especialista*] -> Risk Reviewer -> [fix] -> Critic -> Validator -> Entrega
```

`*` O Orchestrator escolhe somente especialistas necessarios.

## Pipeline (Council)

```text
Conselho (security-architect, authorization-specialist, threat-modeler, security-review, software-architect, backend)
-> Decision Maker
-> Implementation Planner
-> [fix]
-> Validator
-> Entrega
```

## Skills

`security-review`, `security-architect`, `authorization-specialist`, `permission-cache-reviewer`, `threat-modeler`, `si-governance`, `risk-reviewer`, `critic`, `validator`, `backend`

## Checklist

- `checklists/security.md`
- `checklists/security-architecture.md`
- `checklists/authorization.md`
- `checklists/permission-cache.md`
- `checklists/threat-model.md`
- `checklists/review.md`

## Rules

- `rules/hierarchical-orchestration.md`
- `rules/security.md`
- `rules/security-access-control.md`
- `rules/permission-cache.md`
- `rules/threat-modeling.md`

## Ver tambem

- `workflows/security-intelligence.md`
- `docs/SECURITY_INTELLIGENCE.md`
