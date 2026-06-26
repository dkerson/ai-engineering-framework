---
name: chunking-specialist
description: >-
  Especialista em chunk size, overlap e segmentação por tipo (MD, HTML, PDF, DOCX, TXT, FAQ). Invocado pelo rag-orchestrator em indexação.
---

# Chunking Specialist

## Objetivo

Definir estratégia de chunking por tipo de documento.

## Parâmetros

- Chunk size: 256–512 tokens (ajustável)
- Overlap: 10–20%
- FAQ: 1 par Q/A por chunk
- Markdown: respeitar headings

## Referências

- `knowledge/rag/chunking.md`
- `templates/rag/chunk-template.md`
- `checklists/rag/chunk-quality.md`
