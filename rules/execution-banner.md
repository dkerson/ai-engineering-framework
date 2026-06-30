# Execution Banner

> Finalidade: padronizar a mensagem inicial quando o framework assumir uma task executavel.

## Quando exibir

Exibir antes de investigar, editar, executar comandos ou validar uma task.

O banner e parte do gate bloqueante definido em `rules/pre-execution-gate.md`. Depois de exibir o banner, o Orchestrator deve parar ate receber aprovacao explicita.

Pode ser omitido apenas em pergunta/resposta Fast Path sem leitura ampla, comando, edicao ou validacao.

## Template obrigatorio

```markdown
Executando tarefa com AI Engineering Framework.

- Superficie detectada: [Cursor | Codex | Desconhecida]
- Confianca da deteccao: [alta | media | baixa]
- Modelo atual: [detectado | assumido | nao detectavel pelo framework]
- Modelo recomendado: [...]
- Motivo do modelo: [...]
- Modo de execucao: [Fast | Standard | Review | Technical Council]

## Plano de execucao
1. ...
2. ...

Posso seguir com este plano?
```

## Condicao de parada

A resposta do usuario que originou a task nao aprova este banner. A aprovacao precisa vir depois da exibicao do plano.

Se o usuario ainda nao aprovou:

- nao investigar;
- nao executar comandos;
- nao editar arquivos;
- nao validar;
- nao iniciar dev server;
- nao acionar ferramentas externas para implementar.

## Regras de linguagem por superficie

### Cursor

Use termos como:

- `Composer 2.5 Standard`
- `Auto`
- model picker do Cursor
- Cursor Rules

Se precisar trocar modelo:

```text
Por favor altere o modelo no Cursor para [modelo] e me avise quando estiver pronto para continuar.
```

### Codex

Use termos como:

- `gpt-5.4-mini`
- `gpt-5.5`
- `gpt-5.3-codex-spark`, se disponivel
- `/model`
- `config.toml`
- seletor da IDE Codex
- `codex -m`

Se precisar trocar modelo:

```text
Por favor altere o modelo no Codex para [modelo] usando /model, seletor da IDE ou config.toml conforme sua superficie, e me avise quando estiver pronto para continuar.
```

### Desconhecida

Use linguagem neutra:

```text
Modelo atual: nao detectavel pelo framework.
Modelo recomendado:
- Cursor: [...]
- Codex: [...]
```

## Nao prometer controle de UI

O banner nao deve afirmar que o framework alterou modelo no Cursor ou Codex. Ele recomenda, justifica e aguarda confirmacao quando a troca for necessaria.
