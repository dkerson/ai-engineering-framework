# Checklist — NLME Mission

## Antes de executar

- [ ] mission-translator produziu Translation Brief
- [ ] Goal Recognition registrou objetivo real
- [ ] mission-builder produziu Mission Package
- [ ] Mission Confidence calculado
- [ ] prompt-builder produziu Structured Prompt (interno)
- [ ] SIL produziu Mission Brief
- [ ] capability-resolver consultado se aplicável
- [ ] Primeira resposta (`nlme-first-response`) apresentada ao usuário
- [ ] Perguntas ≤ 3 e só se confidence < threshold

## Durante execução

- [ ] Orchestrator mantém monopólio de comunicação
- [ ] Modo operacional mínimo seguro
- [ ] Working Context atualizado
- [ ] Token economy respeitada

## Ao encerrar

- [ ] Mission Report / final-response
- [ ] Mission Memory registrada (FOS)
- [ ] Continuous Evolution backlog se aplicável
