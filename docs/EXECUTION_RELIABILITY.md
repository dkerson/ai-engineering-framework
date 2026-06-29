# Execution Reliability

> Dominio operacional para evitar loops, falso sucesso em frontend e regressao colateral durante missoes de implementacao.

## Objetivo

Tornar execucoes Codex/Cursor mais eficientes e sustentaveis quando uma tarefa simples comeca a falhar repetidamente.

## Problemas cobertos

- Tentativas repetidas com a mesma hipotese.
- Execucao longa sem progresso real.
- Frontend validado em porta errada, cache antigo ou dev server divergente.
- Correcao local que quebra telas ou rotas fora de escopo.
- Falta de evidencia objetiva antes de declarar pronto.

## Componentes

| Artefato | Papel |
|----------|-------|
| `rules/execution-loop-control.md` | Attempt Ledger, limite de tentativas e loop breaker |
| `rules/frontend-runtime-validation.md` | Validacao de porta, URL, cache, console, network e DOM/screenshot |
| `rules/regression-boundary.md` | Boundary Map, arquivos compartilhados e canarios de regressao |
| `checklists/frontend-regression.md` | Smoke test minimo para rotas/telas |
| `context/working-context.md` | Campos Attempt Ledger, Regression Boundary e Frontend Runtime |

## Fluxo recomendado

```text
Bug/alteracao frontend
  -> reproduzir
  -> registrar Boundary Map
  -> diagnosticar causa raiz
  -> aplicar fix minimo
  -> validar runtime correto
  -> validar rota alvo
  -> validar canarios se houve compartilhado
  -> entregar com riscos residuais
```

## Loop breaker

Depois de 2 falhas com a mesma hipotese:

1. parar de aplicar patches na mesma direcao;
2. registrar a hipotese como descartada;
3. revisar evidencias novas;
4. trocar estrategia, escalar modo ou pedir informacao externa.

Depois de 3 tentativas totais sem progresso, o Orchestrator deve entregar diagnostico claro ou escalar. Nao deve continuar por horas repetindo comando, porta ou patch sem variavel nova.

## Frontend runtime

Para telas, rotas e HTML, "compilou" nao basta. O framework deve confirmar:

- comando oficial;
- porta/URL;
- cache/bundle;
- console;
- network;
- evidencia visual ou DOM.

Se funcionar apenas em nova porta, a conclusao correta e: existe divergencia de runtime/cache/dev server a explicar.

## Regression Boundary

Antes de alterar artefatos compartilhados, declarar:

- superficie alvo;
- comportamento dentro do escopo;
- telas/rotas fora de escopo;
- arquivos compartilhados;
- rotas/testes canario;
- risco de regressao.

Se tocar layout, router, provider, CSS global, componente base, hook, cliente API, auth ou permissao, a validacao deve ir alem da tela alvo.
