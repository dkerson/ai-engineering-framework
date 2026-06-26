# Transportadora

> Irisys: cliente transportador (tenant). Umbra: contexto distinto — ver nota.

## Definição de negócio (Irisys)

- **Transportadora** = cliente do Irisys com **tenant** isolado (`CodCliente`, credenciais em MongoDB `tenants`).
- Cadastro: empresas emitentes, filiais, certificado A1, motoristas, veículos, tabela de frete.
- Linehaul Meli/Shopee: transportadora solicita credenciais ao marketplace; implantação Otus7 configura integrações.

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Tenant / credenciais | MongoDB `tenants` | — | API fiscal Meli/Shopee | Empresas |
| Cliente transportadora (lote) | cadastro cliente | — | CTEBatch | CT-e Lotes (formulário) |
| Carrier ID (Meli) | `tenants` | — | API Meli | — |

## Chaves de relacionamento

- `CodCliente` isola lotes, pacotes e parâmetros fiscais
- Empresa emitente (CNPJ) vs filial — validar antes de emissão

## Filtros padrão

- Listagens fiscais: **cliente logado** (tenant da sessão)

## Lacunas conhecidas

- [ ] Tabela SQL exata de cadastro transportadora no DriveAnalytics
- [ ] Umbra: transportadora não é entidade de negócio do portal

## Referências

- `docs/processes/PROC_Irisys_EmissaoCTeMdfe.md` §2, §5–6
