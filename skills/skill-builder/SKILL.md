---
name: skill-builder
description: >-
  Gera novas skills no padrão AI Engineering Framework: SKILL.md, exemplo,
  checklist, integração com orchestrator e documentação. Invocado pelo
  Orchestrator ou em tarefas de expansão do framework.
---

# Skill Builder

## Objetivo

Padronizar criação e registro de novas skills seguindo a arquitetura existente — **evolução incremental**, nunca recriar o que já funciona.

## Quando usar

- Nova skill necessária no framework ou projeto
- Skill existente desatualizada (atualizar, não substituir)
- Expansão do framework para nova stack ou domínio

## Quando NÃO usar

- Criar agent completo (usar `agent-creator`)
- Implementar código de produto

## Artefatos obrigatórios

Para cada nova skill, criar ou atualizar:

| Artefato | Local | Obrigatório |
|----------|-------|-------------|
| SKILL.md | `skills/<nome>/SKILL.md` | Sim |
| Seção Orquestração hierárquica | dentro do SKILL.md | Sim |
| Exemplo | `examples/<nome>.md` ou entrada em exemplo existente | Sim |
| Checklist | `checklists/<area>.md` (novo ou existente) | Se skill tem validação |
| Template | `templates/` ou `skills/_template/` | Se skill gera artefatos |
| Registro orchestrator | `workflows/_index.md` + `AGENTS.md` | Sim |
| Workflow | `workflows/<tipo>.md` | Se entra em pipeline |

## Responsabilidades

1. Definir `name` (kebab-case) e `description` (terceira pessoa + "Invocado pelo Orchestrator")
2. Copiar estrutura de `skills/_template/SKILL.md`
3. Preencher: Objetivo, Quando usar/NÃO usar, Responsabilidades, Entradas, Saídas, Checklist, Integração, Exemplos, Referências
4. Incluir **Orquestração hierárquica** (nunca auto-iniciar; Working Context; Council 150 palavras)
5. Registrar em `AGENTS.md` (tabela de skills) e `workflows/_index.md`
6. Criar exemplo concreto em `examples/`
7. Atualizar `CHANGELOG.md` (entrada MINOR) se skill é do framework core
8. Manter SKILL.md < 500 linhas

## Integração com Orchestrator

- Adicionar skill na tabela de classificação em `skills/orchestrator/SKILL.md` se novo tipo de demanda
- Ou referenciar em workflow existente no passo `[técnica]` / governança
- Não alterar algoritmo do orchestrator sem motivo

## Entradas esperadas

- Propósito e triggers da skill
- Modo(s) em que será usada (Fast/Standard/Review/Council)
- Skills upstream/downstream

## Saídas esperadas

- Skill completa e registrada
- Exemplo documentado
- Sem duplicação de responsabilidade com skill existente

## Checklist

- [ ] Frontmatter `name` + `description`
- [ ] Orquestração hierárquica presente
- [ ] < 500 linhas
- [ ] Registrado em AGENTS.md e workflows/_index.md
- [ ] Exemplo em examples/
- [ ] Sem sobreposição com critic/validator/qa/tech-lead

## Orquestração hierárquica

- **Invocação:** Orchestrator ou tarefa explícita de framework
- **Economia:** seguir `rules/token-economy.md`

## Referências

- Template: `skills/_template/SKILL.md`
- Arquitetura: `docs/ARCHITECTURE.md`
- Geracao incremental: usar `skills/_template/SKILL.md`; geradores em lote legados foram removidos
