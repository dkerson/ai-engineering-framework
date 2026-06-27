# Goal Recognition

> Mecanismo NLME — descobrir o objetivo **real** por trás da frase do usuário.

## Princípio

Nem sempre o texto digitado é o objetivo de negócio. Goal Recognition infere a intenção estratégica.

## Matriz de inferência

| Usuário diz | Objetivo real provável |
|-------------|------------------------|
| "Está feio" | Melhor UX, UI, Design, Experiência, percepção premium |
| "Está lento" | Performance, arquitetura, queries, percepção de velocidade |
| "Ninguém usa" | Onboarding, UX, valor percebido, copy, adoção |
| "Suporte alto" | UX, help, microcopy, fluxos, documentação |
| "Parece amador" | Brand, UI moderna, Design System, Product Excellence |
| "Confuso" | UX, information architecture, labels, fluxos |
| "Quero impressionar" | Product Excellence, benchmark, polish visual |
| "Preciso lançar" | Launch readiness, QA, growth, infra |
| "Analise o KB" | Auditoria de conteúdo, UX da biblioteca, gaps de processo/POP |

## Perspectivas (SIL complementa)

Goal Recognition considera brevemente:

- **CEO** — valor de negócio
- **CPO** — experiência e adoção
- **CTO** — viabilidade técnica
- **Head UX** — fricção e clareza

## Saída

Adiciona ao Translation Brief / Mission Package:

```yaml
goal_literal: ""
goal_real: ""
goal_secondary: []
business_outcome: ""
user_outcome: ""
```

## Regras

- Preferir inferência autônoma quando confidence ≥ 60
- Perguntar só se objetivos conflitantes e risco alto
- Nunca assumir escopo de implementação sem Mission Builder

## Referências

- `docs/Strategic-Intelligence-Layer.md`
- `skills/mission-translator/SKILL.md`
- `rules/goal-recognition.md`
