# Financeiro (Irisys)

> **Cuidado:** `rules/data/financial-data-care.md` — dupla validação em indicadores financeiros.
> Fontes: EFs em `docs/specs/EF_IRS_Irisys_*.md`, `EF_InternoOtus7_DriveAnalytics_CIOTs.md`.

## Definição de negócio

Módulo fiscal/financeiro do Irisys cobre: faturas importadas, alíquota ICMS, resultado financeiro de rotas marketplace, CIOTs, tabela de frete e relatórios Power BI embarcados.

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Lote de faturas | `tb_fin_fat_cliente` | — | `/financial/EmissaoFaturas` | `/financeiro/emissao_faturas` |
| Fatura | `tb_fin_faturas` | SSRS + Blob | visualizarFatura, baixarLoteFaturas | Emissão de Faturas |
| Alíquota ICMS | `tb_aliquota_icms` | usada em CTEProcessamento | `/v2/financial/aliquota_icms` | `/financeiro/aliquota_icms` |
| Alteração rota (financeiro) | `tb_fin_resultado_financeiro_alteracao` | DetalhesRotas* | `POST /DetalhesRotas/{id}` | `/logistics/rotas` |
| Pré-fatura marketplace | `DetalhesRotasFinanceiroMarketplace` | `UspGetMLFichaFinanceiroTransportadora`, etc. | `/DetalhesRotas/{id}/financeiro-marketplace` | Ficha de Rota (aba Financeiro) |
| CIOT | — | — | `/v1/financeiro/ciots` | `/financeiro/ciots` |
| Tabela de frete | cadastro fiscal | — | tabela-frete API | `/fiscal/tabela-frete` |
| Relatório Power BI | `tb_relatorios`, `tb_controller` | — | `/sistema/PowerBI` | `/fiscal/averbação-` (ex.) |
| Log acesso PBI | `tb_relatorio_logs` | — | POST PowerBI | Visualizar relatório |
| Filtros PBI | `tb_relatorios_filtros` | — | embed config | Power BI embed |

## Chaves de relacionamento

- Faturas: lote `tb_fin_fat_cliente` → N `tb_fin_faturas`
- ICMS: combinação UF origem × UF destino + vigência por `CodCliente`
- Ficha rota: código rota → pacotes, financeiro marketplace, alterações em `tb_fin_resultado_financeiro_alteracao`
- Power BI: `tb_controller.ctr_cd_controller` (ex. 776 Averbação) → `tb_relatorios.rel_ds_caminho`

## Filtros padrão

- **Sempre** `CodCliente` / cliente logado
- Alíquota ICMS: `Excluido == false`, vigente
- Ficha rota: período default últimos 2 dias até hoje; marketplace default Mercado Livre
- Power BI: filtros por usuário e cliente (não-admin)

## Regras de agregação

- Lote faturas: `qtd_de_faturas` calculado no lote — validar vs contagem em `tb_fin_faturas`
- Ficha rota: comparar **Irisys x Pré-Fatura** — divergência é alerta, não soma automática
- ICMS: um registro ativo por combinação UF×UF (encerramento lógico do anterior ao salvar)

## Indicadores relacionados

- `indicadores.md` — KPIs de lote CT-e, faturas, pré-fatura

## Lacunas conhecidas

- [ ] Tabelas exatas de CIOT no SQL
- [ ] Procedures completas de fechamento financeiro marketplace
- [ ] Catálogo de todos os relatórios Power BI (`tb_relatorios`)

## Referências

- `EF_IRS_Irisys_EmissaoFaturas.md`
- `EF_IRS_Irisys_AliquotaICMS.md`
- `EF_IRS_Irisys_FichaRota.md`
- `EF_IRS_Irisys_AverbacaoPowerBI.md`
- `EF_IRS_Irisys_TabelaFrete.md`
- `EF_InternoOtus7_DriveAnalytics_CIOTs.md`
