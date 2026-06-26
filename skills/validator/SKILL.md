---
name: validator
description: >-
  Verifica se a entrega está pronta: testes, lint, build, typecheck, documentação e roteiro de teste. Invocado somente pelo Orchestrator nos modos Review e Technical Council.
---

# Validator

## Objetivo

Confirmar que a entrega atende critérios mínimos de qualidade antes do Orchestrator finalizar.

## Quando usar

- Modo **Review** (obrigatório)
- Modo **Technical Council** (obrigatório)
- Modo **Standard** quando QA solicitar validação técnica adicional
- Antes da resposta final ao usuário

## Quando NÃO usar

- Modo Fast
- Durante investigação (só após implementação)
- **Nunca** auto-iniciar

## Checklist obrigatório

Marcar cada item como `ok` | `n/a` | `pendente` | `falhou`:

- [ ] **Lint** — sem erros novos nos arquivos alterados
- [ ] **Typecheck** — quando aplicável (TS, C# strict)
- [ ] **Testes** — unitários/integração do módulo afetado
- [ ] **Build** — quando necessário (backend, mudança estrutural)
- [ ] **Roteiro de teste** — passos para validação manual
- [ ] **Riscos** — residuais identificados ou "nenhum"

## Responsabilidades

1. Ler Working Context (arquivos alterados, validações já feitas)
2. Executar **somente** validações necessárias — não repetir as da QA
3. Registrar resultado no Working Context
4. Emitir veredito: `pronto` | `pendente` | `bloqueado`

## Entradas esperadas

- Working Context com lista de arquivos alterados
- Resultados parciais de QA (se existirem)

## Saídas esperadas

- Checklist preenchido
- Veredito final
- Lista de pendências (se houver)

## Orquestração hierárquica

- **Invocação:** somente Orchestrator
- **Fala com usuário:** não — resultado vai para resposta final
- **Economia:** não rodar build completo se Standard e mudança pontual
- Detalhes: `rules/hierarchical-orchestration.md`

## Checklist da skill

- [ ] Checklist obrigatório completo
- [ ] Validações não duplicadas
- [ ] Veredito explícito

## Referências

- `rules/token-economy.md`
- `checklists/` (por tipo de tarefa)
- `templates/final-response.md`
