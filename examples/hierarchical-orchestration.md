# Exemplo: Orquestração Hierárquica — Bug em Migration

> Referência de execução com modo Review e escalonamento.

## Input do usuário

"Adicione coluna `Origin` na tabela KbArticle com migration EF"

## Fase 1 — Entender

- Intenção: schema change + migration
- Escopo: backend database
- Restrição: preservar dados existentes

## Fase 2 — Classificar

- Tipo: `database` (primário), `feature` (secundário)
- Módulos: backend (Domain, Infrastructure)
- Confidence: alta

## Fase 3 — Escolher modo

- Migration → critério Review
- Não é produção/incidente → não Council
- **Modo: Review**

## Fase 4 — Planejar (Working Context criado)

```markdown
### Classificação
- Tipo: database
- Modo: Review
- Risco: Médio (pendente risk-reviewer)

### Escopo
- Módulos: Umbra.Domain, Umbra.Infrastructure
- Arquivos candidatos: KbArticle.cs, UmbraDbContext, migration
```

## Fase 5 — Investigar

- Context Builder: stack .NET 8 + EF Core, padrão migration existente
- Atualiza WC — não relê após database skill

## Fase 6 — Implementar

- database: cria migration
- backend: atualiza entity e DTOs
- WC atualizado com arquivos alterados

## Fase 7 — Validar

- critic:
  - Causa: schema precisa de Origin → resolve causa ✓
  - Solução simples: coluna nullable com default ✓
  - Risco oculto: dados existentes precisam default
  - Veredito: ajustar
- validator:
  - dotnet build: ok
  - migration aplicável: ok
  - Veredito: pronto

## Fase 8 — Entregar

Orchestrator responde ao usuário (único contato):

- Modo: Review
- Skills: context-builder, database, backend, critic, validator
- Working Context descartado

## Contraste: Technical Council

Se o pedido fosse "Migrar KbArticle para multi-tenant com row-level security em produção":

- Critérios: DB + auth + produção + >3 módulos
- **Modo: Technical Council**
- Conselho: database, backend, software-architect, security-review, qa
- Usuário vê só decisão consolidada — não as 6 opiniões individuais
