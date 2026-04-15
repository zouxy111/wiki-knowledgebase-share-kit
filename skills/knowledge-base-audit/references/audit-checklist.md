# Audit Checklist for a Markdown Knowledge Base

## Preferred audit dimensions
1. frontmatter completeness
2. role / area validity
3. dead links
4. orphan pages
5. missing entrypoint coverage
6. root page coverage
7. page-boundary drift
8. governance drift
9. noise regression
10. root-level stray markdown files

## Good audit order
1. Read the vault profile
2. Read reader entrypoint and maintainer entrypoint
3. Inspect root pages
4. Inspect content pages
5. Build link coverage picture
6. Compare current structure with root page map
7. Scan root-level markdown files
8. Report findings by priority

## Typical checks
- count content pages
- detect files without frontmatter
- detect missing required fields
- detect unresolved wikilinks
- detect pages with no valid entrypoint
- sample-check whether root pages contain long process narration
- sample-check whether `ops` pages have become running logs
- sample-check whether milestone log is still milestone-only
- detect markdown files at vault root that are not in canonical root-level markdown files

## Reporting template

```markdown
## Audit summary
- page count:
- missing frontmatter:
- dead links:
- orphan pages:
- missing entrypoints:
- root-level stray files:
- noise regression:

## Findings
### P1
- problem:
- pages:
- fix:

### P2
- problem:
- pages:
- fix:

### P3
- problem:
- pages:
- fix:
```

## Fix-mode priorities
If the user asks to fix, use this order:
1. missing frontmatter / invalid metadata
2. dead links and orphan pages
3. missing root-page or reader-entry coverage
4. stray root-level markdown files that obviously belong elsewhere
5. governance drift
6. noise cleanup and boundary tightening
