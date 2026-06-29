# Checklist: Frontend Regression

> Finalidade: smoke test minimo para proteger telas funcionando ao corrigir uma rota ou componente.

- [ ] Rota alvo validada no runtime correto
- [ ] URL/porta registradas
- [ ] Console sem erro novo relevante
- [ ] Network sem erro novo relacionado
- [ ] Rota canario do mesmo modulo validada
- [ ] Rota base/home/dashboard validada quando aplicavel
- [ ] Componentes compartilhados revisados quanto a impacto
- [ ] CSS/layout global sem efeito colateral visivel
- [ ] Evidencia visual ou DOM coletada para comportamento esperado
