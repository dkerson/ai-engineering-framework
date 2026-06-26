# Mapa — EF Doc Generator

> Mapeamento seções ↔ placeholders do template `docs/templates/functional-spec.html`

## Metadados hero

| Campo | Placeholder | Exemplo |
|-------|-------------|---------|
| Título | `{{TITULO}}` | Alíquota ICMS |
| Intro | `{{INTRO}}` | Parágrafo resumo |
| Cliente | `{{META_CLIENTE}}` | IRS |
| Referência | `{{META_REFERENCIA}}` | menuId, articleId, repos |
| Sistema | `{{META_SISTEMA}}` | Irisys |
| Responsável | `{{META_RESPONSAVEL}}` | A definir |

## Frontmatter MD (obrigatório)

```yaml
---
titulo: [Título legível]
nome_base: EF_[Cliente]_[Sistema]_[Nome]
versao: "1.0"
data: "YYYY-MM-DD"
cliente: [Cliente]
sistema: [Sistema]
autor: [Agente/usuário]
revisor: A definir
---
```

## Seções MD espelhadas

| # | Seção HTML id | Seção MD |
|---|---------------|----------|
| — | — | Metadados tabela + Fontes técnicas |
| 1 | `#objetivo` | ## 1. Objetivo |
| 2 | `#cenario` | ## 2. Cenário AS IS / TO BE |
| 3 | `#beneficios` | ## 3. Benefícios |
| 4 | `#escopo` | ## 4. Escopo consolidado |
| 5 | `#modulo-dominio` | ## 5. Detalhamento de domínio |
| 6 | `#regras` | ## 6. Regras de negócio (tabela RN) |
| 7 | `#validacao-cruzada` | ## 7. Validação cruzada (opcional) |
| 8 | `#matriz` | ## 8. Matriz (opcional) |
| 9 | `#requisitos` | ## 9. RF / RNF |
| 10 | `#aceite` | ## 10. Critérios de aceite |
| 11 | `#fluxo` | ## 11. Fluxo macro |
| 12 | `#swimlanes` | ## 12. Swimlanes |
| 13 | `#integracoes` | ## 13. Integrações |
| 14 | `#permissoes` | ## 14. Permissões |
| 15 | `#testes` | ## 15. Massa de testes |
| 16 | `#premissas` | ## 16. Premissas / fora escopo |
| 17 | `#riscos` | ## 17. Riscos |
| 18 | `#pendencias` | ## 18. Pendências (+ arquivo `_pendencias.md`) |
| 19 | `#dicionario` | ## 19. Dicionário |
| 20 | `#versionamento` | ## 20. Versionamento |

## Logo Otus7 (obrigatório)

```html
<img alt="Otus7" src="https://www.otus7.com/assets/images/logo-otus-7.svg"/>
```

Header `.brand-header` + footer `.brand-footer`.

## Pendências

Arquivo `{nome_base}_pendencias.md` com tabela ID | Ponto | Impacto | Responsável.
