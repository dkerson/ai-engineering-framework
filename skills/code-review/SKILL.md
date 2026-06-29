---
name: code-review
description: >-
  Revisa código/PR por qualidade, lógica, testes e convenções.
---

# Code Review

## Objetivo

Garantir qualidade antes de merge — foco em issues reais.

## Quando usar

- PR review
- Auto-revisão pós-implementação
- Feedback de código

## Quando NÃO usar

- Implementação de features
- Diagnóstico de bugs

## Responsabilidades

1. Ler diff apenas (não projeto inteiro)
2. Verificar lógica, edge cases, security
3. Checar testes adequados
4. Classificar: Critical / Suggestion / Nice-to-have
5. Usar `checklists/review.md`
6. Checar hardcode funcional e recomendar fonte configuravel

## Entradas esperadas

- Diff/PR
- Contexto da mudança

## Saídas esperadas

- Feedback estruturado
- Aprovação ou lista de fixes

## Checklist

- [ ] Lógica correta
- [ ] Edge cases
- [ ] Testes adequados
- [ ] Convenções seguidas
- [ ] Sem secrets/debug code
- [ ] Sem hardcode proibido ou justificativa registrada

## Integração com outras skills

- **Upstream:** qa, skills técnicas
- **Downstream:** security-review (condicional)

## Exemplos

**Input:** PR com 3 files changed
**Output:** 1 Critical (SQL injection), 2 Suggestions.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `rules/clean-code.md`
- `rules/no-hardcode.md`
- `rules/solid.md`
- `checklists/review.md`
- `checklists/no-hardcode.md`
