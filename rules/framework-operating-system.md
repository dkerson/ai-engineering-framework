# Framework Operating System

## Governance Policy

Nenhuma melhoria pode ser implementada automaticamente.

Fluxo obrigatorio:

1. Registrar
2. Recomendar
3. Aguardar aprovacao do usuario
4. Implementar somente apos aprovacao
5. Atualizar documentacao
6. Atualizar versao
7. Atualizar historico

## FOS Nunca

- Executa codigo
- Implementa features
- Altera arquivos sem aprovacao
- Remove skills
- Apaga historico

## Continuous Evolution

Ao terminar uma mission, registrar quando aplicavel:

- Learning
- Patterns
- Anti-patterns
- Metrics
- Retrospective
- Recommendations
- Health
- Roadmap
- Backlog
- Pattern Extraction

## Execution Intelligence

O framework pode observar cada execucao, mas nao pode se modificar sozinho.

Registrar de forma leve:

- `framework/operating-system/MISSION_LEDGER.md` - resumo da mission.
- `framework/operating-system/SKILL_USAGE.md` - skills usadas de verdade.
- `framework/operating-system/TOKEN_METRICS.md` - sinais de desperdicio/economia.
- `framework/operating-system/EXECUTION_METRICS.md` - baseline, actual units, savings %, retries e errors avoided.
- `framework/operating-system/LEARNING.md` - aprendizados reutilizaveis observados.
- `framework/operating-system/PATTERNS.md` - abordagens repetidas com resultado positivo.
- `framework/operating-system/ANTI_PATTERNS.md` - caminhos repetidos que causaram erro, retrabalho ou desperdicio.
- `framework/operating-system/RECOMMENDATIONS.md` - mudancas propostas, aguardando aprovacao quando alterarem comportamento.
- `framework/operating-system/PROMOTION_CRITERIA.md` - limiares para promover aprendizados.

Regras:

1. Registrar somente metadados curtos.
2. Nunca salvar segredos, prompts completos, codigo longo ou dados privados.
3. Nunca implementar mudancas a partir de metricas sem aprovacao do usuario.
4. Promover padroes somente com evidencia repetida.
5. Preferir aproximacao barata a medicao perfeita e cara.

## Execution Learning Loop

Usar `rules/execution-learning-loop.md` quando uma execucao revelar aprendizado reutilizavel.

Estados permitidos:

| Status | Significado |
|--------|-------------|
| observed | Sinal capturado uma vez; ainda nao muda comportamento |
| recommended | Ha proposta clara para regra, checklist, workflow ou capability |
| approved | Usuario aprovou implementar a mudanca |
| implemented | Mudanca aplicada, validada e documentada |
| rejected | Proposta recusada ou supersedida |

Uma missao pode registrar aprendizado sem virar versao nova. Uma mudanca em regra, checklist, workflow, capability ou bootstrap deve atualizar changelog/status quando for release-worthy.
