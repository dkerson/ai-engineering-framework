# Workflow: Hardcode Audit

> Auditoria de hardcode funcional, operacional, ambiente, autorizacao e configuracao. Modo padrao: Standard. Review se envolver auth, multi-tenant, banco, producao ou refactor amplo.

## Trigger

`hardcode` · `valor fixo` · `parametrizar` · `configuracao` · `scan hardcode` · `modulos/permissoes fixos` · `magic numbers`

## Pipeline

```text
Orchestrator
  -> hardcode-scanner
  -> risk-reviewer*
  -> implementation-planner*
  -> [backend/api/database/react]*
  -> qa/code-review
```

\* Condicional conforme escopo.

## Passos

1. Definir escopo do scan: diff, pasta, modulo ou projeto.
2. Excluir outputs gerados e dependencias (`bin`, `obj`, `node_modules`, `dist`, `.git`).
3. Rodar busca dirigida com `rg`.
4. Classificar achados reais e falsos positivos.
5. Recomendar destino de configuracao.
6. Se aprovado, corrigir por menor diff seguro.
7. Validar regressao e fonte de configuracao.

## Destinos recomendados

| Achado | Destino |
|--------|---------|
| Secret/connection string | env/vault/secret manager |
| URL/host/provider | env/config/registry |
| Modulo/menu/status | banco/config/enum justificado |
| Permissao/role/scope | policy/matriz/banco |
| Threshold/prazo/limite | parametro/config/feature flag |
| Seed de produto | upsert idempotente |

## Guardrails

- Nao corrigir todos os achados automaticamente sem priorizacao.
- Nao transformar contrato estavel em configuracao desnecessaria.
- Nao mover secret real para outro arquivo versionado.
- Nao alterar dados de producao sem aprovacao explicita.
- Para permissao/modulo/menu, validar canarios de acesso e rotas relacionadas.

## Checklists

- `checklists/no-hardcode.md`
- `checklists/review.md`
- `checklists/frontend-regression.md` quando UI/menu/rota forem afetados

## Rules

- `rules/no-hardcode.md`
- `rules/token-economy.md`
- `rules/regression-boundary.md`
- `rules/security.md`
