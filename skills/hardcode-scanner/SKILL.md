---
name: hardcode-scanner
description: >-
  Identifica hardcode funcional, operacional, de ambiente, autorizacao e configuracao em projetos consumidores. Usa scans dirigidos com rg, classifica achados e sugere destino: banco, parametro, config, env, feature flag, enum ou seed idempotente.
---

# Hardcode Scanner

## Objetivo

Encontrar valores fixos que dificultam manutencao, multi-tenant, configuracao por cliente, evolucao de permissao ou mudanca de regra.

## Quando usar

- Auditoria de projeto por hardcode
- Review de PR com seeds, permissoes, modulos, menus, status ou parametros
- Antes de implementar feature que envolve configuracao
- Bugs causados por valor fixo, tenant errado, URL fixa ou permissao hardcoded

## Quando NAO usar

- Secrets scan profundo de seguranca (usar security-review tambem)
- Leitura completa do projeto sem escopo
- Refactor automatico sem aprovacao do usuario

## Responsabilidades

1. Definir escopo do scan: projeto, modulo, pasta ou diff.
2. Rodar busca dirigida com `rg`, nunca varrer tudo sem filtro.
3. Classificar achados: secret, environment, domain, authorization, operational, presentation, test/demo.
4. Marcar falso positivo quando o valor for constante tecnica estavel ou fixture isolada.
5. Recomendar destino: banco, parametro, env/config, registry, feature flag, enum ou seed idempotente.
6. Priorizar por risco e impacto.
7. Registrar achados no Working Context.

## Padroes iniciais de busca

```powershell
rg -n "https?://|localhost|127\.0\.0\.1|password|secret|apiKey|token|connectionString" .
rg -n "role|permission|tenant|cliente|empresa|module|menu|status|AddRange|HasData|Seed|Guid\.Parse|new Guid" .
rg -n "\b\d{2,}\b|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}" .
```

O Orchestrator deve adaptar extensoes e pastas excluidas conforme stack (`bin/`, `obj/`, `node_modules/`, `dist/`, `.git/`, outputs gerados).

## Saida esperada

```markdown
## Hardcode Scan
- Scope:
- Files scanned:
- Findings:
  - file:line
  - category:
  - evidence:
  - risk:
  - recommended destination:
  - suggested fix:
- False positives:
- Next actions:
```

## Criterios de risco

| Risco | Sinal |
|-------|-------|
| Alto | secret, tenant/cliente fixo, permissao/role hardcoded, URL prod fixa, regra comercial variavel |
| Medio | modulo/menu/status/threshold/prazo fixo, seed nao idempotente |
| Baixo | constante nomeada, fixture, mock, default local bem isolado |

## Integracao

- **Upstream:** orchestrator, code-review, backend, api, react, security-review
- **Downstream:** implementation-planner, backend, database, authorization-specialist, qa

## Referencias

- `rules/no-hardcode.md`
- `checklists/no-hardcode.md`
- `rules/security.md`
- `rules/infrastructure-secrets.md`
- `rules/regression-boundary.md`
