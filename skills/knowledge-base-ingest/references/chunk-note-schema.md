# Chunk / Batch Note Schema

Treat `batch-notes/<batch-key>.json` as the **extractive evidence layer**, not as a free-form summary dump.

## Summary
Use one JSON file per batch.
The note should be short enough to compare across batches, but rich enough to synthesize later.

If you want to reduce omissions, do **not** jump directly from source chunks to candidate pages.
First make sure the batch note records:

- what headings were actually read
- what facts must be preserved
- what boundaries / exceptions must survive synthesis
- what still looks under-covered

That way the batch note becomes a real extractive artifact rather than a vague “I read this” marker.

## Field guidance
- `summary`: short batch-level explanation of what this segment contributes
- `key_claims`: reusable claims, not filler prose
- `concepts`: terms, frameworks, or ideas that recur across the source
- `procedures`: stepwise methods, runbooks, or repeatable moves
- `entities`: named people, systems, organizations, datasets, tools
- `open_questions`: conflicts, ambiguities, gaps, unclear scope
- `cross_refs`: chunk files or batch ids that should be revisited together
- `candidate_topics`: concepts likely worth promoting into standalone topic pages

## Recommended extractive extensions

If the source is high-stakes, very long, or easy to misread, extend each batch note with:

- `headings_seen`
- `must_keep_facts`
- `boundaries_and_exceptions`
- `omission_risk`

Example shape:

```json
{
  "batch_id": "batch-001",
  "batch_key": "chapter-a-b01",
  "batch_hash": "content-hash-for-this-batch",
  "status": "completed",
  "headings_seen": ["## Example", "### Caveats"],
  "summary": "2-5 sentence batch summary",
  "must_keep_facts": [
    {
      "fact_id": "fact-001",
      "text": "Important source-backed fact",
      "importance": "high",
      "supported_by": [
        {
          "chunk_file": "002-example.md",
          "quote": "direct supporting quote"
        }
      ]
    }
  ],
  "boundaries_and_exceptions": [
    {
      "boundary_id": "boundary-001",
      "text": "Important limitation or exception",
      "supported_by": [
        {
          "chunk_file": "002-example.md",
          "quote": "direct caveat quote"
        }
      ]
    }
  ],
  "key_claims": ["stable claim"],
  "concepts": ["term or concept"],
  "procedures": ["repeatable procedure"],
  "entities": ["named entity"],
  "open_questions": ["what remains unresolved"],
  "cross_refs": ["related chunk or batch id"],
  "candidate_topics": ["topic page candidate"],
  "omission_risk": ["what still feels thin or under-captured"]
}
```

## Minimal anti-overclaim rule

Do not mark a batch note as effectively “good enough” if:

- `headings_seen` is missing for a complex batch
- `must_keep_facts` is empty even though the batch contains definitional or normative material
- `boundaries_and_exceptions` is empty even though the batch includes caveats

In those cases, the note is still too weak to safely support synthesis.

## Anti-patterns
- copying long raw paragraphs from the source
- writing full essays instead of extraction notes
- mixing transient commentary with stable knowledge
- leaving the batch note as an empty placeholder after reading
