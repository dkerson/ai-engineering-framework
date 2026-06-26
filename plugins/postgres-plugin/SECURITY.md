# Security — PostgreSQL Plugin

## Access Mode

read-write

## Risk Level

high

## Destructive Actions (require explicit approval)

- migration
- delete
- update em massa
- drop

## Prohibited

- Armazenar secrets no repositorio
- Executar acoes write/admin sem aprovacao quando destrutivas
- Bypass do Plugin Resolver ou Security Policy Check
