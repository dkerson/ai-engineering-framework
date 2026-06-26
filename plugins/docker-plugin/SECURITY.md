# Security — Docker Plugin

## Access Mode

read-write

## Risk Level

high

## Destructive Actions (require explicit approval)

- deploy
- delete container
- push image
- alterar compose em producao

## Prohibited

- Armazenar secrets no repositorio
- Executar acoes write/admin sem aprovacao quando destrutivas
- Bypass do Plugin Resolver ou Security Policy Check
