# Model Routing Policy

> Finalidade: recomendar o modelo Cursor/Codex com melhor custo-beneficio antes da execucao e controlar escalonamento quando a missao exigir mais capacidade.

## Principio central

O framework nao altera automaticamente o seletor de modelo do Cursor. O Orchestrator deve recomendar o modelo, justificar a escolha e pausar quando uma troca manual for necessaria.

## Modelo padrao recomendado

Use `Composer 2.5 Standard` como recomendacao padrao quando o objetivo principal for economia de custo.

Use `Auto` ou modelo mais forte somente quando o risco, a ambiguidade ou a chance de retrabalho justificar o custo adicional.

## Recomendacao obrigatoria no plano

Antes de executar qualquer task, o Orchestrator deve apresentar:

```markdown
## Plano de execucao
1. ...
2. ...

## Modelo recomendado
- Modelo: [Composer 2.5 Standard | Auto | modelo forte especifico]
- Motivo: [custo, risco, complexidade, velocidade ou confiabilidade]
- Escalonamento previsto: [quando mudar de modelo durante a execucao]

Posso seguir com este plano?
```

A execucao so continua apos aprovacao explicita do usuario, exceto em pedidos que sejam apenas pergunta/resposta e nao envolvam leitura ampla, comandos, edicao ou validacao.

## Matriz de escolha

| Cenario | Modelo recomendado |
|---------|--------------------|
| Pergunta, explicacao, documentacao simples | Composer 2.5 Standard |
| Fast Path, ajuste localizado, label, copy, CSS simples | Composer 2.5 Standard |
| Analise inicial de bug ou feature pequena | Composer 2.5 Standard |
| Frontend simples ou componente isolado | Composer 2.5 Standard |
| Backend simples, DTO, controller ou service localizado | Composer 2.5 Standard |
| Auth, autorizacao, permissoes, tenants, claims | Auto |
| Banco, migration, query critica, dados financeiros/fiscais | Auto |
| Integracao externa, webhook, pagamento, SEFAZ, marketplace | Auto |
| Deploy, producao, incidente, Docker/infra critica | Auto |
| Refatoracao multi-modulo ou arquitetura | Auto |
| 2 falhas com a mesma hipotese ou causa incerta | Auto |
| Latencia humana mais importante que custo | Auto ou modo rapido explicitamente justificado |

## Escalonamento durante a execucao

Se durante a task surgir um gatilho de escalonamento, o Orchestrator deve parar antes da proxima acao de risco e avisar:

```markdown
Identifiquei necessidade de trocar o modelo.

- Modelo atual assumido: [modelo informado/assumido]
- Modelo recomendado agora: [Auto | modelo forte]
- Motivo: [risco/ambiguidade/retry/contexto]
- Proxima acao apos a troca: [...]

Por favor altere o modelo no Cursor para o recomendado e me avise quando estiver pronto para continuar.
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
- Modelo recomendado:
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
