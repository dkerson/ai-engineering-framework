# Security — AWS Plugin

## Access Mode

read-write

## Risk Level

high

## Destructive Actions (require explicit approval)

- deploy
- delete bucket
- alterar IAM
- lambda update em producao

## Prohibited

- Armazenar secrets no repositorio
- Executar acoes write/admin sem aprovacao quando destrutivas
- Bypass do Plugin Resolver ou Security Policy Check
