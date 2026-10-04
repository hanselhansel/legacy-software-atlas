# Legacy Software Atlas

Which legacy software is ready to be replaced by AI-native companies? This study maps
25 to 40 job categories (core banking, insurance policy admin, hospital records and
more), answers seven questions per category from cited sources, scores each on size,
pain, AI fit, lock-in and crowding, and ends with a replacement playbook drawn from
real cases. It is built for people thinking about founding an AI-native company to
replace legacy software.

**Status:** work in progress. No findings yet.

**Disclosure:** no affiliation with TypeSafe.

## Setup

```bash
brew install gitleaks          # required by the local verify gate
uv sync
git config core.hooksPath .githooks
scripts/verify.sh              # gitleaks, ruff, pytest; prints "verify: ok"
```

The Jev key is read from the `TYPESAFE_API_KEY` environment variable at runtime only.
It is never stored in the repo.

## Data and rights

The repo stores URLs, dates, short quotes under 30 words, and derived labels. It does
not redistribute full third-party text or personal data. Code is MIT licensed;
derived labels and aggregates are CC BY 4.0.

## Design

- Design: `docs/superpowers/specs/2026-10-05-legacy-software-atlas-design.md`
- Plans: `docs/superpowers/plans/`
