# Vault Profile Contract

## The ingest skill should not proceed without these facts
- vault root path
- markdown page directory
- reader entrypoint file
- milestone log file
- maintainer entrypoint file
- area list
- root page map
- canonical root-level markdown files
- frontmatter contract

## Why this matters
Long-form ingestion creates many pages at once. Without a profile, the skill cannot safely decide:
- where overview pages should live
- which root page should own a chapter/topic page group
- which files are allowed at the vault root
- how imported pages should be tagged and typed

## If the profile is missing
Ask for the minimum missing configuration before editing files.
Do not guess:
- root page filenames
- area names
- page directory layout
- metadata fields
- log policy
