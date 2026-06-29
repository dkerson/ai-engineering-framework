# Threat Modeling

> Regras para mapear ameacas antes de implementar ou revisar mudancas sensiveis.

## Escopo minimo

Identificar:

- Assets protegidos.
- Atores internos, externos e service accounts.
- Trust boundaries.
- Entradas externas.
- Acoes privilegiadas.
- Dados sensiveis.
- Dependencias e integracoes.

## Vetores obrigatorios

- Injection.
- Broken authentication.
- Broken authorization.
- Privilege escalation.
- Cross-tenant data leakage.
- Replay.
- Enumeration.
- Session hijack.
- Prompt injection quando houver IA/RAG.
- Supply chain/dependency risk.
- Logging of secrets or PII.

## Saida esperada

```markdown
### Threat Model
- Assets:
- Actors:
- Trust boundaries:
- Abuse cases:
- Attack paths:
- Mitigations:
- Residual risk:
```
