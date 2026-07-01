# RAG Canonical Document Identity

> Purpose: prevent RAG systems from confusing chunks, duplicate records and documents.

## Principle

RAG must distinguish:

- chunk: a searchable text segment;
- record: a database/storage row;
- document: the user-facing knowledge item;
- canonical document: the deduplicated identity used for counting, citation and curation.

Never report chunk count as document count.

## Canonical Key

Prefer a stable canonical key in this order:

1. explicit canonical document id;
2. normalized source URI or blob path;
3. content hash for the complete normalized document;
4. normalized title + document type + business area;
5. normalized title as a fallback.

The fallback is acceptable for chat display, but ingestion should move toward explicit canonical ids and content hashes.

## Deduplication Points

Apply canonical document deduplication in four places:

- ingestion: avoid publishing exact duplicates silently;
- retrieval: avoid returning many records for the same document;
- answer context: keep the best chunk per canonical document unless the user asks for detailed evidence;
- citation display: show a document once, with optional section/chunk count.

## Required Metadata

Every indexed document should carry:

- canonical id or canonical key;
- title;
- document type;
- area/submenu/project context;
- source origin;
- content hash;
- index status;
- embedding model/version where applicable;
- permissions/scope.

## Curation

Duplicate clusters must be visible to curators with:

- canonical title;
- document ids/records in the cluster;
- source origins;
- content hashes or similarity signal;
- recommended action: merge, archive, keep separate, or mark canonical.

## Validation

A RAG implementation is not production-ready until golden questions verify:

- document count is unique by canonical document;
- citations do not repeat the same document;
- screen docs do not outrank process/regulation docs when the user asks for process/regulation;
- a duplicate record does not change the answer or document count.
