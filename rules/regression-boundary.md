# Regression Boundary

> Finalidade: corrigir a tela ou funcao alvo sem quebrar superficies que ja estavam funcionando.

## Principio central

Toda mudanca tem um limite de impacto. O Orchestrator deve declarar esse limite antes de implementar e ampliar a validacao quando tocar artefatos compartilhados.

## Boundary Map

Antes de editar em bug, UI ou feature pequena, registrar no Working Context:

```markdown
### Regression Boundary
- Target surface:
- In-scope behavior:
- Out-of-scope surfaces:
- Shared files touched:
- Canary routes/tests:
- Regression risk: low | medium | high
- Expanded validation required: yes/no
```

## Arquivos que ampliam risco

Se qualquer item abaixo for alterado, a validacao deixa de ser apenas da tela alvo:

- layout/app shell;
- roteador, middleware ou guards;
- provider/context global;
- CSS global, tema, tokens ou reset;
- componente base compartilhado;
- hooks compartilhados;
- cliente API, interceptors ou query keys;
- auth, permissao, feature flags;
- transformacao de dados reutilizada.

## Rotas e testes canario

Para frontend, escolher no minimo:

1. rota alvo;
2. rota irma ou fluxo que usa o mesmo componente/layout;
3. rota base do modulo ou dashboard/home, quando aplicavel.

Para backend/API, escolher:

1. endpoint alvo;
2. consumidor direto;
3. contrato compartilhado, quando aplicavel.

## Regras de implementacao

- Preferir fix local quando o bug e local.
- Evitar mudar componente compartilhado para resolver problema de uma unica tela, salvo quando a causa raiz for compartilhada.
- Se alterar compartilhado, registrar consumidores provaveis e validar canarios.
- Nao refatorar durante bug fix sem necessidade para a causa raiz.

## Criterio de pronto

Uma entrega com arquivo compartilhado alterado so pode ser marcada como pronta quando:

- a rota/funcao alvo passa;
- os canarios definidos passam;
- nenhuma regressao nova foi observada;
- riscos residuais estao claros na resposta final.
