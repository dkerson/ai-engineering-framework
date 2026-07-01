# Codex Model Selection

> Regra operacional para escolher modelo e nivel de raciocinio no Codex antes de missoes do framework.

## Objetivo

Evitar recomendacoes desatualizadas de modelo e alinhar custo, risco e profundidade de raciocinio ao tipo de missao.

## Modelos disponiveis no Codex

Lista observada no Codex:

| Modelo | Uso recomendado |
|--------|-----------------|
| `GPT-5.5` | Missoes complexas, arquitetura, RAG, banco, seguranca, producao, refatoracao ampla e execucao end-to-end. |
| `GPT-5.4` | Features medias, revisoes tecnicas, bugs com algum contexto e implementacoes sem alto risco. |
| `GPT-5.4-Mini` | Ajustes pequenos, UI simples, documentacao, perguntas tecnicas e validacoes pontuais. |
| `GPT-5.3-Codex-Spark` | Tarefas rapidas, comandos diretos, leitura curta, triagem e respostas de baixo risco. |

## Niveis de raciocinio

| Nivel | Uso recomendado |
|-------|-----------------|
| `Baixa` | Perguntas diretas, comandos simples e mudancas triviais. |
| `Media` | Trabalho padrao de desenvolvimento com baixo ou medio risco. |
| `Alta` | Implementacao com multiplos arquivos, backend/API, banco, auth, integracoes e validacao. |
| `Altissimo` | Arquitetura, RAG, seguranca, producao, migracoes sensiveis, incidentes e Technical Council. |

## Matriz rapida

| Missao | Modelo | Raciocinio |
|--------|--------|------------|
| Fast Path, pergunta, status, explicacao | `GPT-5.3-Codex-Spark` ou `GPT-5.4-Mini` | `Baixa` |
| Ajuste pontual de UI/docs/codigo | `GPT-5.4-Mini` | `Baixa` ou `Media` |
| Feature pequena ou bug comum | `GPT-5.4` | `Media` |
| Backend/API/banco sem arquitetura nova | `GPT-5.4` | `Alta` |
| RAG, chat com base de conhecimento, pgvector, Azure OpenAI | `GPT-5.5` | `Alta` |
| RAG em producao, seguranca, permission-aware retrieval, deploy, Technical Council | `GPT-5.5` | `Altissimo` |

## Regra para Umbra RAG

Para implementar RAG + chat da base Irisys/Biblioteca no Umbra, usar:

```text
Modelo: GPT-5.5
Raciocinio: Alta
```

Escalar para `Altissimo` quando a etapa envolver decisao arquitetural, seguranca, permissao por escopo, migracao de banco, deploy em producao ou incidente.

## Politica de custo

Usar o menor par modelo/raciocinio seguro. Nao escolher `GPT-5.5` por padrao para tarefas pequenas, mas tambem nao usar modelos compactos para missoes que cruzam backend, frontend, banco, infra, seguranca e producao.

## Atualizacao

Quando o Codex alterar a lista de modelos disponiveis, atualizar este documento e revisar:

- `rules/token-budget-policy.md`
- `workflows/modes.md`
- `AGENTS.md`
