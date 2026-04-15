# Vault Profile Contract

## The audit skill needs these facts
- vault root path
- content page directory
- reader entrypoint
- milestone log
- maintainer entrypoint
- area list
- root page map
- canonical root-level markdown files
- frontmatter contract

## Why root-level canonical files matter
The audit skill must know which markdown files are intentionally allowed at the vault root.
Otherwise it cannot reliably report stray root-level markdown artifacts.

## If the profile is missing
Ask for the minimum missing configuration before claiming something is invalid.
Do not guess:
- which pages are root pages
- whether a markdown file belongs at the vault root
- allowed area names
- required metadata fields
