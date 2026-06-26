---
name: deployment
description: >-
  Implantação: release, rollback, smoke tests, feature flags.
---

# Deployment

## Objetivo

Executar deploy seguro com validação pós-deploy.

## Quando usar

- Deploy produção/staging
- Rollback
- Release pipeline

## Quando NÃO usar

- Desenvolvimento local
- Code review

## Responsabilidades

1. Verificar checklist pre-deploy
2. Executar pipeline ou instruir passos
3. Smoke tests pós-deploy
4. Monitorar erros iniciais
5. Plano de rollback documentado

## Entradas esperadas

- Release notes
- Artefatos buildados

## Saídas esperadas

- Deploy concluído
- Smoke test results

## Checklist

- [ ] Pre-deploy checklist ok
- [ ] Deploy executado
- [ ] Smoke tests passando
- [ ] Rollback plan ready

## Integração com outras skills

- **Upstream:** qa, release-notes
- **Downstream:** support (monitoring)

## Exemplos

**Input:** Deploy v2.3
**Output:** Staging ok, prod deployed, smoke login OK.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `checklists/deploy.md`
- `workflows/deployment.md`
