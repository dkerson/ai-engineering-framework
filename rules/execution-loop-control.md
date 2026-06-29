# Execution Loop Control

> Finalidade: impedir que execucoes longas repitam a mesma hipotese, o mesmo teste ou a mesma correcao sem evidencia nova.

## Principio central

Toda tentativa precisa mudar uma variavel relevante ou produzir evidencia nova. Repetir a mesma acao com o mesmo contexto nao e progresso.

## Attempt Ledger obrigatorio

Em bugs, frontend runtime, validacoes falhando ou qualquer execucao com mais de uma tentativa, o Orchestrator deve manter no Working Context:

```markdown
### Attempt Ledger
- Attempt #:
- Hypothesis:
- Changed files:
- Validation command:
- Result:
- Evidence:
- Same as previous attempt: yes/no
- Decision: continue | change hypothesis | escalate | ask user | stop
```

## Limites de tentativa

| Condicao | Acao obrigatoria |
|----------|------------------|
| 1 falha | Registrar evidencia e ajustar a proxima acao. |
| 2 falhas com a mesma hipotese | Invalidar a hipotese ate surgir evidencia nova. |
| 2 falhas sem causa raiz | Voltar para diagnostico, nao aplicar novo patch. |
| 3 tentativas totais sem progresso | Escalar modo, pedir evidencia externa ou parar com diagnostico claro. |
| Mesmo comando/teste repetido sem mudanca | Proibido; primeiro alterar variavel, ambiente ou hipotese. |

## Loop breaker

Antes da proxima tentativa, responder internamente:

1. O que mudou desde a tentativa anterior?
2. Que evidencia prova que esta nova tentativa e diferente?
3. Qual hipotese foi descartada?
4. Qual criterio encerra a investigacao?

Se essas perguntas nao tiverem resposta objetiva, parar e replanejar.

## Integracao com Context Hygiene

Quando houver repeticao, ruido ou conflito, avaliar `rules/context-hygiene.md`.

Se o contexto estiver `Polluted`, criar `Compacted Snapshot` antes de continuar. O snapshot deve preservar somente a hipotese ativa, hipoteses descartadas, evidencias e proxima acao.

## Anti-padroes bloqueados

- "Tentar de novo" sem mudanca de codigo, ambiente, cache ou dados.
- Trocar porta e declarar sucesso sem explicar por que a porta anterior falhava.
- Aplicar patches cumulativos sem causa raiz.
- Rodar build/testes longos varias vezes sem ler o erro mais recente.
- Reabrir arquivos ja analisados sem nova pergunta especifica.

## Quando escalar

Escalar de Standard para Review quando:

- a causa raiz permanece incerta apos 2 tentativas;
- o fix toca arquivo compartilhado ou contrato entre telas;
- validacao aponta regressao fora da tela alvo;
- dev server, cache, proxy ou roteamento estao envolvidos.

Escalar para Technical Council somente se houver arquitetura, producao, >3 modulos, auth, banco, pagamentos ou incidente critico.
