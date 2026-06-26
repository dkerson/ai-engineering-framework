# CTe — Conhecimento de Transporte Eletrônico (Irisys)

> Preenchido a partir de `docs/processes/PROC_Irisys_EmissaoCTeMdfe.md` e `docs/specs/EF_IRS_Irisys_CTeLotes.md`. **Não inventar** regras além das fontes citadas.

## Definição de negócio

- **CT-e** no Irisys para Linehaul (Meli/Shopee): emissão de **rede subcontratada** com base no **CT-e guarda-chuva** (XML do marketplace).
- **Linehaul Meli:** emissão típica **manual** na Gestão de CT-e.
- **Linehaul Shopee:** manual e **automática** (evolução; requer base de frete + 4PL estável).
- **Last Mile** neste contexto **não emite** CT-e (PROC v1.2).
- Irisys **não** emite CT-e via WhatsApp (canal FECTO/concorrente).

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Lote de CT-e | `tb_cte_lotes` | — | `GET/POST /v2/financial/cte-batch` | `/financeiro/cte-lotes` |
| Pacote do lote | `tb_cte_lotes_pacotes` | — | mesmo módulo CTEBatch | CT-e Lotes (detalhe pacote) |
| Anexo do lote | `tb_cte_lotes_anexos` | — | CTEBatch | CT-e Lotes |
| Gestão manual | — | — | APIs fiscais internas + Meli/Shopee | Gestão de CT-e |
| Credenciais tenant | MongoDB `tenants` | — | API fiscal Meli/Shopee | Empresas (cadastro) |
| Webhook Shopee 4PL | `tb_spe_webhook` | — | API 4PL Shopee | Monitoramento rotas |

## Chaves de relacionamento

- Lote ↔ pacotes: `tb_cte_lotes` ↔ `tb_cte_lotes_pacotes` (vínculo por lote)
- Pacote: status, chave CT-e, URLs gravados em `tb_cte_lotes_pacotes`
- **Tenant:** `CodCliente` + credenciais em `tenants` (isolamento por transportadora)

## Filtros padrão

- Listagem de lotes: **cliente logado** + **grupos de acesso CTE/MDFE** (avulso, pré-fatura, admin)
- Emissão: CNPJ emitente vs rota (verificar **filial** antes de go-live)
- Status de pacote/lote conforme processamento SEFAZ (timeline)

## Regras de agregação

- Contagem de CT-es por lote: pacotes em `tb_cte_lotes_pacotes` com status respectivo
- Valor do lote: campo persistido no lote (`tb_cte_lotes`) — validar contra soma de pacotes se divergência reportada
- **Não** agregar CT-e guarda-chuva com rede subcontratada no mesmo total sem regra explícita

## Indicadores relacionados

- Ver `indicadores.md` — catálogo a expandir com time fiscal

## Lacunas conhecidas

- [ ] Mapear procedures de preparação/envio SEFAZ no backend (CTEBatchRepository)
- [ ] Gestão de CT-e: rotas Angular exatas além de CT-e Lotes
- [ ] Status enum completo de `tb_cte_lotes_pacotes`

## Referências

- `docs/processes/PROC_Irisys_EmissaoCTeMdfe.md`
- `docs/specs/EF_IRS_Irisys_CTeLotes.md`
- Repositórios: `Otus7/DriveAnalyticsFrontEnd`, `Otus7/DriveAnalyticsBackEnd`
