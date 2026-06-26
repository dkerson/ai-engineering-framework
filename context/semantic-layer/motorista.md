# Motorista

> Preenchido parcialmente a partir de PROC Irisys (Linehaul Shopee — TripInfo).

## Definição de negócio

- Cadastro operacional obrigatório para emissão (prefill e validação), especialmente **Shopee Linehaul**.
- Evento **TripInfo** (Shopee 4PL) traz motorista, placa, hub na rota.

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Cadastro motorista | cadastros operacionais Irisys | — | — | Cadastros |
| Dados rota (Shopee) | `tb_spe_webhook` / fila | — | API 4PL TripInfo | Monitoramento |

## Chaves de relacionamento

- Rota Shopee ↔ motorista/placa via webhook 4PL
- CT-e: prefill a partir de cadastro + dados da rota

## Lacunas conhecidas

- [ ] Nome exato de tabelas de motorista/veículo no DriveAnalytics
- [ ] Vínculo motorista ↔ CIOT (`/financeiro/ciots`)

## Referências

- `docs/processes/PROC_Irisys_EmissaoCTeMdfe.md` §2.1, glossário TripInfo
- `docs/specs/EF_InternoOtus7_DriveAnalytics_CIOTs.md`
