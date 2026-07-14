# Verification methodology

## Discovery

The catalog uses four discovery channels:

1. existing research-workflow notes and drafts;
2. locally maintained, publicly hosted skill repositories;
3. the official Skills CLI discovery workflow (`npx skills find ...`) across research-stage keywords;
4. web and GitHub search for additional public repositories.

Discovery sources are only leads. A Skills CLI result, search snippet, article, or social post is never sufficient for inclusion by itself.

## First-party verification

For every main-list entry, maintainers inspect:

- the public GitHub repository;
- the exact `SKILL.md` or, for a suite/plugin, a concrete skill entry plus its manifest or README;
- the first-party installation or entry documentation;
- the repository-level license, or the absence of one;
- platform and runtime constraints stated by the upstream project.

`source_ref` stores the exact commit inspected. `source_url` and `install_url` are pinned to that commit so a future default-branch change does not rewrite the historical basis of verification.

## Status semantics

The main catalog uses one status:

- `verified`: source availability, entry path, and installation documentation were checked on `verified_at`.

This is a source-verification status, not an execution or endorsement status. Third-party skills were not installed or run as part of catalog verification. Security, scientific validity, reproducibility of advertised results, API costs, and policy compliance remain the user's responsibility.

## Selection policy

- Keep at least 20 high-confidence entries and expand only when a fixed source revision and first-party entry documentation are available.
- Cover all 13 stages of the research workflow.
- Prefer a small set of representative skills over listing every near-duplicate in a large bundle.
- Preserve platform diversity when the source documentation supports it.
- Move ambiguous, peripheral, runtime-locked, or license-conflicted candidates to `docs/candidates.md`.

Subjective comparisons are kept in `docs/ranking.md`, separate from the verified catalog. Ranking scores do not change source-verification status.

## Automated checks

`scripts/validate_data.py` enforces schema, category coverage, a minimum catalog size, commit pinning, and required metadata. `scripts/render_readmes.py` keeps the Chinese and English tables synchronized with the YAML source. `scripts/check_links.py` checks repository, pinned source, and install-document links without requiring a GitHub token.
