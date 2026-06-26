---
name: security-review
description: >-
  Análise de segurança: OWASP, auth, secrets, injection.
---

# Security Review

## Objetivo

Identificar vulnerabilidades antes de merge/deploy.

## Quando usar

- Auth/pagamentos/PII
- Após code-review em área sensível
- Solicitação explícita

## Quando NÃO usar

- UI cosmética
- Docs sem código

## Responsabilidades

1. OWASP Top 10 checklist
2. Auth/authz flows
3. Input validation, injection
4. Secrets scan
5. Usar `checklists/security.md`

## Entradas esperadas

- Code diff
- Architecture de auth

## Saídas esperadas

- Security findings
- Severity classification

## Checklist

- [ ] Injection checked
- [ ] Auth/authz valid
- [ ] Secrets not exposed
- [ ] HTTPS/TLS
- [ ] Dependencies scanned

## Integração com outras skills

- **Upstream:** code-review
- **Downstream:** backend (fixes)

## Exemplos

**Input:** PR login endpoint
**Output:** Medium — rate limiting missing.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `rules/security.md`
- `checklists/security.md`
