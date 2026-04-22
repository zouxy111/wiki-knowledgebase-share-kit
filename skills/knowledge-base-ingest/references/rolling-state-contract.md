# Rolling State Contract

## Run directory structure
A close-reading run should produce a directory like this:

```text
ingest-run/
  README.md
  batch-plan.json
  reading-state.json
  chunks/
  batch-packets/
  batch-notes/
  claim-map.json
  delivery-gate.json
  synthesis/
```

## `reading-state.json`
This file is the machine-readable snapshot of progress.
It should at least track:
- source path and source title
- source hash
- effective split level
- total batch count
- completed vs pending batches
- changed / new / removed batches after a rerun
- rolling snapshot of concepts / entities / candidate topics / open questions
- per-batch status and packet/note paths

## Rolling snapshot expectations
The rolling snapshot should remain lightweight.
It is not a full memory dump.
It should only carry enough context to help the next batch stay coherent:
- recent summaries
- top repeated concepts
- top entities
- candidate topics worth promoting
- unresolved questions worth watching

## `batch-notes/<batch-key>.json`
Each completed batch note should use this shape:

```json
{
  "batch_id": "batch-001",
  "batch_key": "chapter-a-b01",
  "batch_hash": "content-hash-for-this-batch",
  "status": "completed",
  "summary": "2-5 sentence batch summary",
  "key_claims": ["stable claim"],
  "concepts": ["term or concept"],
  "procedures": ["repeatable procedure"],
  "entities": ["named entity"],
  "open_questions": ["what remains unresolved"],
  "cross_refs": ["related chunk or batch id"],
  "candidate_topics": ["topic page candidate"]
}
```

These notes are not just “batch summaries”. They are the first structured evidence layer for later synthesis and claim validation.

## `claim-map.json`
This file records how important synthesized claims map back to:
- batch keys
- source chunks
- supporting quotes

Its purpose is to reduce unsupported or overstated delivery claims.

## `delivery-gate.json`
This file is the final completion gate.
It should summarize:
- chunk coverage status
- extractive note completeness
- claim support status
- integrity status
- final delivery label (`partial` / `coverage-complete` / `evidence-complete` / `ready-to-promote`)

## Keep it stable
Do not let batch notes drift into free-form diaries.
They should stay compact, comparable, and suitable for later synthesis.

## Incremental rerun rule
If the chunk hash for a batch changes:
- archive the old note for traceability
- reset that batch to pending
- keep other unchanged completed notes reusable

Do not force the reader to re-read the whole source when only one chapter changed.
