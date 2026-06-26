---
name: devops
description: >-
  CI/CD, Docker, infra, monitoring, IaC.
---

# DevOps

## Objetivo

Automatizar build, deploy e observabilidade.

## Quando usar

- Pipeline CI/CD
- Docker/K8s
- Monitoring/alerting
- Infra changes

## Quando NÃO usar

- Código applicativo
- UX design

## Responsabilidades

1. Analisar pipeline existente
2. Alteração mínima no CI/CD
3. Secrets via vault/env — nunca commit
4. Health checks e monitoring
5. Documentar runbook

## Entradas esperadas

- Repo structure
- Deploy requirements

## Saídas esperadas

- Pipeline config
- Runbook updates

## Checklist

- [ ] Pipeline verde
- [ ] Secrets seguros
- [ ] Health checks
- [ ] Rollback testado

## Integração com outras skills

- **Upstream:** performance, deployment
- **Downstream:** deployment, qa

## Exemplos

**Input:** Build lento 15min
**Output:** Cache npm/dotnet — 4min.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `checklists/deploy.md`
- `rules/security.md`
