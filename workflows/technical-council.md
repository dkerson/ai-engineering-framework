# Technical Council — Processo de Decisão

> **Não é uma skill.** Processo convocado exclusivamente pelo Orchestrator no modo **Technical Council**.

## Quando convocar

Somente quando **pelo menos um** critério for verdadeiro:

| Critério | Exemplo |
|----------|---------|
| > 3 módulos afetados | frontend + backend + infra |
| Alteração arquitetural | nova camada, mudança de padrão |
| Autenticação / autorização | Entra ID, roles, policies |
| Banco de dados / migração | EF migration, schema change |
| Integração crítica | pagamento, ERP, API externa sensível |
| Pagamentos | billing, cobrança |
| Performance crítica | gargalo em produção |
| Incidente em produção | downtime, data loss |

Se nenhum critério se aplica → usar modo Review ou Standard com mínimo de skills.

## Fluxo

```
Orchestrator identifica necessidade
        ↓
Monta conselho (somente skills necessárias)
        ↓
Cada skill: diagnóstico · risco · recomendação · validação (máx. 150 palavras)
        ↓
Risk Reviewer classifica risco global
        ↓
Decision Maker consolida e resolve conflitos
        ↓
Implementation Planner gera plano técnico
        ↓
Orchestrator executa plano (skills técnicas)
        ↓
Validator verifica entrega
        ↓
Orchestrator entrega decisão consolidada ao usuário
```

## Montagem do conselho

O Orchestrator convoca **apenas** skills relevantes. Exemplos:

| Cenário | Skills do conselho |
|---------|-------------------|
| Nova API | software-architect, backend, api, database, qa, code-review |
| Migração de banco | database, backend, software-architect, qa, risk-reviewer |
| Incidente produção | bug-hunter, risk-reviewer, backend, devops, deployment |
| Refatoração grande | software-architect, tech-lead, code-review, qa, performance |

Sempre incluir `risk-reviewer` e `decision-maker` em conselhos formais.

## Formato de resposta (cada skill no conselho)

```markdown
**Diagnóstico:** [1–2 frases]
**Riscos:** [nível + detalhe]
**Melhor solução:** [ação concreta]
**Validação:** [o que verificar antes de implementar]
```

**Máximo: 150 palavras por skill.**

## O que o usuário vê

| Mostrar | Ocultar |
|---------|---------|
| Decisão consolidada | Opiniões individuais brutas |
| Plano de implementação | Debate interno do conselho |
| Risco classificado | Respostas completas de cada skill |
| Próximos passos | Working Context interno |

## Após o conselho

1. Orchestrator atualiza Working Context com decisão
2. Implementation Planner produz etapas ordenadas
3. Execução segue modo Review (Critic + Validator no final)
4. Resposta final via `templates/final-response.md`
