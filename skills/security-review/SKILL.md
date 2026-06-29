---
name: security-review
description: >-
  Analise de seguranca: OWASP, auth, secrets, injection, dependencias e findings. Invocado pelo Orchestrator para revisao geral de seguranca; delega arquitetura segura, autorizacao profunda, cache de permissoes, threat modeling e governanca de SI as skills especializadas de Security Intelligence.
---

# Security Review

## Objetivo

Identificar vulnerabilidades antes de merge/deploy.

## Quando usar

- Auth, pagamentos, PII ou dados sensiveis.
- Apos code-review em area sensivel.
- Solicitacao explicita de seguranca.
- Revisao geral antes ou depois de especialistas de Security Intelligence.

## Quando NAO usar

- UI cosmetica.
- Docs sem codigo.
- Arquitetura segura profunda: usar `security-architect`.
- Autorizacao profunda: usar `authorization-specialist`.

## Responsabilidades

1. Aplicar OWASP Top 10 checklist.
2. Revisar auth/authz flows em nivel geral.
3. Revisar input validation e injection.
4. Procurar secrets expostos.
5. Usar `checklists/security.md`.
6. Sinalizar ao Orchestrator quando a missao exigir `security-architect`, `authorization-specialist`, `permission-cache-reviewer`, `threat-modeler` ou `si-governance`.

## Entradas esperadas

- Code diff.
- Architecture de auth, quando existir.
- Working Context.

## Saidas esperadas

- Security findings.
- Severity classification.
- Especialista adicional recomendado, quando necessario.

## Checklist

- [ ] Injection checked
- [ ] Auth/authz valid
- [ ] Secrets not exposed
- [ ] HTTPS/TLS
- [ ] Dependencies scanned
- [ ] Security Intelligence escalation checked

## Integracao com outras skills

- **Upstream:** code-review, security-architect*, authorization-specialist*, permission-cache-reviewer*, threat-modeler*
- **Downstream:** backend (fixes), risk-reviewer, validator

## Orquestracao hierarquica

- **Unico contato com usuario:** Orchestrator.
- **Invocacao:** somente quando o Orchestrator incluir no pipeline.
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados.
- **Modo Council:** max. 150 palavras.
- **Economia:** seguir `rules/token-economy.md`.

## Referencias

- `docs/SECURITY_INTELLIGENCE.md`
- `rules/security.md`
- `rules/security-access-control.md`
- `rules/permission-cache.md`
- `rules/threat-modeling.md`
- `checklists/security.md`
