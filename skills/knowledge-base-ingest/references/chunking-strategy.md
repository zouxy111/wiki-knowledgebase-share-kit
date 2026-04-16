# Chunking Strategy for Long Markdown Sources

## Goal
Split long-form source material into chunks that are:
- readable
- reusable
- linkable
- maintainable in a wiki knowledge base

## Recommended split order

### 1. Prefer natural source boundaries
Use the source's own structure first:
- part
- chapter
- section
- appendix
- glossary

### 2. Split at the shallowest useful heading level
Typical defaults:
- book / handbook: start at H2 (chapter level)
- technical spec: start at H2 or H3
- notes dump: start where stable themes begin, not every timestamp
- tutorial: start at lesson or step group level

### 3. Re-split oversized chunks
If a chunk is still too large:
- split by the next heading level
- or convert one chapter into an overview + subtopic pages

## Heuristics

### Good chunk
- answers one stable question
- has a clear parent topic
- can be linked from overview and root pages
- is small enough to read and maintain without scrolling through a book-length page

### Bad chunk
- mixes multiple chapters
- is only a raw dump of copied prose
- has no obvious inbound links
- is too small to justify its own page

## Good page families

### Source overview page
Contains:
- source identity
- author / edition / origin
- what was imported
- page map
- navigation links

### Chapter page
Contains:
- chapter summary
- key concepts
- links to subtopics
- links to previous / next chapter pages

### Topic page
Contains:
- normalized concept or method
- source references
- related links to neighboring ideas

## Anti-patterns
- one page per paragraph
- one page for an entire book
- pure TOC pages with no knowledge content
- importing the source but forgetting to build navigation
