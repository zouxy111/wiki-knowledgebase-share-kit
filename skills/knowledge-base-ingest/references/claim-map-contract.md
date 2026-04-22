# Claim Map Contract

Use `claim-map.json` to stop the ingest workflow from overclaiming completion or certainty.

## Purpose

`claim-map.json` is the evidence ledger for final synthesis.
It should answer:

- which candidate page contains which important claims
- whether those claims are directly supported, weakly supported, inferred, or unsupported
- which batch note / source chunk / evidence quote justifies each claim

Without this artifact, a delivery summary can easily overstate what was actually confirmed by the source.

## Minimum shape

```json
{
  "generated_at": "2026-04-19T14:40:00",
  "run_name": "ingest-run",
  "source_title": "Example Handbook",
  "pages": [
    {
      "page_file": "candidate-pages/knowledge-example-topic.md",
      "page_type": "knowledge",
      "claims": [
        {
          "claim_id": "claim-001",
          "text": "Important source-backed statement",
          "claim_kind": "core-fact",
          "status": "supported",
          "supported_by": [
            {
              "batch_key": "chapter-a-b01",
              "chunk_file": "002-topic.md",
              "quote": "direct supporting quote"
            }
          ]
        }
      ]
    }
  ]
}
```

## Allowed claim statuses

- `supported`
- `weakly-supported`
- `inferred`
- `unsupported`

## Promotion rule

Pages can only be treated as **ready to promote** when their important claims are:

- primarily `supported`
- optionally a small number of `weakly-supported` claims, clearly marked

Claims that remain `inferred` or `unsupported` must not be presented as settled knowledge.

## Keep it practical

This file does not need to model every sentence.
It should cover the **important claims that the final delivery is relying on**.
