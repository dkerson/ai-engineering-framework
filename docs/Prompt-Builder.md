# Prompt Builder

> Skill NLME — transformação interna de Mission Package em Prompt Estruturado.

## Visibilidade

O usuário **nunca** vê o Structured Prompt. É artefato interno entre NLME → SIL → Orchestrator.

## Prompt Intelligence

Todo Structured Prompt contém automaticamente:

| Campo | Origem |
|-------|--------|
| Objetivo | Goal Recognition + Mission Builder |
| Escopo | Mission Builder (in/out) |
| Domínios | Mission Recognition |
| Capabilities | COS resolver |
| Skills | Autonomous Planning |
| Plugins | integration-resolver / plugin-resolver |
| Restrições | AGENTS projeto + rules |
| Segurança | Risk preliminar + mcp-security |
| Critérios de sucesso | Mission type + workflow |
| Plano | Mission Builder steps |
| Roadmap | Mission Builder fases |

## Template

`templates/mission/structured-prompt.md`

## Fluxo

```text
Mission Package
    → prompt-builder
    → Structured Prompt (Working Context)
    → SIL (refina → Mission Brief)
    → orchestrator (classifica + executa)
```

## Compatibilidade legada

O Structured Prompt inclui campo `legacy_demand_type` mapeado para tabela do Orchestrator (`bug`, `feature`, `product-excellence`, etc.) — **interfaces públicas preservadas**.

## Skill

`skills/prompt-builder/SKILL.md`
