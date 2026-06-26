---
name: release-notes
description: >-
  Produz notas de release para usuários/stakeholders.
---

# Release Notes

## Objetivo

Comunicar mudanças de forma clara para release.

## Quando usar

- Bug fix em release
- Feature pronta para deploy
- Comunicação pós-deploy

## Quando NÃO usar

- Changelog técnico (usar changelog)
- Durante desenvolvimento

## Responsabilidades

1. Listar mudanças user-facing
2. Agrupar: Added/Fixed/Changed/Removed
3. Linguagem não-técnica para usuários
4. Usar `templates/release-notes.md`

## Entradas esperadas

- Changelog
- PRs merged

## Saídas esperadas

- Release notes document

## Checklist

- [ ] User-facing only
- [ ] Agrupado por tipo
- [ ] Sem jargão técnico excessivo
- [ ] Breaking changes destacados

## Integração com outras skills

- **Upstream:** qa, code-review
- **Downstream:** deployment

## Exemplos

**Input:** Release v2.3
**Output:** "Added: Login Google. Fixed: erro ao salvar pedido."


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `templates/release-notes.md`
- `checklists/release.md`
