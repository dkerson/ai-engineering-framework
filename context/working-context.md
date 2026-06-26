# Working Context — Memória Temporária de Execução

> Finalidade: contexto compartilhado durante uma tarefa. **Descartado ao finalizar.**

## Responsável

O **Orchestrator** cria, mantém e descarta o Working Context.

## Ciclo de vida

```
Início da tarefa → Orchestrator cria WC
       ↓
Skills adicionam descobertas (sem reler)
       ↓
Tarefa concluída → WC descartado
```

## Estrutura sugerida

```markdown
## Working Context — [resumo da tarefa]

### Classificação
- Tipo: [bug|feature|...]
- Modo: [Fast|Standard|Review|Technical Council]
- Risco: [Muito Baixo|Baixo|Médio|Alto|Crítico]

### Escopo
- Módulos afetados: [...]
- Arquivos candidatos: [...]

### Descobertas
- [skill]: [bullet resumido]
- [skill]: [bullet resumido]

### Decisões
- [decisão consolidada]

### Plano
- [etapas do implementation-planner]

### Validações pendentes
- [ ] ...
```

## Regras

| Fazer | Não fazer |
|-------|-----------|
| Adicionar bullets concisos (1–2 linhas) | Colar código inteiro |
| Referenciar `startLine:endLine:path` | Repetir análise de outra skill |
| Indicar arquivos já lidos | Reler arquivo já no WC |
| Atualizar status de validação | Manter WC entre sessões |

## Quando pular leitura

Se o Working Context já contém análise de um arquivo, a skill seguinte **deve** reutilizar — não abrir o arquivo novamente, exceto se a implementação exigir edição.

## Integração

- Orchestrator: cria e consolida
- Context Builder: popula escopo e stack
- Skills técnicas: adicionam descobertas e arquivos alterados
- Critic / Risk Reviewer: adicionam riscos
- Decision Maker: adiciona decisões
- Implementation Planner: adiciona plano
- Validator: marca validações concluídas
