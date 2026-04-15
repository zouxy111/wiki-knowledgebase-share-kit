# Maintenance Checklist for a Markdown Knowledge Base

## Fixed maintenance loop
1. Read the vault profile
2. Gather source truth
3. Run the noise filter
4. Decide page role and area
5. Update target page
6. Sync root page / reader entry / milestone log
7. Validate metadata, links, and page boundaries

## Minimum sync requirement
Every substantial update should sync at least:
- target page
- corresponding root page
- reader entrypoint
- milestone log

## Noise filter
Remove or compress before writing:
- long task play-by-play
- one-off runtime states
- repeated update notes
- low-value absolute path lists
- raw run outputs
- original runtime mirrors
- explanation text that only mattered in the current chat

## Role-writing rules

### `project`
- navigation, stable overview, long-term boundaries, topic entrypoints
- not long process narration

### `knowledge`
- concepts, structures, methods, rules, decision frameworks
- not single-run fixes or temporary TODOs

### `ops`
- symptom / root cause / treatment / boundary
- reusable troubleshooting and repeatable runbooks
- not full chronological logs

### `task`
- ownership, collaboration, fill-back order, active task structure
- move stable knowledge elsewhere

### `overview`
- governance, index, maintainer guidance, vault-level explanations
- not project execution history

### `log`
- milestone-only
- not task replay

## Validation checklist
- required frontmatter fields present
- page role matches content
- area is valid according to the profile
- page has an entrypoint from root page or reader entrypoint
- no dead links introduced
- root pages did not absorb long process narration
- `ops` pages did not become running logs
- milestone log stayed milestone-only
