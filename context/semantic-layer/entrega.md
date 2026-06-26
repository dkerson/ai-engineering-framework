# Entrega (pacote / parada)

> No Irisys, entrega operacional materializa-se como **pacote** e **parada** na Ficha de Rota — não como módulo isolado "Entregas".

## Definição de negócio

- **Pacote:** unidade rastreada na rota (marketplace Linehaul/last mile conforme operação).
- **Parada/endereço:** ponto de entrega ou coleta associado ao pacote na ficha.
- Campos documentados: transferência, PNR, reclamações, volumosos (EF Ficha de Rota).

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Pacotes da rota | `DetalhesRotasPacotes` | `UspGetMLFichaDadosPacotes` | `GET /DetalhesRotas/{codigo}/pacotes` | `/logistics/rotas/:id` (aba Pacotes) |
| Pacote CT-e (fiscal) | `tb_cte_lotes_pacotes` | CTEBatch | `/v2/financial/cte-batch` | `/financeiro/cte-lotes` |
| Webhook Shopee | `tb_spe_webhook` | — | API 4PL | Monitoramento |

## Chaves de relacionamento

- Rota (`codigo`) → N pacotes (`DetalhesRotasPacotes`)
- Lote CT-e → N pacotes fiscais (`tb_cte_lotes_pacotes`)

## Filtros padrão

- Pacotes exibidos no contexto da rota selecionada
- CT-e: pacotes do lote + status de processamento SEFAZ

## Regras de agregação

- Contagem de pacotes por rota: listagem `ListaRotasFinanceiro` (campo pacotes)
- Não misturar pacotes operacionais (logística) com pacotes fiscais (lote) sem mapear chave comum

## Lacunas conhecidas

- [ ] Chave entre pacote marketplace e `tb_cte_lotes_pacotes`
- [ ] Status enum de entrega na logística vs fiscal

## Referências

- `EF_IRS_Irisys_FichaRota.md` §5
- `cte.md`, `viagem.md`
