# Infrastructure Secrets

## Nunca armazenar

- Tokens
- Senhas
- Connection strings
- Certificates
- Private keys
- Secrets
- Credenciais reais

## Sempre usar

- Environment variables
- Secret Managers
- Placeholders
- `.env.example`

## Proibido

- Criar `.env` com valores reais.
- Copiar credenciais para docs.
- Registrar connection strings completas.

## Permitido

- Nome da variavel de ambiente.
- Nome do Secret Manager.
- Escopo da permissao.
- Exemplo placeholder.
