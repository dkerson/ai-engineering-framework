# Design Guide — Operacional

## Antes de gerar interface

O Orchestrator responde internamente:

1. Projeto tem Design System?
2. Existe identidade visual?
3. Existe biblioteca de componentes?
4. Existe padrão visual / guideline / tema?
5. É legado?

→ Define **Design Mode** (`rules/design/design-modes.md`)

## Pipeline mínimo (interface nova ou significativa)

| Etapa | Skill |
|-------|-------|
| Produto | product-designer |
| Pesquisa* | ux-researcher |
| UX | ux-designer |
| UI | ui-designer |
| Tokens | design-system |
| Referências | benchmark-specialist |
| Implementação | react / flutter |
| Revisão | design-reviewer |
| Scores | product-aesthetic-director |
| QA | qa |

\* ux-researcher quando requisitos vagos ou novo produto

## Critérios de entrega

- Aparência moderna (dentro do modo)
- Consistência visual
- Usabilidade e produtividade
- Leitura desktop + mobile
- Acessibilidade
- Hierarquia clara
- Reuso máximo de componentes
- Mínimo de cliques

## Quando pular pipeline completo

- LEGACY + typo/label → Fast/Standard sem redesign
- Alteração só backend → sem skills de design
- Docs sem UI → sem design pipeline

## Referências de qualidade (princípios)

Linear, Stripe, Notion, Vercel, GitHub, Material 3, Apple HIG, Fluent 2 — **nunca copiar** layout ou marca.
