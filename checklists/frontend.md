# Checklist: Frontend

## Anti-hardcode

- [ ] Sem hardcode de URL, permissao, menu, status ou regra variavel
- [ ] Valores variaveis vindos de API/config/contexto apropriado

## Runtime e regressao

- [ ] Porta/URL corretas confirmadas
- [ ] Cache/bundle coerente com a alteracao
- [ ] Console sem erro novo relevante
- [ ] Network sem erro novo relacionado
- [ ] Rota alvo validada por DOM ou screenshot
- [ ] Rotas canario validadas quando arquivo compartilhado mudou

> Finalidade: validação para tarefas tipo `frontend`.

- [ ] Loading/error/empty states
- [ ] Responsivo
- [ ] A11y básica
- [ ] Tipagem correta
- [ ] Sem console.log
- [ ] Mensagens pt-BR
