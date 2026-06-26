# Database

> Finalidade: Boas práticas de banco de dados.

## Regras

- Migrations reversíveis (up/down)
- Índices em colunas de filtro/join frequentes
- Evitar SELECT * em produção
- Transações para operações multi-step
- Naming: snake_case ou PascalCase conforme ORM
