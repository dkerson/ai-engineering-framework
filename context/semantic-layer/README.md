# Semantic Layer — Camada Semântica Otus/Irisys

> **Finalidade:** mapear conceitos de negócio para fontes técnicas (tabelas, views, procedures, APIs, telas). Base para skills `semantic-layer-specialist` e `business-rule-mapper`.

## Como usar

1. Preencher cada arquivo de domínio conforme o conhecimento do time — **não inventar regras**
2. O projeto consumidor pode sobrescrever em `context/semantic-layer/` local
3. Skills consultam aqui antes de escrever SQL ou relatórios

## Estrutura por arquivo

Cada `*.md` de domínio segue o template em `templates/data/semantic-layer-entry.md`.

## Domínios

| Arquivo | Conceitos (preencher) |
|---------|------------------------|
| [cte.md](cte.md) | Conhecimento de Transporte Eletrônico |
| [mdfe.md](mdfe.md) | Manifesto Eletrônico |
| [financeiro.md](financeiro.md) | Faturamento, receitas, custos |
| [motorista.md](motorista.md) | Motoristas, vínculos, documentos |
| [transportadora.md](transportadora.md) | Transportadoras, contratos |
| [cliente.md](cliente.md) | Clientes, grupos, contratos |
| [viagem.md](viagem.md) | Viagens, rotas, status |
| [entrega.md](entrega.md) | Entregas, comprovantes |
| [ocorrencia.md](ocorrencia.md) | Ocorrências operacionais |
| [indicadores.md](indicadores.md) | KPIs transversais e definições |

## Integração

- Framework: `rules/data/semantic-layer.md`
- Projeto Umbra: complementar com `context/business.md` do consumidor
- Irisys: mapear telas/relatórios conforme forem documentados
