# Workflow: Documento de Processo

> Gera e grava guia/passo a passo HTML + MD — entrega documental.

## Trigger

`process-doc` — sinais:

- processo, passo a passo, guia, manual, tutorial
- como funciona, rotina, procedimento operacional
- "documente o processo de", "explique como"

## Pipeline

Modo: **Standard**

```
Context Builder* → Process Doc Generator → Entrega
```

\* Context Builder só se processo/sistema desconhecido.

## Passos

| # | Skill | Ação |
|---|-------|------|
| 1 | context-builder | Identificar módulo, rotas, permissões (se necessário) |
| 2 | process-doc-generator | Estruturar passos, gerar HTML+MD, **gravar em docs/processes/** |

## Saída

```
docs/processes/PROC_{Sistema}_{Nome}.html
docs/processes/PROC_{Sistema}_{Nome}.md
```

## Regras de entrega

- **Gravar arquivos** — não responder só no chat
- Resposta final: resumo + caminhos
- Não confundir com EF (kickoff) nem screen-doc (tela Irisys KB)

## Referências

- Skill: `skills/process-doc-generator/SKILL.md`
- Template: `docs/templates/process-doc.html`
- Exemplo: `docs/pmo/relatorio-sprint-clickup-guia-usuario.html`
