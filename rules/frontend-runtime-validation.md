# Frontend Runtime Validation

> Finalidade: validar telas no runtime correto, evitando falso positivo causado por cache, porta errada, servidor antigo ou navegador com estado obsoleto.

## Principio central

Uma tela so esta validada quando a rota alvo foi aberta no servidor correto, com bundle atualizado, sem erros relevantes de console/network e com evidencia visual ou DOM coerente.

## Descoberta de runtime

Antes de testar frontend:

1. Identificar o comando oficial do projeto (`package.json`, scripts docs ou instrucao do usuario).
2. Verificar se ja existe dev server rodando e qual porta ele usa.
3. Reutilizar a porta existente quando ela pertence ao projeto e responde corretamente.
4. Se abrir nova porta, registrar motivo no Working Context.
5. Registrar URL absoluta validada.

## Cache e estado

Quando a validacao visual/rota divergir do codigo alterado:

- fazer hard reload ou abrir contexto limpo do browser;
- limpar cache do bundler apenas quando houver evidencia de bundle obsoleto;
- reiniciar dev server quando o processo estiver servindo build antigo;
- nao declarar sucesso em outra porta sem comparar contra a porta original.

## Checklist minimo

- [ ] Porta/URL confirmada.
- [ ] Bundle reflete o arquivo alterado.
- [ ] Rota alvo abre sem erro fatal.
- [ ] Console sem erro novo relevante.
- [ ] Network sem 404/500 inesperado relacionado a tela.
- [ ] DOM ou screenshot confirma o comportamento esperado.
- [ ] Se nova porta foi usada, motivo documentado.

## Falso sucesso

Estes sinais nao encerram a tarefa sozinhos:

- "Funcionou em outra porta".
- "Compilou" sem abrir a rota.
- "HTML parece certo no arquivo" sem validar runtime.
- "Nao ha erro terminal" com erro visivel no browser.
- Screenshot de rota diferente da solicitada.

## Quando acionar Regression Boundary

Aplicar `rules/regression-boundary.md` quando a mudanca tocar:

- layout global;
- roteamento;
- providers;
- CSS global;
- componente compartilhado;
- hook compartilhado;
- auth/permissao;
- chamadas API usadas por mais de uma tela.
