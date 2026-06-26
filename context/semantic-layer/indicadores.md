# Indicadores — KPIs transversais

> Catálogo inicial. Preencher com time fiscal/BI — apenas entradas com fonte documentada.

## CT-e Lotes — quantidade por lote

- **Definição:** Número de pacotes/CT-es vinculados a um lote
- **Fórmula / lógica:** Contagem de registros em `tb_cte_lotes_pacotes` por lote
- **Fonte autorizada:** `tb_cte_lotes_pacotes` + API `/v2/financial/cte-batch`
- **Granularidade:** por lote (`tb_cte_lotes`)
- **Filtros obrigatórios:** cliente logado, grupos CTE/MDFE
- **Consumidores:** tela `/financeiro/cte-lotes` (coluna quantidade)
- **Última validação:** EF_IRS_Irisys_CTeLotes v1.0

## CT-e Lotes — valor do lote

- **Definição:** Valor total associado ao lote na listagem
- **Fonte autorizada:** campo em `tb_cte_lotes` (EF)
- **Granularidade:** por lote
- **Lacuna:** validar fórmula vs soma de pacotes em caso de divergência

## Emissão de Faturas — quantidade por lote

- **Definição:** Número de faturas importadas em um lote
- **Fonte autorizada:** `tb_fin_fat_cliente.qtd_de_faturas` / contagem `tb_fin_faturas`
- **Granularidade:** por lote de importação
- **Consumidores:** `/financeiro/emissao_faturas`
- **Referência:** `EF_IRS_Irisys_EmissaoFaturas.md`

## Ficha de Rota — Irisys vs Pré-Fatura

- **Definição:** Comparação de valores Irisys com pré-fatura do marketplace
- **Fonte autorizada:** `DetalhesRotasFinanceiroMarketplace` via API financeiro-marketplace
- **Granularidade:** por rota
- **Filtros:** período, marketplace, motorista, base, status
- **Uso:** alertas de divergência (sem pré-fatura, sem base frete, diferença de valores)
- **Referência:** `EF_IRS_Irisys_FichaRota.md`

## Alíquota ICMS vigente

- **Definição:** Alíquota CST/CFOP por UF origem × destino na vigência
- **Fonte autorizada:** `tb_aliquota_icms` (`Excluido == false`)
- **Consumidores:** preparação CT-e (`CTEProcessamentoRepository` quando `aplicar-regra-icms`)
- **Referência:** `EF_IRS_Irisys_AliquotaICMS.md`

## Power BI Averbação (embed)

- **Definição:** Painel analítico fiscal — **não é fluxo transacional**
- **Fonte autorizada:** `tb_relatorios.rel_ds_caminho` via controller 776
- **API:** `/sistema/PowerBI?EncryptCodController={rotaParams}`
- **Consumidores:** `/fiscal/averbação-`
- **Referência:** `EF_IRS_Irisys_AverbacaoPowerBI.md`

- [ ] KPIs CIOT consolidados
- [ ] KPIs PMO Umbra (ClickUp) — módulo PMO do portal, fora do Irisys

## Referências

- `docs/specs/EF_IRS_Irisys_CTeLotes.md`
- `context/semantic-layer/cte.md`
