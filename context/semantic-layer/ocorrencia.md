# Ocorrência operacional

> Irisys não possui EF dedicada "Ocorrências" no catálogo Umbra — ocorrências aparecem no contexto de **pacotes da rota** e **validação**.

## Definição de negócio

- **Reclamações** e indicadores de problema em pacotes (Ficha de Rota).
- **Status de validação** da rota — independente do carregamento financeiro.
- **PNR**, transferência, volumosos — flags/indicadores em `DetalhesRotasPacotes`.

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Indicadores pacote | `DetalhesRotasPacotes` | `UspGetMLFichaDadosPacotes` | pacotes da rota | Ficha de Rota |
| Status validação rota | — | — | `/v2/logistic/validationStatus` | Ficha de Rota |
| Mapa/validação | — | — | `/v2/support/validationMap` | Ficha de Rota (aba Mapa) |
| Erro pacote CT-e | `tb_cte_lotes_pacotes` | — | CTEBatch timeline | CT-e Lotes |

## Chaves de relacionamento

- Ocorrência/reclamação vinculada ao **pacote** dentro da **rota**
- Erro fiscal no campo `erro` (ou equivalente) em `tb_cte_lotes_pacotes`

## Filtros padrão

- Consulta por rota e período na ficha

## Lacunas conhecidas

- [ ] Módulo dedicado de ocorrências (se existir fora das EFs analisadas)
- [ ] Tabela SQL de reclamações/PNR
- [ ] Integração ocorrência → suporte ClickUp

## Referências

- `EF_IRS_Irisys_FichaRota.md`
- `entrega.md`, `cte.md`
