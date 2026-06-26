---
name: bug-hunter
description: >-
  Diagnóstico sistemático de bugs: reproduzir, isolar camada, localizar
  causa raiz com leitura mínima de arquivos. Usar em erros, falhas,
  comportamento inesperado, stack traces ou antes de implementar fix.
---

# Bug Hunter

## Objetivo

Encontrar causa raiz com investigação mínima e dirigida.

## Quando usar

- Qualquer bug ou erro
- Comportamento inesperado
- Antes de implementar fix

## Quando NÃO usar

- Feature nova
- Review de código

## Responsabilidades

1. Capturar erro/stack/logs
2. Reproduzir passos mínimos
3. Bisect: isolar camada (UI/API/DB)
4. Localizar arquivo+linha
5. Documentar causa raiz (`templates/root-cause-analysis.md` se complexo)

## Entradas esperadas

- Mensagem de erro
- Steps to reproduce
- Logs

## Saídas esperadas

- Causa raiz identificada
- Arquivo(s) afetado(s)
- Hipótese de fix

## Checklist

- [ ] Reproduzido
- [ ] Camada isolada
- [ ] Arquivo/linha localizados
- [ ] Causa raiz documentada
- [ ] Leitura mínima de arquivos

## Integração com outras skills

- **Upstream:** context-builder
- **Downstream:** tech-lead, backend, etc.

## Exemplos

**Input:** Erro 500 ao salvar pedido
**Output:** NullReference em OrderService.Save line 42 — CustomerId null.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `templates/bug-report.md`
- `templates/root-cause-analysis.md`
- `rules/token-economy.md`
