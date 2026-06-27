# Natural Language Mission Engine — Regras

## Posição

NLME é a **primeira camada** após o usuário. Preserva SIL, COS, FOS e Orchestrator.

## Regras absolutas

NLME (mission-translator, mission-builder, prompt-builder):

- **Nunca** implementam código
- **Nunca** alteram arquivos do projeto consumidor
- **Nunca** executam comandos no repositório
- **Nunca** expõem Structured Prompt ao usuário
- **Sempre** produzem artefatos para SIL e Orchestrator

## Bootstrap (ordem)

```text
NLME → SIL → COS → Orchestrator → Domains → Skills
```

## Toda interação não-trivial

1. Passa por NLME (salvo continuação de missão ativa)
2. Orchestrator apresenta `nlme-first-response` antes de investigar
3. Mission Confidence ≥ 60 → executar sem perguntas desnecessárias

## Preservação

- Classificação legada Orchestrator permanece
- Skills existentes intactas
- Workflows existentes intactos
- `legacy_demand_type` no Structured Prompt mantém compatibilidade

## Mission Memory

Ao encerrar missão, registrar via FOS:

- Objetivo · Decisões · Roadmap · Resultados · Aprendizados

Ver `docs/Missions.md` · `framework/operating-system/`

## Economia

- NLME não abre código — só registries e docs de missão
- Pipeline mínimo de skills
- Referências por link

## Referências

- `docs/Natural-Language-Missions.md`
- `workflows/natural-language-mission.md`
