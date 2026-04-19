# Close-Reading Mode for Oversized Sources

## When to switch into this mode
Use close-reading mode when any of these is true:
- the source is book-scale or handbook-scale
- the source will split into many chunks and simple one-pass rewriting is too shallow
- the user explicitly asks for chunked close reading / 分块精读 / 精读整本书
- you need the AI to accumulate understanding across chapters instead of treating every chunk as isolated

## Goal
Do not only split the file.

Instead, create a stable reading harness that can:
- batch chunks into readable review packets
- preserve rolling context from completed batches
- collect reusable concepts, claims, procedures, and open questions
- synthesize stable knowledge-base outputs after close reading

## Recommended loop
1. Run `scripts/close_read_markdown.py`
2. Review one batch packet at a time
3. Save one JSON note per batch into `batch-notes/`
4. Treat those batch notes as the **extractive evidence layer**, not just short summaries
5. Re-run the script to refresh rolling state and future packet context
6. Prefer changed-batches-only continuation: keep unchanged completed notes, reset only batches whose chunk hash changed
7. When enough batches are complete, run `scripts/synthesize_knowledge.py`
8. Build `claim-map.json` for the important claims in the candidate pages
9. Build `delivery-gate.json` before claiming the import is complete
10. Promote only the stable overview / chapter / topic outputs into the vault

## Important rule
Close-reading mode is for **deep understanding of oversized sources**, not for dumping raw text into the knowledge base.

Additional rule:

> The execution agent must not self-certify “fully complete”.
> Completion belongs to the delivery gate, not to the worker summary.
