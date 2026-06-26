---
name: changelog
description: >-
  Registro técnico de mudanças para desenvolvedores.
---

# ChangeLog

## Objetivo

Manter histórico técnico de alterações.

## Quando usar

- Feature concluída
- Após merge significativo

## Quando NÃO usar

- Release notes user-facing (release-notes)

## Responsabilidades

1. Listar commits/PRs relevantes
2. Formato Keep a Changelog
3. Linkar issues/PRs
4. Usar `templates/changelog.md`

## Entradas esperadas

- PRs, commits
- Implementação concluída

## Saídas esperadas

- Entrada de changelog

## Checklist

- [ ] Formato consistente
- [ ] Breaking changes section
- [ ] Links para PRs

## Integração com outras skills

- **Upstream:** code-review
- **Downstream:** release-notes

## Exemplos

**Input:** Feature OAuth
**Output:** "## [Unreleased] ### Added - Google OAuth login (#123)"


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `templates/changelog.md`
