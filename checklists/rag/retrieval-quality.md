# Retrieval Quality Checklist

- [ ] Permissions applied before ranking.
- [ ] Top-k is appropriate for the domain.
- [ ] Scores are documented or inspectable.
- [ ] Deduplication uses canonical document identity, not only chunk or source id.
- [ ] Reported document count uses unique canonical documents.
- [ ] Hybrid search or rerank is applied when one retrieval mode favors the wrong source type.
- [ ] Question intent is considered: process, screen, regulation, presentation, integration or error.
- [ ] Golden questions for the domain passed before production.
