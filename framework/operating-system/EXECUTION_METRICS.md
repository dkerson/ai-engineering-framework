# Execution Metrics

> Per-execution lightweight metrics for future token savings reports.

## Method

- Real token savings require trustworthy token telemetry from the active surface.
- When real telemetry is unavailable, use operational units from `rules/execution-metrics.md`.
- Percentages in this file are estimated efficiency percentages, not measured token counts.
- Keep entries short; never store prompts, secrets, long code excerpts or private data.

## Entries

| Date | Mission | Surface | Mode | Recommended Model | Baseline Route | Actual Route | Baseline Units | Actual Units | Estimated Savings % | Retries Avoided | Errors Avoided | Confidence | Evidence |
|------|---------|---------|------|-------------------|----------------|--------------|----------------|--------------|---------------------|-----------------|----------------|------------|----------|
| 2026-06-30 | Token Savings Report baseline | Codex | Fast | gpt-5.4-mini | Manual qualitative report without structured per-execution metrics | Added report workflow from existing ledgers | 24 | 14 | 42 | 0 | 1 | Media | Report uses ledgers and declares no real token telemetry |
| 2026-06-30 | Execution Metrics | Codex | Standard | gpt-5.5 | Future reports rely on qualitative ledgers only | Added structured operational units and report fields | 32 | 20 | 38 | 0 | 2 | Media | Baseline/actual units, retries avoided and errors avoided now recorded |
