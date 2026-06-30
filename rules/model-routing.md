# Model Routing Policy

> Finalidade: recomendar o modelo Cursor/Codex com melhor custo-beneficio antes da execucao e controlar escalonamento quando a missao exigir mais capacidade.

## Principio central

O framework nao altera automaticamente o seletor de modelo do Cursor ou Codex. O Orchestrator deve recomendar o modelo, justificar a escolha e pausar quando uma troca manual for necessaria.

Aplicar `rules/surface-routing.md` antes desta regra.

## Modelo padrao recomendado

Use a recomendacao padrao da superficie detectada:

| Superficie | Padrao economico | Escalonamento |
|------------|------------------|---------------|
| Cursor | `Composer 2.5 Standard` | `Auto` ou modelo forte disponivel |
| Codex | `gpt-5.4-mini` | `gpt-5.5` |
| Desconhecida | informar opcoes Cursor e Codex | perguntar se a escolha bloquear execucao |

Use `Auto` ou modelo mais forte somente quando o risco, a ambiguidade ou a chance de retrabalho justificar o custo adicional.

## Recomendacao obrigatoria no plano

Antes de executar qualquer task, o Orchestrator deve apresentar:

```markdown
## Plano de execucao
1. ...
2. ...

## Modelo recomendado
- Superficie: [Cursor | Codex | Desconhecida]
- Modelo: [Composer 2.5 Standard | Auto | gpt-5.4-mini | gpt-5.5 | modelo forte especifico]
- Motivo: [custo, risco, complexidade, velocidade ou confiabilidade]
- Escalonamento previsto: [quando mudar de modelo durante a execucao]

Posso seguir com este plano?
```

A execucao so continua apos aprovacao explicita do usuario, exceto em pedidos que sejam apenas pergunta/resposta e nao envolvam leitura ampla, comandos, edicao ou validacao.

## Matriz de escolha

| Cenario | Cursor | Codex |
|---------|--------|-------|
| Pergunta, explicacao, documentacao simples | Composer 2.5 Standard | gpt-5.4-mini |
| Fast Path, ajuste localizado, label, copy, CSS simples | Composer 2.5 Standard | gpt-5.4-mini |
| Analise inicial de bug ou feature pequena | Composer 2.5 Standard | gpt-5.4-mini |
| Frontend simples ou componente isolado | Composer 2.5 Standard | gpt-5.4-mini |
| Backend simples, DTO, controller ou service localizado | Composer 2.5 Standard | gpt-5.4-mini |
| Auth, autorizacao, permissoes, tenants, claims | Auto | gpt-5.5 |
| Banco, migration, query critica, dados financeiros/fiscais | Auto | gpt-5.5 |
| Integracao externa, webhook, pagamento, SEFAZ, marketplace | Auto | gpt-5.5 |
| Deploy, producao, incidente, Docker/infra critica | Auto | gpt-5.5 |
| Refatoracao multi-modulo ou arquitetura | Auto | gpt-5.5 |
| 2 falhas com a mesma hipotese ou causa incerta | Auto | gpt-5.5 |
| Latencia humana mais importante que custo | Auto ou modo rapido explicitamente justificado | gpt-5.3-codex-spark se disponivel, senao gpt-5.5 |

## Escalonamento durante a execucao

Se durante a task surgir um gatilho de escalonamento, o Orchestrator deve parar antes da proxima acao de risco e avisar:

```markdown
Identifiquei necessidade de trocar o modelo.

- Modelo atual assumido: [modelo informado/assumido]
- Modelo recomendado agora: [Auto | gpt-5.5 | modelo forte]
- Motivo: [risco/ambiguidade/retry/contexto]
- Proxima acao apos a troca: [...]

Por favor altere o modelo na superficie ativa para o recomendado e me avise quando estiver pronto para continuar.
```

Depois da confirmacao do usuario, continuar do Working Context ativo sem reiniciar a investigacao.

## Nao escalonar por padrao

Nao recomendar Auto apenas porque a tarefa parece grande. Primeiro classificar risco, superficies afetadas, dominios e chance de retrabalho.

Nao recomendar modelo caro para:

- leitura dirigida;
- perguntas conceituais;
- documentacao;
- alteracoes pequenas;
- validacoes simples;
- tarefas com arquivo e linha claramente indicados.

## Registro no Working Context

Registrar em toda task executavel:

```markdown
### Model Routing
- Superficie:
- Modelo recomendado:
- Modelo atual: [detectado|assumido|nao detectavel]
- Motivo:
- Gatilhos de escalonamento:
- Aprovacao do usuario: [pendente|aprovado|nao aplicavel]
- Mudanca solicitada durante execucao:
```

## Integracao com economia de tokens

Esta regra complementa `rules/token-budget-policy.md` e `rules/token-economy.md`.

Modelo barato sem plano e sem limite de escopo pode ficar caro por retrabalho. Modelo caro sem gatilho objetivo tambem desperdiça custo. A decisao correta combina:

1. Menor modo seguro.
2. Menor conjunto de arquivos e skills.
3. Modelo mais barato capaz de concluir com baixa chance de retry.
4. Escalonamento explicito quando a evidencia muda.
