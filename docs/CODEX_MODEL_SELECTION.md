# Codex Model Selection

> Regra operacional para escolher modelo e nível de raciocínio no Codex antes de missões do framework.

## Objetivo

Evitar recomendações desatualizadas de modelo e alinhar custo, risco e profundidade de raciocínio ao tipo de missão.

## Modelos disponíveis no Codex

Lista observada no seletor atual do Codex:

| Modelo | Uso recomendado |
|--------|-----------------|
| `GPT-5.5` | Missões complexas, arquitetura, RAG, banco, segurança, produção, refatoração ampla e execução end-to-end. |
| `GPT-5.4` | Features médias, revisões técnicas, bugs com algum contexto e implementações sem alto risco. |
| `GPT-5.4-Mini` | Ajustes pequenos, UI simples, documentação, perguntas técnicas e validações pontuais. |
| `GPT-5.3-Codex-Spark` | Tarefas rápidas, comandos diretos, leitura curta, triagem e respostas de baixo risco. |

## Níveis de raciocínio

| Nivel | Uso recomendado |
|-------|-----------------|
| `Baixa` | Perguntas diretas, comandos simples e mudancas triviais. |
| `Média` | Trabalho padrão de desenvolvimento com baixo ou médio risco. |
| `Alta` | Implementação com múltiplos arquivos, backend/API, banco, auth, integrações e validação. |
| `Altíssimo` | Arquitetura, RAG, segurança, produção, migrações sensíveis, incidentes e Technical Council. |

## Matriz rapida

| Missão | Modelo | Raciocínio |
|--------|--------|------------|
| Fast Path, pergunta, status, explicação | `GPT-5.3-Codex-Spark` ou `GPT-5.4-Mini` | `Baixa` |
| Ajuste pontual de UI/docs/código | `GPT-5.4-Mini` | `Baixa` ou `Média` |
| Feature pequena ou bug comum | `GPT-5.4` | `Média` |
| Backend/API/banco sem arquitetura nova | `GPT-5.4` | `Alta` |
| RAG, chat com base de conhecimento, pgvector, Azure OpenAI | `GPT-5.5` | `Alta` |
| RAG em produção, segurança, permission-aware retrieval, deploy, Technical Council | `GPT-5.5` | `Altíssimo` |

## Regra para Umbra RAG

Para implementar RAG + chat da base Irisys/Biblioteca no Umbra, usar:

```text
Modelo: GPT-5.5
Raciocínio: Alta
```

Escalar para `Altíssimo` quando a etapa envolver decisão arquitetural, segurança, permissão por escopo, migração de banco, deploy em produção ou incidente.

## Politica de custo

Usar o menor par modelo/raciocínio seguro. Não escolher `GPT-5.5` por padrão para tarefas pequenas, mas também não usar modelos compactos para missões que cruzam backend, frontend, banco, infra, segurança e produção.

## Atualizacao

Quando o Codex alterar a lista de modelos disponíveis, atualizar este documento e revisar:

- `rules/token-budget-policy.md`
- `workflows/modes.md`
- `AGENTS.md`
