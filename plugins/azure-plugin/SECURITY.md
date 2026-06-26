# Security — Azure Plugin

## Access Mode

read-write

## Risk Level

high

## Destructive Actions (require explicit approval)

- deploy
- delete resource
- alterar permissao
- alterar Entra ID

## Prohibited

- Armazenar secrets no repositorio
- Executar acoes write/admin sem aprovacao quando destrutivas
- Bypass do Plugin Resolver ou Security Policy Check
