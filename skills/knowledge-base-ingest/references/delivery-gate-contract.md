# Delivery Gate Contract

Use `delivery-gate.json` as the **single source of truth** for whether an ingest run is actually complete.

## Purpose

The execution agent must not self-certify completion.

Instead, the run should produce a small gate file that combines:

- chunk coverage status
- extractive batch-note status
- claim support status
- integrity / link / frontmatter status

Only this gate may authorize the labels:
- complete
- fully imported
- ready to promote

## Minimum shape

```json
{
  "generated_at": "2026-04-19T14:45:00",
  "run_name": "ingest-run",
  "coverage_check": {
    "status": "pass",
    "manifest_entries": 48,
    "coverage_rows": 48,
    "unread_chunks": 0,
    "blocked_chunks": 0
  },
  "extractive_check": {
    "status": "pass",
    "expected_batches": 12,
    "completed_notes": 12,
    "missing_notes": [],
    "weak_batches": []
  },
  "evidence_check": {
    "status": "pass",
    "total_claims": 37,
    "supported_claims": 33,
    "weakly_supported_claims": 4,
    "inferred_claims": 0,
    "unsupported_claims": 0
  },
  "integrity_check": {
    "status": "pass",
    "dead_links": 0,
    "missing_frontmatter": 0,
    "unregistered_pages": 0
  },
  "final_status": "ready-to-promote"
}
```

## Allowed final statuses

- `partial`
- `coverage-complete`
- `evidence-complete`
- `ready-to-promote`

## Rule

If `final_status` is anything other than `ready-to-promote`, the run must be reported as:

- partial
- draft
- incomplete
- candidate only

and **must not** be presented as a fully complete import.
