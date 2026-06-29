# Configuration & Hardcode Governance

> Governanca para evitar valores fixos que deveriam ser parametrizados por banco, configuracao, ambiente, feature flag, registry ou constantes de dominio justificadas.

## Objetivo

Evitar que regras de produto, autorizacao, ambiente e operacao fiquem escondidas no codigo, tornando futuras mudancas caras e arriscadas.

## O que o framework passa a detectar

- Modulos, menus e permissoes fixos em seed.
- Roles, scopes e tenants hardcoded.
- URLs, endpoints, hosts e portas fixas.
- IDs de cliente, usuario, empresa ou perfil.
- Status, categorias e tipos em strings soltas.
- Numeros magicos para ordem, limite, prazo ou threshold.
- Seeds sem idempotencia.

## Exemplo real de risco

```csharp
new PortalModule("rh", "RH", 10)
new PortalModule("legal", "Juridico", 20)
new Permission { Code = $"{m.Code}.read" }
new Permission { Code = $"{m.Code}.manage" }
```

Esse padrao define estrutura de produto e autorizacao no codigo. A recomendacao e mover a fonte para banco/configuracao ou manter apenas defaults idempotentes que possam ser sobrescritos.

## Artefatos

| Artefato | Papel |
|----------|-------|
| `rules/no-hardcode.md` | Politica anti-hardcode e classificacao |
| `checklists/no-hardcode.md` | Checklist de review |
| `skills/hardcode-scanner/SKILL.md` | Skill de scan e classificacao |
| `workflows/hardcode-audit.md` | Fluxo de auditoria e correcao |

## Como usar em projetos

1. Pedir scan por escopo: projeto inteiro, modulo, pasta ou diff.
2. O Orchestrator invoca `hardcode-scanner`.
3. O scanner usa `rg` com padroes dirigidos.
4. Achados sao classificados por risco e destino recomendado.
5. Correcoes sao feitas apenas quando aprovadas ou quando a tarefa pede explicitamente.

## Resultado esperado

Cada achado deve responder:

- onde esta;
- por que e hardcode;
- se e falso positivo;
- qual risco;
- qual destino recomendado;
- como corrigir com menor impacto.
