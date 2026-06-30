# Pre-Execution Gate

> Finalidade: impedir que o framework comece uma task executavel antes de exibir plano, recomendar modelo e receber aprovacao explicita do usuario.

## Principio central

Toda task executavel tem um ponto de parada obrigatorio antes da primeira acao de execucao. O Orchestrator pode entender, classificar, escolher modo e montar o plano minimo; depois disso deve exibir o banner e aguardar aprovacao.

Esta regra transforma `rules/model-routing.md` e `rules/execution-banner.md` em um gate bloqueante, nao apenas em uma mensagem informativa.

## O que conta como task executavel

Considere executavel qualquer pedido que envolva ao menos uma destas acoes:

- leitura ampla de arquivos, busca no projeto ou investigacao com comandos;
- execucao de shell, scripts, testes, build, lint, dev server ou validacao;
- edicao, criacao, delecao, renomeacao ou movimentacao de arquivos;
- alteracao de configuracao, dependencias, banco, infra, MCP, plugin ou capability;
- navegacao/validacao de frontend, screenshots, console, network ou DOM;
- consulta a servico externo quando usada para decidir implementacao;
- qualquer acao com efeito persistente ou risco de regressao.

## Excecao Fast Path

O gate pode ser omitido somente quando todas as condicoes forem verdadeiras:

1. o pedido e pergunta/resposta, confirmacao, status ou explicacao curta;
2. nao exige leitura ampla, comandos, edicao, validacao ou acesso externo;
3. nao altera arquivos nem comportamento do projeto;
4. nao ha risco relevante de auth, banco, seguranca, producao, arquitetura ou dados sensiveis.

Leitura dirigida de um unico arquivo/regra pode ocorrer no Fast Path apenas para responder uma duvida sobre o proprio framework, desde que nao vire investigacao ampla.

## Sequencia obrigatoria

Antes da primeira acao executavel:

1. detectar superficie conforme `rules/surface-routing.md`;
2. classificar tipo, dominio e modo;
3. aplicar `rules/model-routing.md`;
4. criar plano curto e verificavel;
5. exibir `rules/execution-banner.md`;
6. perguntar `Posso seguir com este plano?`;
7. parar a execucao ate aprovacao explicita.

## Aprovacao explicita

Conta como aprovacao:

- "pode executar";
- "pode seguir";
- "aprovado";
- "sim, execute";
- outra frase inequivoca enviada depois do plano e banner.

Nao conta como aprovacao:

- o pedido inicial de executar a tarefa;
- "faz isso", "faz essa reestruturacao", "corrige" ou equivalente antes do plano;
- silencio, continuacao automatica ou ausencia de objecao;
- aprovacao para uma ideia anterior quando o plano atual ainda nao foi exibido;
- aprovacao implicita por urgencia.

## Gate Record no Working Context

Registrar em toda task executavel:

```markdown
### Pre-Execution Gate
- Task executavel: [sim|nao]
- Excecao Fast Path: [sim|nao + motivo]
- Banner exibido: [sim|nao]
- Plano apresentado: [sim|nao]
- Modelo recomendado: [sim|nao]
- Pergunta de aprovacao: [sim|nao]
- Aprovacao explicita recebida: [pendente|sim|nao aplicavel]
- Frase de aprovacao:
- Primeira acao executavel permitida: [sim|nao]
```

## Stop condition

Se `Aprovacao explicita recebida` estiver `pendente`, o Orchestrator deve parar. Nao investigar, nao rodar comando, nao editar e nao validar.

Se perceber que executou sem gate, deve interromper imediatamente, informar o desvio, exibir o plano correto e pedir aprovacao antes de continuar.

## Relacao com troca de modelo

Se surgir gatilho de escalonamento durante a execucao, aplicar novamente o gate em modo reduzido:

1. explicar modelo atual assumido e modelo recomendado;
2. dizer por que a troca e necessaria;
3. informar a proxima acao;
4. aguardar o usuario confirmar a troca/manual ou autorizar continuar sem troca.
