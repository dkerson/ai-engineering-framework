# Workflow: Plugin Mission

> Cadastrar, ativar, desativar, listar, validar ou criar plugins.

## Trigger

Cadastre plugin, ative plugin, desative plugin, liste plugins, crie plugin para {serviço}, quais plugins, permissão de escrita, risco alto.

## Pipeline

```text
Plugin Mission
-> Project Resolver* (se por projeto)
-> Plugin Builder* (se criar novo)
-> Plugin Manager (cadastro/lista/ativa/desativa/valida)
-> Plugin Resolver* (se consulta de uso em missão)
-> Registry Update
-> Project Registry Update* (PROJECT_PLUGINS.md)
-> Plugin Health
-> FOS Update
```

`*` Quando necessário.

## Modo sugerido

| Cenário | Modo |
|---------|------|
| Listar, consultar | Fast |
| Ativar, desativar, cadastrar | Standard |
| Criar plugin, alterar permissões | Standard → Review se risco |

## Skills

`project-resolver`, `plugin-builder`, `plugin-manager`, `plugin-resolver`, `security-review`, `risk-reviewer`, `validator`

## Regras

- Nunca armazenar secrets.
- Toda mudança de status → FOS.
- Plugins draft não executam integração real.
- Ações destrutivas exigem aprovação explícita.

## Referências

- `docs/PLUGIN_ARCHITECTURE.md`
- `plugins/PLUGIN_POLICY.md`
- `plugins/PLUGIN_REGISTRY.md`
