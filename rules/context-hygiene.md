# Context Hygiene Protocol

> Finalidade: manter a janela de trabalho utilizavel durante missoes longas, removendo ruido operacional sem perder decisoes, evidencias e proximos passos.

## Principio central

O Orchestrator deve avaliar se o contexto ativo continua limpo o bastante para guiar a execucao. Quando houver poluicao, ele cria um **Compacted Snapshot** no Working Context e passa a trabalhar a partir dele.

Este protocolo nao apaga tecnicamente o historico da ferramenta. Ele define qual parte do historico permanece operacionalmente relevante.

## Responsavel

Somente o **Orchestrator** decide quando compactar contexto.

Skills podem sinalizar poluicao, mas nao compactam por conta propria.

## Gatilhos obrigatorios

Avaliar higiene de contexto:

1. Apos investigacao longa ou com muitos arquivos.
2. Antes de implementar quando houve mudanca de plano.
3. Antes de validar quando a missao acumulou muitos achados.
4. Antes de escalar para Review ou Technical Council.
5. Quando uma skill sinalizar repeticao, ruido ou conflito.
6. Quando o output de ferramentas ficar maior que o necessario para a proxima decisao.

## Sinais de contexto poluido

- Objetivo atual misturado com hipoteses antigas.
- Mais de um plano concorrente sem decisao consolidada.
- Outputs longos ja resumidos no Working Context.
- Arquivos lidos sem relacao com o proximo passo.
- Mesma evidencia repetida por multiplas skills.
- Decisoes antigas contradizem a decisao mais recente.
- Validacoes passadas aparecem como pendentes.
- Conversa exploratoria atrapalha a acao imediata.

## O que preservar

O Compacted Snapshot deve manter apenas:

- Objetivo real da missao.
- Modo, risco, dominios e restricoes do usuario.
- Decisoes consolidadas.
- Hipoteses ainda abertas.
- Arquivos lidos, alterados ou candidatos relevantes.
- Evidencias importantes com caminho/linha quando existir.
- Plano ativo e proximo passo.
- Validacoes executadas e pendentes.
- Riscos, bloqueios e perguntas realmente abertas.

## O que descartar operacionalmente

- Outputs brutos de comandos ja resumidos.
- Planos substituidos.
- Hipoteses invalidadas.
- Arquivos investigados e descartados.
- Trechos grandes de codigo ja referenciados por arquivo/linha.
- Debates internos de skills apos decisao consolidada.
- Repeticoes de regras ja aplicadas.
- Conversa sem impacto na execucao.

## Status de saude

| Status | Significado | Acao |
|--------|-------------|------|
| Clean | Contexto curto, coerente e acionavel. | Continuar. |
| Growing | Contexto util, mas com acumulo perceptivel. | Resumir achados novos em bullets. |
| Polluted | Ruido pode afetar decisao ou custo. | Criar Compacted Snapshot antes de continuar. |

## Formato minimo

```markdown
### Context Health
- Status: Clean | Growing | Polluted
- Pollution signals:
- Last hygiene check:
- Active context source: Full | Compacted Snapshot

### Compacted Snapshot
- Objective:
- Current mode/risk:
- User constraints:
- Decisions:
- Relevant files:
- Preserved evidence:
- Open hypotheses:
- Active plan:
- Validation state:
- Next action:
- Risks/blockers:
- Dropped noise:
```

## Regras de uso

- Compactar antes de continuar quando o status for `Polluted`.
- Nao perder decisao recente em favor de contexto antigo.
- Nao copiar codigo longo para o snapshot.
- Nao registrar dados privados, secrets ou prompts completos.
- Se uma informacao nao orienta decisao, implementacao ou validacao, ela nao entra no snapshot.
- A resposta final pode mencionar a compactacao apenas quando isso ajudar o usuario a entender custo, risco ou continuidade.

## Integracao com Execution Intelligence

Registrar em `TOKEN_METRICS.md` somente quando houver sinal util:

- contexto compactado por poluicao real;
- releitura evitada por snapshot;
- ruido causado por output excessivo;
- perda de eficiencia por falta de snapshot anterior.
