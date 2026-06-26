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

## Lacunas conhecidas

- [ ] Indicadores financeiros (faturamento, ICMS) — mapear com `financeiro.md` e EF Alíquota ICMS
- [ ] KPIs PMO Umbra (ClickUp) — fora do Irisys; ver módulo PMO

## Referências

- `docs/specs/EF_IRS_Irisys_CTeLotes.md`
- `context/semantic-layer/cte.md`
