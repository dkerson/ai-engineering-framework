# Workflow: Especificação Funcional (documento)

> Gera e grava EF HTML + MD — entrega documental, sem implementação.

## Trigger

`functional-spec-doc` — sinais:

- especificação funcional, EF, spec funcional, kickoff
- AS IS / TO BE, requisitos formais, documento para cliente
- "gere a EF", "crie a spec de"

## Pipeline

Modo: **Standard**

```
Context Builder* → EF Doc Generator → Entrega
```

\* Context Builder só se projeto/escopo desconhecido.

## Passos

| # | Skill | Ação |
|---|-------|------|
| 1 | context-builder | Mapear sistema, repos, rotas (se necessário) |
| 2 | ef-doc-generator | Investigar, gerar HTML+MD, **gravar em docs/specs/** |

## Saída

```
docs/specs/EF_{Cliente}_{Sistema}_{Nome}.html
docs/specs/EF_{Cliente}_{Sistema}_{Nome}.md
docs/specs/EF_{...}_pendencias.md  (se aplicável)
```

## Regras de entrega

- **Gravar arquivos** — não responder só no chat
- Resposta final: resumo + caminhos + como abrir HTML no browser
- Não invocar QA, code-review ou implementação

## Referências

- Skill: `skills/ef-doc-generator/SKILL.md`
- Template: `docs/templates/functional-spec.html`
