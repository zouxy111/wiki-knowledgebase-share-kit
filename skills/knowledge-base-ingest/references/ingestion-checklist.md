# Long-Form Ingestion Checklist

## Fixed ingest loop
1. Read source markdown and vault profile
2. Decide source type and target knowledge structure
3. Build an ingestion map before editing files
4. Split the source into manageable chunks
5. Decide page role and area for each page group
6. Rewrite into knowledge-base form
7. Add navigation and cross-links
8. Sync root page / reader entrypoint / milestone log
9. Validate page length, coverage, and link integrity

## Minimum output set
Every substantial import should produce at least:
- one source overview page
- one or more chapter/topic pages
- links between these pages
- an entry from a root page or reader entrypoint
- a milestone log update

## Link model checklist
Each imported page group should consider:
- parent link
- child list
- prev / next navigation
- related topic links
- source attribution

## Default compression rules
Prefer:
- summaries
- rewritten outlines
- concept extraction
- normalized terminology
- merged repeated explanations

Avoid by default:
- giant verbatim chapter copies
- raw appendix dumps with no navigation
- pages that only mirror the original table of contents
- dozens of micro-pages with no retrieval value

## Validation checklist
- no page should remain a giant monolith if a better split is obvious
- no imported page should be orphaned
- source lineage should be visible
- page role should match content
- entrypoints should be updated
- milestone log should capture the import event
