# Security Policy

## Supported versions

This repository is maintained as a reusable documentation-and-skill package. Security fixes are applied to the current development line and the latest published release.

| Version | Supported |
|---|---|
| `main` | ✅ |
| Latest release | ✅ |
| Older releases | ❌ |

## Reporting a vulnerability

If you believe you have found a security issue, please **do not open a public issue with full exploit details**.

Preferred reporting path:
1. Use **GitHub private vulnerability reporting** / a private security advisory if it is available for this repository.
2. If private reporting is not available, contact the maintainers through their GitHub profiles before public disclosure.
3. Use a public issue only for **non-sensitive hardening questions** or when the report does not expose a real exploit path.

When reporting, please include:
- a short summary of the issue
- the affected file(s), script(s), or workflow(s)
- reproduction steps
- impact and scope
- any suggested mitigation if you already have one

## What to expect

The maintainers will try to:
- acknowledge the report in a reasonable time
- assess severity and scope
- decide whether a fix belongs on `main`, the latest release, or both
- coordinate disclosure once a fix or mitigation is ready

## Scope notes

This repository mainly contains:
- markdown documentation
- reusable templates
- skill metadata and helper scripts

Typical security-relevant areas include:
- shell scripts in `skills/**/scripts/`
- template wording that could encourage unsafe behavior
- instructions that cause users to expose private data or secrets
- automation or coordination flows that mishandle sensitive information

## Sensitive data rule

Do not include API keys, tokens, passwords, cookies, or private user data in public issues, pull requests, or example files.
