# RAG Golden Questions Checklist

Use this checklist before declaring a RAG assistant production-ready.

- [ ] At least 10 representative questions exist for the target domain.
- [ ] Questions cover broad terms, exact titles, process questions, screen questions, regulation/policy questions and follow-ups.
- [ ] Each question has expected canonical documents.
- [ ] Each question has expected refusal behavior when knowledge is missing.
- [ ] Duplicate document records do not change document count.
- [ ] Top citations are unique by canonical document.
- [ ] Answer format is validated: context first, concise answer, invitation to deepen.
- [ ] Latency is measured for retrieval, rerank and generation.
- [ ] Curator workflow exists for unanswered or low-confidence questions.
- [ ] Permission-aware retrieval is tested with at least one restricted document.
