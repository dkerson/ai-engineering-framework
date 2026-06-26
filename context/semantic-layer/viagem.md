# Viagem / Rota (Linehaul)

> No contexto Irisys Linehaul, "viagem" alinha-se a **rota** operacional Meli/Shopee.

## Definição de negócio

- **Linehaul (LH):** transporte entre bases/hubs (Shopee SPX, Meli).
- Rota precisa estar disponível na **API fiscal** e/ou **4PL** antes da emissão.
- MDF-e vincula CT-es da viagem (ver `mdfe.md`).

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Rota Shopee 4PL | `tb_spe_webhook` | — | API 4PL webhook | Monitoramento |
| Rota/pacote Meli | — | — | API fiscal Meli | Gestão CT-e |
| Fila webhook | MongoDB `WEBHOOK_SHOPEE` | job DriveAnalytics | — | — |

## Filtros padrão

- Rotas do tenant/carrier correto (Meli: app atribuído ao carrier)

## Lacunas conhecidas

- [ ] Modelo de entidade "viagem" unificado no SQL vs eventos webhook
- [ ] Deluna/FECTO: coexistência e redirect 4PL (ver PROC §8)

## Referências

- `docs/processes/PROC_Irisys_EmissaoCTeMdfe.md` §3, §12 FAQ
