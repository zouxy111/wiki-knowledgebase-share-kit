# Vault Profile Contract

## The skill should not proceed without these facts
- vault root path
- markdown page directory
- reader entrypoint file
- milestone log file
- maintainer entrypoint file
- area list
- root page map
- canonical root-level markdown files
- frontmatter contract

## The fixed model this skill assumes
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

## If the profile is missing
Ask for the minimum missing configuration before editing files.
Do not guess:
- paths
- root page filenames
- area names
- naming conventions
- log policy

## Why canonical root-level markdown files matter
Audit and maintenance both need to know which markdown files are allowed at the vault root.
Without this, stray-file checks become noisy and unreliable.
