---
name: qa
description: >-
  Estratégia de testes, casos de teste, validação manual/automática.
---

# QA

## Objetivo

Garantir qualidade via testes direcionados — não suíte completa desnecessária.

## Quando usar

- Após implementação
- Validação de fix
- Plano de testes para feature

## Quando NÃO usar

- Implementação de código (skills técnicas)
- Review de código puro

## Responsabilidades

1. Derivar casos do functional spec / bug report
2. Executar testes relacionados apenas
3. Verificar edge cases críticos
4. Documentar `templates/test-plan.md` se feature grande
5. Reportar falhas ao tech-lead
6. Validar Boundary Map quando a mudança tocar arquivos compartilhados
7. Para frontend, confirmar runtime correto antes de aceitar evidencia visual
8. Validar fonte de configuracao quando hardcode foi removido ou aceito

## Entradas esperadas

- Implementação concluída
- Critérios de aceite

## Saídas esperadas

- Resultado de testes
- Casos adicionais se gaps

## Checklist

- [ ] Happy path validado
- [ ] Edge cases críticos
- [ ] Regressão mínima ok
- [ ] Testes relacionados executados
- [ ] Boundary Map revisado quando aplicável
- [ ] Rotas/testes canário executados quando arquivo compartilhado mudou
- [ ] Frontend validado em URL/porta corretas quando aplicável
- [ ] Fonte configuravel/fallback validado quando houve anti-hardcode

## Integração com outras skills

- **Upstream:** backend, react, flutter, api
- **Downstream:** code-review

## Exemplos

**Input:** Fix validação email
**Output:** 3 casos: válido, inválido, vazio — todos passando.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `rules/testing.md`
- `rules/regression-boundary.md`
- `rules/frontend-runtime-validation.md`
- `rules/no-hardcode.md`
- `checklists/feature.md`
- `checklists/frontend-regression.md`
- `checklists/no-hardcode.md`
- `templates/test-plan.md`
