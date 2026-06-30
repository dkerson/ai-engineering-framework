# Processo Universal



> Finalidade: fases obrigatórias em toda execução do Personal AI Framework.



## Fases



### 1. Entender

- Extrair intenção, escopo, restrições

- Identificar tipo(s) de demanda

- Confirmar ambiguidades críticas (perguntar só se bloqueante)



### 2. Classificar

- Mapear para tipo(s) de demanda (`workflows/_index.md`)

- Estimar módulos e arquivos afetados (sem ler ainda)

- Confidence: alta/média/baixa



### 3. Escolher modo

- Fast / Standard / Review / Technical Council

- Avaliar critérios do conselho (`workflows/technical-council.md`)

- Risk Reviewer se dúvida sobre risco

- Detalhes: `workflows/modes.md`



### 4. Planejar

- Criar Working Context (`context/working-context.md`)

- Selecionar pipeline mínimo para o modo

- Aplicar `rules/model-routing.md`: recomendar modelo, justificar custo/risco e definir gatilhos de escalonamento

- Technical Council: montar conselho + Decision Maker + Implementation Planner

- Listar skills e ordem (máx. 10 passos visíveis)

- Apresentar plano + modelo recomendado ao usuario e perguntar "Posso seguir com este plano?"

- Aguardar aprovacao explicita antes de investigar, editar, executar comandos ou validar, exceto pergunta/resposta Fast Path sem leitura ampla, comando, edicao ou validacao



### 5. Investigar

- Aplicar `rules/token-economy.md`

- Localizar erro/stack/arquivo antes de leitura ampla

- Context Builder se contexto insuficiente

- Atualizar Working Context — não reler arquivos

- Avaliar Context Health; se poluido, criar Compacted Snapshot antes de seguir



### 6. Implementar

- Menor alteração possível

- Seguir plano do Implementation Planner (se existir)

- Seguir rules: clean-code, naming, security conforme área



### 7. Validar

- **Standard:** QA

- **Review/Council:** Critic + Validator

- Antes de validacao ampla, confirmar que o Working Context ou Compacted Snapshot contem plano ativo, arquivos alterados e pendencias reais

- Checklist do tipo (`checklists/`)

- Build completo só se Validator exigir



### 8. Revisar

- Critic em Review/Council

- Code-review se alteração significativa

- Security review se auth/dados sensíveis



### 9. Entregar

- Orchestrator consolida (Technical Council: só decisão, não opiniões brutas)

- `templates/final-response.md`

- Artefatos gerados (specs, ADRs, etc.)

- **Descartar Working Context**



## Regras transversais



Aplicar em todas as fases:

- `rules/hierarchical-orchestration.md`

- `rules/token-economy.md`

- `rules/model-routing.md`

- `rules/context-hygiene.md`

- Rules específicas conforme área (ver `rules/`)

