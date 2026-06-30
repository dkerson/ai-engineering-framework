# Surface Routing Policy

> Finalidade: identificar se a execucao esta acontecendo em Cursor, Codex ou superficie desconhecida antes de recomendar modelo, mensagem e acao do usuario.

## Principio central

O framework deve separar a superficie de execucao do tipo de tarefa. A mesma task pode exigir mensagens e modelos diferentes em Cursor e Codex.

Nunca afirmar que a superficie foi detectada com alta confianca sem evidencia objetiva.

## Superficies suportadas

| Superficie | Como tratar |
|------------|-------------|
| Cursor | Usar linguagem de Cursor: model picker, Composer, Auto, Cursor Rules, `.cursor/` |
| Codex | Usar linguagem de Codex: `config.toml`, `/model`, seletor IDE, `codex -m`, Codex app/CLI/IDE |
| Desconhecida | Usar linguagem neutra e pedir confirmacao somente se a diferenca bloquear modelo ou acao |

## Sinais de deteccao

### Codex - alta confianca

- Contexto da sessao informa Codex desktop/app/CLI/IDE.
- Ferramentas Codex estao disponiveis no ambiente atual.
- Variavel `CODEX_HOME` existe.
- Arquivo `.codex/config.toml` ou `$CODEX_HOME/config.toml` define contexto ativo relevante.
- Usuario diz explicitamente que esta usando Codex.

### Cursor - alta confianca

- Usuario diz explicitamente que esta usando Cursor.
- Pedido menciona model picker, Composer, Auto do Cursor ou Cursor Rules como superficie ativa.
- Arquivos `.cursor/rules` ou configuracao Cursor sao o alvo direto da task.

### Media confianca

- Projeto possui `.codex/`, mas a sessao atual nao prova Codex.
- Projeto possui `.cursor/`, mas a sessao atual nao prova Cursor.
- `AGENTS.md` menciona Codex/Cursor, mas isso e compatibilidade, nao superficie ativa.

### Baixa confianca

- Apenas existe `AGENTS.md`.
- Apenas o framework cita Cursor/Codex.
- O usuario nao mencionou ferramenta e nao ha sinais de ambiente.

## Resultado obrigatorio

Registrar no Working Context:

```markdown
### Surface Routing
- Superficie detectada: [Cursor|Codex|Desconhecida]
- Confianca: [alta|media|baixa]
- Evidencias:
- Mensagem de modelo deve usar:
- Modelo atual detectavel: [sim|nao|parcial]
```

## Modelo atual

O framework pode detectar modelo atual somente quando houver evidencia confiavel em configuracao, comando ou contexto exposto.

Nao detectar como fato:

- modelo selecionado visualmente no Cursor;
- modelo selecionado temporariamente por UI sem API/contexto acessivel;
- modelo assumido por historico da conversa.

Quando nao houver evidencia, escrever:

```text
Modelo atual: nao detectavel pelo framework.
```

## Fallback

Se a superficie for desconhecida:

1. Exibir banner neutro.
2. Recomendar modelo em formato dividido: Cursor e Codex.
3. Perguntar qual superficie o usuario esta usando somente se a escolha do modelo ou a acao de troca for necessaria antes de continuar.

## Integracao

Aplicar antes de `rules/model-routing.md` e `rules/execution-banner.md`.
