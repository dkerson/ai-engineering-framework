# No Hardcode Governance

> Finalidade: evitar hardcode funcional, operacional e de configuracao que dificulte manutencao, multi-tenant, mudancas de regra e evolucao de produto.

## Principio central

Valor que pode variar por ambiente, cliente, tenant, usuario, plano, operacao, permissao, regra de negocio ou tempo nao deve ficar fixo no codigo. Deve vir de banco, parametro, configuracao, env var, feature flag, registry ou constante de dominio explicitamente justificada.

## Classificacao

| Tipo | Exemplos | Destino recomendado |
|------|----------|---------------------|
| Secret hardcode | tokens, senhas, connection strings, API keys | env/vault/secret manager |
| Environment hardcode | URLs, hosts, portas, paths externos, provider IDs | config/env/registry |
| Domain hardcode | status, tipos, categorias, modulos, departamentos, menus | banco/parametro/enum de dominio |
| Authorization hardcode | roles, permissoes, scopes, tenants, grupos | matriz de permissao/banco/policy |
| Operational hardcode | timeouts, limites, thresholds, paginação, dias, horarios | parametro/config/feature flag |
| Presentation hardcode | labels operacionais, mensagens administrativas, ordem de menu | banco/config/i18n/design system |
| Test/demo hardcode | fixtures, mocks, seeds locais | dados de teste isolados |

## Permitido

- Constantes tecnicas estaveis exigidas por protocolo ou biblioteca.
- Enums de dominio versionados quando o valor faz parte do contrato do sistema.
- Defaults idempotentes para bootstrap, desde que possam ser sobrescritos por banco/configuracao.
- Valores em testes, mocks e fixtures, quando isolados de runtime real.

## Proibido sem justificativa

- IDs fixos de usuario, cliente, tenant, empresa, perfil, role ou modulo.
- URLs externas, endpoints, buckets, filas, topicos e hosts fixos.
- Regras comerciais embutidas em UI ou services sem fonte configuravel.
- Permissoes geradas ou comparadas por strings soltas.
- Seeds com `AddRange` cego para entidades de produto sem upsert/idempotencia.
- Listas de modulos, menus, status ou parametros operacionais fixas no codigo.
- Numeros magicos usados como limite, ordem, prioridade, prazo ou threshold.

## Padrao recomendado

1. Identificar se o valor varia por ambiente, tenant, cliente, regra ou tempo.
2. Escolher fonte de verdade:
   - banco para configuracao administravel;
   - env/config para ambiente e infraestrutura;
   - feature flag para rollout;
   - enum/constante para contrato estavel;
   - seed idempotente apenas para defaults.
3. Nomear a fonte e registrar no Working Context.
4. Validar fallback seguro e comportamento quando ausente.

## Seeds e defaults

Seeds de produto devem ser:

- idempotentes (`upsert`, chave natural, codigo unico);
- seguros para rodar mais de uma vez;
- separados de dados de demo;
- capazes de preservar customizacoes existentes;
- revisados quando criarem modulos, permissoes, menus, parametros ou roles.

Exemplo de risco:

```csharp
new PortalModule("rh", "RH", 10)
new Permission { Code = $"{m.Code}.read" }
```

Classificacao: `Domain hardcode` + `Authorization hardcode`.

Preferir fonte configuravel e seed idempotente:

```csharp
var moduleDefinitions = await moduleDefinitionProvider.GetDefaultsAsync(cancellationToken);
await moduleSeeder.UpsertModulesAsync(moduleDefinitions, cancellationToken);
await permissionSeeder.UpsertDefaultPermissionsAsync(moduleDefinitions, cancellationToken);
```

## Scan em projetos

O scan deve ser dirigido e barato. Usar `rg` primeiro e depois classificar achados.

Quando o pedido envolver modulo, menu, role, permissao, status ou seed, a primeira passada deve focar codigo de runtime: seeders, bootstrap/startup, policies, guards, navegacao, menus e services. Documentacao, migrations e snapshots historicos so entram depois, como contexto ou falso positivo.

Padroes iniciais:

```text
https?://|localhost|127\.0\.0\.1
[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}
password|secret|apiKey|token|connectionString
role|permission|tenant|cliente|empresa|module|menu|status
AddRange|HasData|Seed|Guid\.Parse|new Guid
```

O resultado deve separar:

- achado real;
- falso positivo;
- destino recomendado;
- risco;
- arquivo/linha;
- correcao sugerida.

## Validacao

Antes de concluir:

- conferir que nao houve novo hardcode proibido;
- validar fonte de configuracao escolhida;
- validar fallback quando parametro estiver ausente;
- validar regressao em telas/fluxos consumidores;
- em permissao/modulo/menu, validar matriz de acesso e rotas relacionadas.
