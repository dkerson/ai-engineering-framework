# Natural Language Mission Engine (NLME)

> v2.12.0 — Camada de interpretação de linguagem natural acima do Strategic Intelligence Layer.

## Objetivo

Permitir que o usuário **converse naturalmente** sem construir prompts técnicos. O framework traduz objetivos de negócio em missões executáveis.

## Posição na arquitetura

```text
Usuário (linguagem natural)
        ↓
Natural Language Mission Engine (NLME)
        ↓
Strategic Intelligence Layer (SIL)
        ↓
Capability Operating System (COS)
        ↓
Master Orchestrator
        ↓
Domains → Skills → Implementação
```

## Componentes NLME

| Componente | Tipo | Função |
|------------|------|--------|
| Mission Translator | Skill | Traduz frase humana → Translation Brief |
| Goal Recognition | Mecanismo | Objetivo real vs texto literal |
| Mission Recognition | Mecanismo | Tipo de missão e domínios |
| Natural Commands | Catálogo | Verbos → tipos de missão |
| Mission Builder | Skill | Monta Mission Package |
| Prompt Builder | Skill | Structured Prompt interno |
| Mission Confidence | Mecanismo | Score antes de executar |
| Mission Catalog | Catálogo | Tipos oficiais de missão |
| Autonomous Planning | Política | Seleção automática de skills/workflows |

## Pipeline NLME

```text
1. mission-translator     → Translation Brief
2. goal-recognition       → Objetivo real
3. mission-builder        → Mission Package + Confidence
4. prompt-builder         → Structured Prompt (interno)
5. SIL                    → Mission Brief final
6. capability-resolver    → Capabilities COS
7. orchestrator           → Execução operacional
```

## Comportamento obrigatório

Antes de investigar ou implementar, o Orchestrator **responde primeiro** (via `templates/mission/nlme-first-response.md`):

1. Missão identificada
2. Objetivo (negócio)
3. Capabilities utilizadas
4. Domínios
5. Plano resumido
6. Roadmap resumido
7. Perguntas — **somente** se Mission Confidence < 60 e gap crítico

Caso contrário: **executar autonomamente**.

## Preservação

- Nenhuma skill removida
- SIL, COS, FOS, Orchestrator e domínios intactos
- Classificação legada do Orchestrator permanece válida
- Evolução incremental — NLME **antecede** SIL, não substitui

## Documentação

| Doc | Conteúdo |
|-----|----------|
| [Mission-Translator.md](Mission-Translator.md) | Skill tradutora |
| [Goal-Recognition.md](Goal-Recognition.md) | Objetivo real |
| [Prompt-Builder.md](Prompt-Builder.md) | Prompt estruturado interno |
| [Mission-Catalog.md](Mission-Catalog.md) | Catálogo de missões |
| [Natural-Commands.md](Natural-Commands.md) | Verbos naturais |
| [Autonomous-Planning.md](Autonomous-Planning.md) | Planejamento autônomo |
| [Mission-Confidence.md](Mission-Confidence.md) | Score de confiança |
| [Mission-Recognition.md](Mission-Recognition.md) | Reconhecimento (legado + NLME) |

## Referências

- `skills/mission-translator/SKILL.md`
- `skills/mission-builder/SKILL.md`
- `skills/prompt-builder/SKILL.md`
- `workflows/natural-language-mission.md`
- `rules/natural-language-mission-engine.md`
