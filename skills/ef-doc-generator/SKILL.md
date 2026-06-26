---
name: ef-doc-generator
description: >-
  Gera e grava especificação funcional Otus7 em HTML + Markdown (design system
  com logo Otus7). Usar quando pedir EF, especificação funcional, spec de
  feature, documento kickoff, AS IS/TO BE ou gerar spec para cliente/sistema.
---

# EF Doc Generator

## Objetivo

Produzir **Especificação Funcional** completa no padrão visual Otus7 (HTML + MD) e **gravar no repositório** — não apenas responder no chat.

## Quando usar

- "Gere a EF de…", "especificação funcional", "documento EF"
- Feature nova ou mudança que exige kickoff formal
- Pedido com cliente/sistema (ex.: IRS Irisys, Umbra PMO)
- Após product-owner ou investigação de código existente

## Quando NÃO usar

- Documento passo a passo / guia de uso → `process-doc-generator`
- Tela Irisys já existente (documentação operacional) → skill `screen-doc`
- Spec técnica de implementação pura → `technical-spec` (sem HTML Otus)

## Responsabilidades

1. **Investigar** — código/repos relevantes (mínimo necessário; `rules/token-economy.md`)
2. **Montar conteúdo** — seções EF completas (ver mapa abaixo)
3. **Gerar HTML** — a partir de `docs/templates/functional-spec.html` (substituir placeholders ou preencher seções)
4. **Gerar MD espelho** — mesmo conteúdo, formato markdown editável
5. **Gravar arquivos** — usar ferramenta Write; **obrigatório persistir no disco**
6. **Pendências** — se houver gaps, gravar `{nome_base}_pendencias.md`
7. **Responder** — resumo curto + caminhos dos arquivos (não colar HTML/MD inteiro no chat)

## Saída obrigatória (gravar no repo)

```
docs/specs/{nome_base}.html
docs/specs/{nome_base}.md
docs/specs/{nome_base}_pendencias.md   ← se houver gaps
```

### Convenção de nome

`EF_{Cliente}_{Sistema}_{NomeCurtoPascalCase}`

Exemplos:
- `EF_IRS_Irisys_AliquotaICMS`
- `EF_InternoOtus7_Umbra_LoginGoogle`

## Entradas esperadas

- Título / feature / tela / processo a especificar
- Cliente e sistema (inferir ou perguntar só se bloqueante)
- Opcional: articleId, menuControllerId, rotas, repos GitHub

## Saídas esperadas

| Arquivo | Formato |
|---------|---------|
| `.html` | Design system Otus7 — logo header/footer, slides, sumário navegável |
| `.md` | Frontmatter YAML + tabelas + seções espelhadas |
| `_pendencias.md` | Lista de pontos a confirmar antes de DEV |

## Seções EF (HTML — 20 blocos)

Referência: [template-map.md](template-map.md) e exemplos em `docs/specs/EF_IRS_Irisys_AliquotaICMS.*`

1. Objetivo · 2. AS IS/TO BE · 3. Benefícios · 4. Escopo · 5. Domínio
6. Regras (RN01…) · 7. Validação cruzada · 8. Matriz · 9. RF/RNF
10. Critérios aceite · 11. Fluxo macro · 12. Swimlanes · 13. Integrações
14. Permissões · 15. Massa testes · 16. Premissas · 17. Riscos
18. Pendências · 19. Dicionário · 20. Versionamento

## Checklist

- [ ] `nome_base` segue convenção EF_*
- [ ] HTML usa logo `https://www.otus7.com/assets/images/logo-otus-7.svg`
- [ ] HTML e MD gravados em `docs/specs/`
- [ ] Conteúdo em pt-BR
- [ ] Regras numeradas RN01, RN02…
- [ ] Pendências em arquivo separado se existirem
- [ ] Chat: só resumo + paths (não dump de arquivos)

## Integração com outras skills

- **Upstream:** orchestrator, context-builder, product-owner, functional-spec
- **Downstream:** technical-spec, tech-lead (implementação)

## Modo de execução (orchestrator)

Quando classificação = `functional-spec-doc`:

```
context-builder (se necessário) → ef-doc-generator → [fim]
```

**Não** passar por code-review ou QA — entrega é documentação gravada.

## Exemplos

**Input:** "Gere a EF do login com Google no Umbra"

**Output gravado:**
- `docs/specs/EF_InternoOtus7_Umbra_LoginGoogle.html`
- `docs/specs/EF_InternoOtus7_Umbra_LoginGoogle.md`

**Chat:** "EF gerada. Arquivos: docs/specs/EF_InternoOtus7_Umbra_LoginGoogle.{html,md}"


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- Template HTML: `docs/templates/functional-spec.html`
- Mapa seções: [template-map.md](template-map.md)
- Exemplo real: `docs/specs/EF_IRS_Irisys_AliquotaICMS.html`
- Comparação screen-doc: `docs/library/screen-doc-vs-ef-funcional.md`
- Workflow: `workflows/functional-spec-doc.md`
