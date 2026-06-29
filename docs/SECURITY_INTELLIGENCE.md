# Security Intelligence

> Dominio para arquitetura segura, autorizacao, permissoes, cache de acesso, modelagem de ameacas e governanca de SI.

## Objetivo

Separar revisao generica de seguranca de decisoes estruturais de acesso e protecao. `security-review` continua sendo o revisor geral; Security Intelligence adiciona especialistas para riscos que exigem profundidade.

## Quando acionar

- Auth, autorizacao, RBAC, ABAC, multi-tenant ou escopos.
- Cache de permissao, sessao, claims, token introspection ou memoria local.
- Nivel de acesso por usuario, tenant, plano, cargo, feature flag ou ambiente.
- Superficie de ataque, privilege escalation, injection, replay, enumeration ou lateral movement.
- Politicas de SI: secrets, auditoria, logs, MFA, segregacao de funcoes e dados sensiveis.
- Mudancas em arquitetura que alteram trust boundaries.

## Skills

| Skill | Papel |
|-------|-------|
| `security-architect` | Define trust boundaries, zonas, padroes seguros e trade-offs de arquitetura. |
| `authorization-specialist` | Modela RBAC/ABAC, roles, scopes, tenants e matriz de permissoes. |
| `permission-cache-reviewer` | Revisa cache de permissao, TTL, invalidacao, fail-closed e stale access. |
| `threat-modeler` | Mapeia ameacas, abuso, vetores de ataque e mitigacoes. |
| `si-governance` | Define controles de SI, auditoria, segregacao, secrets e politicas operacionais. |

## Relacao com skills existentes

- `security-review`: checklist geral, findings e severidade.
- `risk-reviewer`: risco, impacto, probabilidade e rollback.
- `software-architect`: arquitetura geral; usa `security-architect` quando seguranca muda o desenho.
- `plugin-resolver`: permissao de plugins e `access_mode`.
- `permission-aware-retrieval`: permissionamento especifico de RAG.
- `prompt-injection-reviewer`: ataques de prompt/RAG.

## Menor pipeline seguro

| Cenario | Pipeline |
|---------|----------|
| Revisao simples OWASP | `security-review -> risk-reviewer -> validator` |
| RBAC/ABAC ou multi-tenant | `authorization-specialist -> security-review -> validator` |
| Cache de permissao | `permission-cache-reviewer -> authorization-specialist -> security-review -> validator` |
| Mudanca arquitetural sensivel | Technical Council com `security-architect`, `authorization-specialist`, `threat-modeler`, `risk-reviewer` |
| Politica de SI | `si-governance -> security-review -> validator` |

## Regras essenciais

- Permissao deve ser avaliada antes da acao protegida, nunca apenas na UI.
- Cache de permissao deve falhar fechado (`deny`) quando houver duvida.
- Toda decisao de acesso sensivel precisa de fonte autoritativa, versao ou invalidacao.
- Mudanca de role, tenant, plano, status, sessao ou feature flag deve invalidar acesso derivado.
- Logs de auditoria devem registrar decisao relevante sem expor secrets ou PII desnecessaria.
- Acoes destrutivas exigem revalidacao server-side e, quando aplicavel, confirmacao explicita.

## Saida esperada no Working Context

```markdown
### Security Intelligence
- Security scope:
- Trust boundaries:
- Access model:
- Permission cache:
- Threats:
- Required controls:
- Validation:
- Residual risk:
```
