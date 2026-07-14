# Contributing

感谢你帮助维护这份科研 Agent Skills 清单。Please keep every change evidence-based and easy to verify.

## What belongs in the main catalog

An entry must satisfy all of the following:

1. Its GitHub repository is public and directly accessible.
2. The repository contains an inspectable `SKILL.md`, skill suite, or plugin manifest backed by public source.
3. A first-party README, `SKILL.md`, or official document explains its purpose and installation or entrypoint.
4. The skill has a clear place in one of the 13 research-workflow categories.
5. The entry records the exact commit reviewed, license status, supported agents, and verification date.

Do not submit marketing-only pages, closed-source assistants, generic tool lists, standalone MCP servers, or claims sourced only from blog posts and social media.

## Verification meaning

`verified` means the public repository, exact source entry, and installation documentation were checked. It does **not** mean:

- the code was executed;
- the project passed a security audit;
- every advertised capability was reproduced;
- the skill is academically correct or appropriate for a particular study.

Record operational caveats in `notes_zh` and `notes_en`, especially authentication, data upload, external APIs, non-commercial licenses, missing licenses, or host-specific requirements.

## Adding or updating an entry

1. Edit `data/skills.yaml`; it is the source of truth.
2. Pin `source_ref` to the full 40-character commit SHA that you inspected.
3. Make `source_url` point to the exact `SKILL.md` at that commit.
4. Pin `install_url` to the README or official installation document at the same commit.
5. Paraphrase the purpose; do not copy long upstream descriptions.
6. Regenerate both README files and run validation.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/render_readmes.py --write
python3 scripts/validate_data.py
python3 scripts/render_readmes.py --check
python3 scripts/check_links.py --scope source
```

## Pull request checklist

- [ ] The repository and exact source link are publicly accessible.
- [ ] Purpose, platform, and install claims come from first-party sources.
- [ ] The license field reflects the upstream repository; `NOASSERTION` is used when no clear license was found.
- [ ] Chinese and English summaries describe the same capability.
- [ ] Limitations and data-handling requirements are explicit.
- [ ] Validation and generated-README checks pass.
- [ ] No token, Cookie, credential, private URL, or local-only secret was added.

Unresolved candidates should go to `docs/candidates.md` instead of the main catalog.
