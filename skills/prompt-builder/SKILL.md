---
name: prompt-builder
description: >-
  Transforma Mission Package em Prompt Estruturado interno para Master Orchestrator. O usuário nunca vê este artefato. Invocado pelo Orchestrator via NLME após Mission Builder.
---

# Prompt Builder

## Objetivo

Materializar **Prompt Intelligence** — prompt estruturado completo que o Master Orchestrator consome sem exigir prompt técnico do usuário.

## Quando usar

- Após mission-builder em fluxo NLME
- Antes de SIL enriquecer ou validar Mission Brief

## Quando NÃO usar

- Exibir prompt ao usuário (proibido)
- Substituir Orchestrator na execução
- **Nunca** auto-iniciar

## Responsabilidades

1. Preencher **Structured Prompt** → `templates/mission/structured-prompt.md`
2. Incluir: objetivo, escopo, domínios, capabilities, skills, restrições, segurança, critérios de sucesso, plano, roadmap
3. Herdar **Prompt Intelligence** de Mission Package + overlays do projeto consumidor
4. Entregar ao SIL para refinamento estratégico (Mission Brief final)
5. Garantir compatibilidade com classificação legada do Orchestrator

## Orquestração hierárquica

- **Upstream:** mission-builder
- **Downstream:** SIL (Mission Brief) → orchestrator
- **Segurança:** respeitar `rules/mcp-security.md`, sem credenciais
- **Economia:** prompt conciso; referências por link, não cópia de docs

## Saídas esperadas

**Structured Prompt** (interno — Working Context):

| Seção | Conteúdo |
|-------|----------|
| Objective | Objetivo de negócio |
| Scope | In/out explícito |
| Project | Registry + context overlay |
| Domains | Lista ordenada |
| Capabilities | IDs COS |
| Skills | Pipeline ordenado |
| Plugins | Se infra/MCP |
| Constraints | Umbra rules, identidade visual, etc. |
| Security | Auth, dados, produção |
| Success criteria | Testável |
| Plan | Passos numerados |
| Roadmap | Fases |
| Operational mode | Fast/Standard/Review/Council |

## Checklist

- [ ] Todas as seções Prompt Intelligence preenchidas ou N/A
- [ ] Usuário não exposto ao artefato
- [ ] SIL recebe Structured Prompt + Mission Package

## Referências

- `docs/Prompt-Builder.md`
- `templates/mission/structured-prompt.md`
- `templates/mission/mission-brief.md`
- `rules/strategic-intelligence-layer.md`
