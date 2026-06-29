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
2. Priorizar arquivos executaveis de runtime antes de docs/migrations: seeders, bootstrap/startup, configuracao, policies, guards, navegacao, menus e services.
3. Rodar busca dirigida com `rg`, nunca varrer tudo sem filtro.
4. Quando o usuario trouxer evidencia visual ou arquivo/linha, iniciar pelo mesmo padrao e pelos arquivos equivalentes.
5. Classificar achados: secret, environment, domain, authorization, operational, presentation, test/demo.
6. Marcar falso positivo quando o valor for constante tecnica estavel, migration historica, documentacao sem efeito runtime ou fixture isolada.
7. Recomendar destino: banco, parametro, env/config, registry, feature flag, enum ou seed idempotente.
8. Priorizar por risco e impacto.
9. Registrar achados no Working Context.

## Padroes iniciais de busca

```powershell
rg -n "https?://|localhost|127\.0\.0\.1|password|secret|apiKey|token|connectionString" .
rg -n "role|permission|tenant|cliente|empresa|module|menu|status|AddRange|HasData|Seed|Guid\.Parse|new Guid" .
rg -n "\b\d{2,}\b|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}" .
```

O Orchestrator deve adaptar extensoes e pastas excluidas conforme stack (`bin/`, `obj/`, `node_modules/`, `dist/`, `.git/`, outputs gerados).

## Seeds, modulos e permissoes

Para pedidos sobre modulos, menus, departamentos, roles ou permissoes, o scan deve ter uma primeira passada obrigatoria em arquivos de seed/bootstrap e controle de acesso. Exemplo:

```powershell
rg -n "NewModule\(|AddRange|HasData|Ensure.*Module|Ensure.*Permission|RolePermission|UserPermission|portal\.|\.read|\.manage" backend frontend --glob "!**/Migrations/**" --glob "!**/node_modules/**"
rg -n "\"rh\"|\"legal\"|\"commercial\"|\"finance\"|\"operations\"|\"it\"|Jur[ií]dico|Comercial|Financeiro|Opera" backend frontend --glob "!**/Migrations/**"
```

Nao considerar o scan concluido enquanto achados em seeder/bootstrap nao forem classificados como real, falso positivo ou contrato estavel justificado.

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
