---
name: process-doc-generator
description: >-
  Gera e grava documento explicativo de processo ou passo a passo em HTML +
  Markdown (casca visual Otus7 com logo). Usar quando pedir guia, processo,
  como funciona, passo a passo, manual de uso, rotina operacional ou tutorial.
---

# Process Doc Generator

## Objetivo

Produzir **documento explicativo de processo** (guia, passo a passo, manual) no padrão visual Otus7 e **gravar no repositório**.

Mesma casca visual da EF (logo, deck, slides, meta-grid) — conteúdo orientado a **explicar e conduzir**, não a kickoff de projeto.

## Quando usar

- "Documente o processo de…", "passo a passo", "guia de uso"
- "Como funciona…", "manual", "rotina", "tutorial"
- Explicar fluxo operacional existente (import, aprovação, deploy interno)
- Onboarding de usuários ou operação

## Quando NÃO usar

- Especificação funcional / kickoff / AS IS-TO BE → `ef-doc-generator`
- Tela Irisys para KB → `screen-doc`
- README técnico de código → documentação simples em markdown

## Responsabilidades

1. **Entender** o processo (perguntar só se bloqueante)
2. **Investigar** código/UI mínima se processo for de sistema
3. **Estruturar** conteúdo explicativo (intro → passos → FAQ)
4. **Gerar HTML** — `docs/templates/process-doc.html`
5. **Gerar MD espelho** — editável, com sumário linkável
6. **Gravar arquivos** — Write tool; **obrigatório persistir**
7. **Responder** — resumo + paths (sem dump no chat)

## Saída obrigatória (gravar no repo)

```
docs/processes/{nome_base}.html
docs/processes/{nome_base}.md
```

### Convenção de nome

`PROC_{Sistema}_{NomeCurtoPascalCase}`

Exemplos:
- `PROC_Umbra_ImportClickUpSprint`
- `PROC_Irisys_EmissaoCTe`
- `PROC_Umbra_OnboardingPortal`

Processos de módulo específico podem ir em subpasta:
- `docs/pmo/PROC_Umbra_ClickUpReferencias.md` (se já existir convenção local)

**Preferência:** `docs/processes/` para novos documentos.

## Entradas esperadas

- Nome do processo
- Sistema/módulo (Umbra, Irisys, PMO, KB…)
- Público-alvo (operador, admin, dev)
- Opcional: rotas, permissões, screenshots/assets

## Saídas esperadas

| Arquivo | Conteúdo |
|---------|----------|
| `.html` | Guia visual Otus7 — passo a passo em `.step-block` |
| `.md` | Versão editável com sumário e tabelas |

## Seções (HTML — 10 blocos)

Referência: [template-map.md](template-map.md) e `docs/pmo/relatorio-sprint-clickup-guia-usuario.*`

1. Introdução · 2. Acesso e pré-requisitos · 3. Visão geral
4. **Passo a passo** (núcleo — `.step-block`) · 5. Decisões/ramificações
6. Papéis · 7. Dicas · 8. FAQ · 9. Glossário · 10. Versionamento

## Formato passo a passo (HTML)

```html
<article class="step-block">
  <div class="step-block__head">
    <span class="step-block__num">1</span>
    <h3>Título do passo</h3>
  </div>
  <p>Descrição...</p>
  <ol><li>Subpasso</li></ol>
  <div class="note note--tip"><strong>Dica:</strong> ...</div>
</article>
```

Classes de nota: `.note--tip`, `.note--warn`, `.note--admin`

## Checklist

- [ ] `nome_base` segue convenção PROC_*
- [ ] Logo Otus7 no header e footer
- [ ] HTML + MD gravados
- [ ] Passos numerados e acionáveis
- [ ] pt-BR
- [ ] Chat: resumo + paths apenas

## Integração com outras skills

- **Upstream:** orchestrator, context-builder
- **Downstream:** nenhuma (entrega documental)

## Modo de execução (orchestrator)

Classificação = `process-doc`:

```
context-builder (se necessário) → process-doc-generator → [fim]
```

## Exemplos

**Input:** "Documente o processo de importação do ClickUp no Umbra"

**Output gravado:**
- `docs/processes/PROC_Umbra_ImportClickUpSprint.html`
- `docs/processes/PROC_Umbra_ImportClickUpSprint.md`

**Referência de qualidade:** `docs/pmo/relatorio-sprint-clickup-guia-usuario.html`


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- Template HTML: `docs/templates/process-doc.html`
- Mapa seções: [template-map.md](template-map.md)
- Exemplo: `docs/pmo/relatorio-sprint-clickup-guia-usuario.*`
- Workflow: `workflows/process-doc.md`
