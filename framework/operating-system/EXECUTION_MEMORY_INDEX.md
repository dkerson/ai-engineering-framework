# Execution Memory Index

> Indice curto para recuperar aprendizados operacionais antes de novas execucoes. Nao armazena prompts completos, secrets, codigo longo ou dados privados.

## Como usar

- Consultar antes de tasks nao triviais.
- Procurar por mission type, dominio, skill, erro, tecnologia, arquivo ou anti-padrao.
- Preferir este indice antes de ler ledgers longos.
- Atualizar somente quando houver aprendizado reutilizavel.

## Campos

| Date | Mission | Tags | What Worked | What Failed | Reuse Before Next Similar Mission | Evidence |
|------|---------|------|-------------|-------------|-----------------------------------|----------|
| 2026-06-29 | Context Hygiene Protocol | context, tokens, long-mission | Compacted Snapshot preserva decisoes e descarta ruido operacional | Contexto longo sem snapshot mistura planos antigos e hipoteses invalidadas | Avaliar Context Health em transicoes de fase e antes de validacao ampla | `rules/context-hygiene.md`, `framework/operating-system/LEARNING.md` |
| 2026-06-29 | Execution Reliability Guardrails | retry, frontend, validation | Attempt Ledger e Boundary Map reduzem repeticao de comandos e falso sucesso de runtime | Tentar a mesma hipotese apos 2 falhas aumenta custo e risco | Antes de nova tentativa, exigir evidencia nova e variavel alterada | `rules/execution-loop-control.md`, `rules/frontend-runtime-validation.md` |
| 2026-06-30 | Execution Metrics | tokens, reporting, metrics | Baseline/actual units permitem estimar economia sem inventar tokens reais | Relatorios qualitativos nao sustentam comparacao recorrente | Registrar unidades operacionais quando task executavel tiver sinal util | `rules/execution-metrics.md`, `framework/operating-system/EXECUTION_METRICS.md` |
| 2026-07-01 | Update local framework from dkerson | git, conflict, update | Stash temporario + fast-forward preservou alteracoes locais antes de resolver conflitos | Pull direto em worktree sujo poderia sobrescrever ou confundir conflitos | Em update Git com dirty tree, verificar remotos, stash nomeado, ff-only e resolver conflitos por evidencia | `framework/operating-system/EXECUTION_METRICS.md` |
