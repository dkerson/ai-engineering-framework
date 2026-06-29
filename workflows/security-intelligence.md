# Workflow: Security Intelligence

> Arquitetura segura, autorizacao, permissoes, cache de acesso, threat modeling e governanca de SI.

## Trigger

`security-intelligence` - SI, seguranca estrutural, permissionamento, nivel de acesso, cache de permissao, RBAC, ABAC, multi-tenant, threat model, ataque, privilege escalation.

## Modo sugerido

| Condicao | Modo |
|----------|------|
| Revisao pontual de acesso | Review |
| Cache de permissao ou multi-tenant | Review |
| Mudanca arquitetural, authz em producao, dados sensiveis ou admin | Technical Council |

## Pipeline Review

```text
authorization-specialist*
-> permission-cache-reviewer*
-> threat-modeler*
-> security-review
-> risk-reviewer
-> validator
```

`*` O Orchestrator escolhe somente as skills necessarias.

## Pipeline Council

```text
security-architect
-> authorization-specialist
-> threat-modeler
-> risk-reviewer
-> decision-maker
-> implementation-planner
-> security-review
-> validator
```

## Skills

`security-architect`, `authorization-specialist`, `permission-cache-reviewer`, `threat-modeler`, `si-governance`, `security-review`, `risk-reviewer`, `validator`

## Rules

- `rules/security.md`
- `rules/security-access-control.md`
- `rules/permission-cache.md`
- `rules/threat-modeling.md`

## Checklists

- `checklists/security.md`
- `checklists/security-architecture.md`
- `checklists/authorization.md`
- `checklists/permission-cache.md`
- `checklists/threat-model.md`
