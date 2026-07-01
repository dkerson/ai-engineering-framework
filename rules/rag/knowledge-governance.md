# Knowledge Governance

- Every KB change must be versioned.
- Required metadata: id, canonical id/key, title, type, version, source origin, content hash, permissions, updated_at and index status.
- Reindex after structural changes; rollback must be supported.
- Do not index secrets or PII without an explicit approved policy.
- Additional uploads must run duplicate checks by normalized title and content hash.
- Document and chunk are different entities; reports and answers must count canonical documents.
- Unanswered questions, low confidence, wrong sources and duplicate clusters must feed curation.
