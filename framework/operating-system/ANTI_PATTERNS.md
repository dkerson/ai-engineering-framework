# Anti Patterns

| Anti Pattern | Signal | Risk | Recommendation |
|--------------|--------|------|----------------|
| Chunk-as-document counting | RAG reports chunks or duplicate records as documents | High | Use canonical document identity and golden questions |
| Symptom-only RAG patching | Fix citation display without checking ingestion, canonical identity and curation | High | Trace issue through ingestion, retrieval, answer context and UI |
| Learning without promotion status | Useful lesson stays in chat summary only | Medium | Use Execution Learning Loop with observed/recommended/approved/implemented status |
| Automatic self-modification | Framework changes without approval | High | Never allow; require user approval |
| Skill sprawl | Many overlapping skills without usage data | Medium | Track usage before consolidation |
| Documentation duplication | Same rule repeated in many docs | Medium | Prefer links and central rules |
| Token waste | Re-reading already summarized context | Medium | Use Working Context and Mission Memory |
