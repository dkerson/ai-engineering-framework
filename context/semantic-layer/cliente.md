# Cliente / Participante

> No Irisys, "cliente" aparece em papéis distintos: **tenant** (transportadora logada), **cliente transportadora** (emissão faturas), **participante fiscal** (CT-e).

## Definição de negócio

| Conceito | Definição |
|----------|-----------|
| **Cliente logado (tenant)** | Transportadora/organização da sessão — isola dados (`CodCliente`) |
| **Cliente transportadora** | Tomador/contratante na importação de faturas (lista "Clientes transportadoras") |
| **Participante fiscal** | Pessoa/empresa em papéis CT-e: remetente, destinatário, tomador, expedidor, recebedor |

Participante com CNPJ/CPF único por organização; primeiro endereço é principal. Tomador ausente pode **bloquear** emissão CT-e.

## Fontes de dados

| Conceito | Tabela/View | Procedure | API | Tela/Relatório |
|----------|-------------|-----------|-----|----------------|
| Participante fiscal | cadastro participantes | — | API participantes | `/fiscal/participantes` |
| Cliente transportadora (faturas) | lista auxiliar | — | `GET .../getClients` | `/financeiro/emissao_faturas` |
| Empresa emitente | cadastro empresas | — | `GET .../getEmpresas` | Emissão Faturas, CT-e |
| Tenant | MongoDB `tenants` | — | — | Empresas |

## Chaves de relacionamento

- Participante → endereços (principal + adicionais, até 10)
- Fatura: `CodigoEmpresaCliente`, `CodigoEmpresa` no lote
- CT-e: participantes alimentam Gestão CT-e e Tabela Frete

## Filtros padrão

- Listagens por `CodCliente` da sessão
- Participantes: busca, ordenação na listagem

## Lacunas conhecidas

- [ ] Nome exato da tabela SQL de participantes fiscais
- [ ] Entidade "cliente transportadora" no schema

## Referências

- `EF_IRS_Irisys_ParticipantesFiscais.md`
- `EF_IRS_Irisys_EmissaoFaturas.md`
- `transportadora.md`
