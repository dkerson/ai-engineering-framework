# MDFe — Manifesto Eletrônico de Documentos Fiscais (Irisys)

> Preenchido a partir de `docs/processes/PROC_Irisys_EmissaoCTeMdfe.md` e `EF_IRS_Irisys_CTeLotes.md`.

## Definição de negócio

- **MDF-e** vincula CT-es de uma **viagem** / lote autorizado.
- Regra operacional (PROC): emitir MDF-e **após** CT-es do lote **autorizados** — ação **Gerar MDF-e** na listagem de lotes (`/financeiro/cte-lotes`).
- **Não** emitir manifesto antes do lote CT-e autorizado.

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Lote CT-e (origem MDF-e) | `tb_cte_lotes` | — | `/v2/financial/cte-batch` | `/financeiro/cte-lotes` |
| CT-es sem MDF-e | — | endpoint CTEBatch | `CteMdfeBatchXmlExportModule` | CT-e Lotes |
| Exportação XML CT-e/MDF-e | `tb_cte_lotes`, `tb_cte_lotes_pacotes` | — | export ZIP por período | CT-e Lotes |

## Chaves de relacionamento

- MDF-e gerado a partir de lote CT-e autorizado (mesmo módulo fiscal)
- CT-es elegíveis: consultar endpoint de CT-es sem MDF-e no backend

## Filtros padrão

- Somente lotes com CT-es em status **autorizado** para geração de MDF-e
- Grupos de acesso **CTE / MDFE** (mesmos parâmetros do lote)

## Regras de agregação

- Um MDF-e por conjunto de CT-es da viagem/lote conforme regra fiscal do módulo
- Não contar CT-e cancelado/rejeitado no manifesto

## Indicadores relacionados

- Ver `indicadores.md`

## Lacunas conhecidas

- [ ] Tabelas específicas de MDF-e no backend (além de vínculo via lote)
- [ ] Status pós-geração MDF-e na timeline

## Referências

- `docs/processes/PROC_Irisys_EmissaoCTeMdfe.md` §7, §12 FAQ
- `docs/specs/EF_IRS_Irisys_CTeLotes.md`
