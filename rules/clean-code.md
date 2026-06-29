# Clean Code

## Guardrail anti-hardcode

- Aplicar `rules/no-hardcode.md` para valores variaveis por ambiente, cliente, tenant, usuario, permissao, regra ou tempo.
- Numeros magicos devem virar parametro, constante nomeada ou configuracao justificada.
- Strings de dominio, status, permissao, role, modulo ou menu nao devem ficar soltas no codigo.

> Finalidade: Código legível, funções pequenas, nomes expressivos, DRY sem over-abstraction.

## Regras

- Funções ≤30 linhas quando possível
- Nomes revelam intenção — sem abreviações obscuras
- Um nível de abstração por função
- Evitar comentários que repetem código
- Early return em vez de nesting profundo
- Sem código morto ou comentado
