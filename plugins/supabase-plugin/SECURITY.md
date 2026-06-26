# Security — Supabase Plugin

## Access Mode

read-write

## Risk Level

high

## Destructive Actions (require explicit approval)

- migration
- delete row
- alter RLS
- deploy edge function

## Prohibited

- Armazenar secrets no repositorio
- Executar acoes write/admin sem aprovacao quando destrutivas
- Bypass do Plugin Resolver ou Security Policy Check
