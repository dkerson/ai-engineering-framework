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
- Tipo: [bug|feature|data|hybrid|...]
- Mission Type: [Development|Growth|Modernization|Dashboard|...]
- Mission Mode: [Analysis|Planning|Implementation|Validation|Continuous Improvement|Innovation|Emergency|Learning]
- Modo: [Fast|Standard|Review|Technical Council]
- Risco: [Muito Baixo|Baixo|Médio|Alto|Crítico]
- Domínios: [Development|Data Intelligence|Business/Operations|QA/Validation]
- Growth & Brand: [sim/não]
- Knowledge Hub: [areas consultadas]
- Product Excellence: [sim/não]
- Infrastructure Intelligence: [sim/não]
- Hybrid Flow: [sim/não]

### Mission Memory (quando aplicável)
- Objetivo principal:
- Objetivos secundários:
- Mission Score:
  - Valor esperado:
  - Complexidade:
  - Esforço:
  - Impacto:
  - Prazo estimado:
  - Confiança:
  - Risco:
- Decisões:
- Hipóteses:
- Roadmap:
- Quick wins:
- Validações:
- Backlog sugerido:

### Escopo
- Módulos afetados: [...]
- Arquivos candidatos: [...]

### Data Intelligence (quando aplicável)
- Objetivo da task:
- Regra de negócio:
- Tabelas envolvidas:
- Views envolvidas:
- Procedures envolvidas:
- APIs envolvidas:
- Telas/relatórios envolvidos:
- Filtros aplicados:
- Período analisado:
- Chaves de relacionamento:
- Riscos de duplicidade:
- Riscos de cardinalidade:
- Regras de agregação:
- Validações executadas:
- Divergências encontradas:

### Growth & Brand Intelligence (quando aplicável)
- Objetivo de comunicação:
- Público-alvo:
- Tom de voz:
- Posicionamento:
- Estrutura de página/conteúdo:
- Copy principal:
- Assets existentes:
- Tipo de asset recomendado:
- SEO/metadados:
- Prova social:
- Riscos de marca/conversão:
- Notas Product Audit:

### Product Excellence / Evolution (quando aplicável)
- Modo visual: [Legacy|Hybrid|Greenfield|Automatic]
- Knowledge Hub consultado:
- Benchmark usado:
- Dimensões avaliadas:
- Categorias abaixo de 8:
- Quick wins:
- Curto prazo:
- Médio prazo:
- Estratégico:
- Impacto/esforço/prioridade:

### Infrastructure Intelligence (quando aplicável)
- Projeto:
- Ambiente:
- Repositorio:
- Banco:
- Servico:
- API:
- Fila:
- Storage:
- Cloud/provider:
- MCP:
- Variaveis de ambiente:
- Secret reference:
- Registry atualizado:
- Credenciais reais ausentes: [sim/não]

### Descobertas
- [skill]: [bullet resumido]

### Decisões
- [decisão consolidada]

### Plano
- [etapas do hybrid-flow-planner / implementation-planner / data-orchestrator]

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
| Popular seção Data Intelligence em demandas de dados/BI | Inventar regras de negócio |

## Quando pular leitura

Se o Working Context já contém análise de um arquivo, a skill seguinte **deve** reutilizar — não abrir o arquivo novamente, exceto se a implementação exigir edição.

Para SQL: seguir ordem em `rules/data/query-performance.md`.

## Integração

- Strategic Intelligence Layer: gera Mission Brief e Mission Memory; não implementa
- Orchestrator: cria e consolida
- hybrid-flow-planner / data-orchestrator: plano e domínios
- Context Builder: popula escopo e stack
- Skills técnicas: adicionam descobertas e arquivos alterados
- business-rule-mapper / semantic-layer-specialist: regras e mapeamentos
- data-validator: validações e divergências
- Critic / Risk Reviewer: adicionam riscos
- cross-domain-decision-maker / decision-maker: decisões
- Implementation Planner: adiciona plano
- Validator: marca validações concluídas
