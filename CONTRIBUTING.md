# Contributing

Thank you for considering a contribution. This repository is a reusable kit for maintaining markdown/wiki knowledge bases with a knowledge-base-first workflow.

## What kind of contributions are welcome
- Better documentation or onboarding instructions
- Stronger maintenance or audit checklists
- Clearer prompt wording for the shareable skills
- More portable examples that do not assume a specific local environment
- Bug fixes in templates, docs, or skill metadata

## Before you open a pull request
1. Keep the **shareable template body de-localized**.
   - Do not hardcode personal local paths in reusable skill files.
   - Do not hardcode one user's area names or root page names in the template body.
2. Put environment-specific details in `examples/`, not in the reusable skill core.
3. Preserve the fixed page-role model unless you are intentionally proposing a breaking change:
   - `project`
   - `knowledge`
   - `ops`
   - `task`
   - `overview`
4. Keep the methodology boundaries intact:
   - knowledge-base-first
   - root pages are for navigation and stable overview
   - `ops` pages default to symptom / root cause / fix / boundary
   - milestone logs should not become task playbacks

## Recommended validation
Before submitting, please check:
- the three skill directories still contain `SKILL.md`, `references/`, and `agents/openai.yaml`
- the example prompts still match the current skill names
- the template docs do not accidentally reintroduce personal local paths
- examples remain examples and do not leak into the reusable template wording

## Pull request style
- Prefer small, focused PRs
- Explain *why* the change improves reuse or clarity
- Note whether the change affects template behavior, examples, or docs only
- If the change is breaking, document the migration path in the PR description and `CHANGELOG.md`

## Issues
When filing an issue, please include:
- what platform you use the skills on
- what you expected to happen
- what actually happened
- whether the problem is in the reusable template, the example profile, or your own vault profile
