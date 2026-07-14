# Awesome Academic Skills

[中文](README.md)

A workflow-oriented, machine-validated catalog of public Agent Skills for academic research. The current release contains 39 high-confidence entries across 13 stages, from ideation and literature work to experiments, submission, and reviewer response.

## Scope

- Every main-list entry has a publicly accessible GitHub repository and a traceable `SKILL.md`, plugin entry, or skill-suite entrypoint.
- Tables show only the repository, pinned skill entrypoint, and purpose for quick scanning. Platform, installation, license, and verification metadata remain in [data/skills.yaml](data/skills.yaml).
- All technical claims come only from first-party README files, `SKILL.md` files, or official documentation.
- `verified` means that the public source, exact entrypoint, and installation documentation were checked on the stated date. It does not mean the third-party skill was executed, security-audited, or endorsed for research quality.
- Review upstream dependencies, permissions, data-upload behavior, and license terms before installation.
- Marketing-only products, closed implementations, ordinary research tools, and standalone MCP servers are outside the main catalog.

The structured source of truth is [data/skills.yaml](data/skills.yaml). See [docs/methodology.md](docs/methodology.md) for the process and [docs/candidates.md](docs/candidates.md) for held or excluded candidates. A Chinese source-audit ranking of the user-nominated projects is available in [docs/ranking.md](docs/ranking.md).

## Install and use

Choose a research stage, open the pinned source by clicking the skill name, then give that link to your agent:

```text
Install this Agent Skill: <paste the Skill link>

First read the Skill and the repository's official README. Identify my current agent, install directory, and dependencies. Before acting, explain which directories will be written, which scripts will run, and which permissions are required; install only after confirmation. Do not guess the installation method or run code from an unverified source.
```

Projects may use skill directories, plugins, Python packages, or setup scripts, so there is no trustworthy universal command. The structured catalog retains each upstream installation entry for agent verification and automation.

## Catalog

<!-- CATALOG:START -->

### Topics and Ideas

| Repository / Skill | Purpose |
|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>[scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/blob/e12d68309994d5643c7c2ee00ce883f570916b7d/skills/scientific-brainstorming/SKILL.md) | Generates research ideas, interdisciplinary connections, testable hypotheses, and potential gaps through open-ended dialogue. |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)<br>[brainstorming-research-ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/21-research-ideation/brainstorming-research-ideas/SKILL.md) | Uses structured frameworks to explore problem spaces, project pivots, and novel angles on existing work. |
| [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)<br>[research-ideation](https://github.com/Galaxy-Dawn/claude-scholar/blob/2f7766fd541a723d4ddc6230b3277f948d61b093/skills/research-ideation/SKILL.md) | Refines a vague topic into a research-question card, evidence needs, falsification criteria, method choices, and next actions, with optional Zotero, Obsidian, analysis, and writing handoffs. |

### Literature Search

| Repository / Skill | Purpose |
|---|---|
| [Mingyue-Cheng/academic-search](https://github.com/Mingyue-Cheng/academic-search)<br>[academic-search](https://github.com/Mingyue-Cheng/academic-search/blob/3ae684450bc0d24a9c4cb0b39ad08d3acb8f95fb/SKILL.md) | Searches multiple academic sources, normalizes metadata, analyzes citations, checks open access, and exports references. |
| [cookjohn/cnki-skills](https://github.com/cookjohn/cnki-skills)<br>[cnki-search](https://github.com/cookjohn/cnki-skills/blob/20d65f660456daf53ad0f7c74494ac3b829b925f/skills/cnki-search/SKILL.md) | Uses Chrome DevTools MCP to operate CNKI pages, search by keyword, and extract structured results. |

### Paper Reading and Knowledge Management

| Repository / Skill | Purpose |
|---|---|
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)<br>[nature-reader](https://github.com/Yuan1z0825/nature-skills/blob/4170a8a6262642841699c55d468e21ff70a2fe34/skills/nature-reader/SKILL.md) | Turns PDFs, DOIs, arXiv papers, or pasted text into figure-aware, source-grounded bilingual full-paper readers. |
| [huangkiki/dailypaper-skills](https://github.com/huangkiki/dailypaper-skills)<br>[paper-reader](https://github.com/huangkiki/dailypaper-skills/blob/ec6329c9ee6405f706d7a327937872ae75220774/skills/paper-reader/SKILL.md) | Reads, summarizes, and critiques computer-vision and deep-learning papers, with optional Zotero integration. |
| [SNL-UCSB/literature-survey-skill](https://github.com/SNL-UCSB/literature-survey-skill)<br>[survey](https://github.com/SNL-UCSB/literature-survey-skill/blob/18475960526bc0f3a64bced026d11ccce97a521b/SKILL.md) | Organizes 10–150 papers through Intent, Triage, Deepen, and Synthesize stages for depth-aware reading, grounded extraction, cross-paper matrices, and gap analysis. |
| [cosen1024/llm-wiki-skill](https://github.com/cosen1024/llm-wiki-skill)<br>[llm-wiki-skill](https://github.com/cosen1024/llm-wiki-skill/blob/2f200cd945021a56376794ffecb3b19174de6f85/SKILL.md) | Incrementally compiles papers, notes, and web sources into a persistent, cross-linked, queryable Markdown knowledge base. |

### Research Design

| Repository / Skill | Purpose |
|---|---|
| [zjYao36/Auto-Research-Refine](https://github.com/zjYao36/Auto-Research-Refine)<br>[research-refine-pipeline](https://github.com/zjYao36/Auto-Research-Refine/blob/a1f14495856afe1e400c65d84ce22f68a027ef75/research-refine-pipeline/SKILL.md) | Refines a vague research direction into a reviewable proposal and a detailed experimental roadmap. |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>[experimental-design](https://github.com/K-Dense-AI/scientific-agent-skills/blob/e12d68309994d5643c7c2ee00ce883f570916b7d/skills/experimental-design/SKILL.md) | Plans randomization, grouping, blocking, factorial designs, replication, and confounding control before data collection. |

### Experiments and Code

| Repository / Skill | Purpose |
|---|---|
| [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills)<br>[paper-to-code](https://github.com/lingzhi227/agent-research-skills/blob/9e6c085d65e313e475e921fdfe795ac11eb7589e/skills/paper-to-code/SKILL.md) | Converts an ML paper into a runnable repository through planning, per-file analysis, and dependency-ordered implementation. |
| [jurgendn/agent-skills](https://github.com/jurgendn/agent-skills)<br>[reproducibility-audit](https://github.com/jurgendn/agent-skills/blob/ff8db273421cd0ec6cde55d84d802a4e9e5fdb26/skills/research-skills/artifact-and-reproducibility/reproducibility-audit/SKILL.md) | Audits whether code, data, configuration, seeds, and documentation are sufficient to reproduce a target result. |

### Data Analysis

| Repository / Skill | Purpose |
|---|---|
| [allenai/asta-plugins](https://github.com/allenai/asta-plugins)<br>[analyze-data](https://github.com/allenai/asta-plugins/blob/1f9d837a48910a28a8f2aee23fc174db891ad234/plugins/asta-tools/skills/analyze-data/SKILL.md) | Uses the DataVoyager multi-agent pipeline to execute code, create artifacts, and answer a focused question over tabular data. |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>[statistical-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/e12d68309994d5643c7c2ee00ce883f570916b7d/skills/statistical-analysis/SKILL.md) | Guides test selection, assumption checks, effect sizes, power analysis, Bayesian alternatives, and APA-style reporting. |

### Paper Writing

| Repository / Skill | Purpose |
|---|---|
| [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)<br>[research-paper-writing](https://github.com/Master-cai/Research-Paper-Writing-Skills/blob/77e7c2c1ba06f7d71844873147665437a03aac1b/research-paper-writing/SKILL.md) | Supports ML, CV, and NLP paper drafting and revision through section structure, paragraph flow, claim alignment, and reviewer-facing presentation. |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)<br>[nature-writing](https://github.com/Yuan1z0825/nature-skills/blob/4170a8a6262642841699c55d468e21ff70a2fe34/skills/nature-writing/SKILL.md) | Plans, drafts, or restructures manuscript sections and the overall argument from author-provided claims, results, figures, and notes. |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)<br>[ml-paper-writing](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/ml-paper-writing/SKILL.md) | Structures arguments, citations, LaTeX drafts, and camera-ready preparation for top ML and AI venues from a research repository. |
| [Norman-bury/research-writing-skill](https://github.com/Norman-bury/research-writing-skill)<br>[research-writing-assistant](https://github.com/Norman-bury/research-writing-skill/blob/6f7959554b4614d879d79cb4ece9ed04a7c8a88c/SKILL.md) | Organizes thesis and research-article work through routing, brainstorming, chapter drafting, evidence-driven introductions, experiment planning, LaTeX, statistics, and self-review modules. |
| [Boom5426/Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills)<br>[paper-workflow](https://github.com/Boom5426/Nature-Paper-Skills/blob/edf232f534d859d3db38b48654f50bfa5023dd90/skills/core/paper-workflow/SKILL.md) | Routes Nature-series manuscripts across project bootstrap, evidence-chain revision, figure-text alignment, statistical and citation audits, submission checks, and reviewer response skills. |
| [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer)<br>[scientific-writing](https://github.com/K-Dense-AI/claude-scientific-writer/blob/44414bded0ea850658aac59c014f3d6bec6d1ca8/skills/scientific-writing/SKILL.md) | Generates papers, reviews, grants, and scientific reports through live research, two-stage IMRAD drafting, citation management, reporting guidelines, figures, and LaTeX output. |

### Polishing and Translation

| Repository / Skill | Purpose |
|---|---|
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)<br>[nature-polishing](https://github.com/Yuan1z0825/nature-skills/blob/4170a8a6262642841699c55d468e21ff70a2fe34/skills/nature-polishing/SKILL.md) | Polishes, restructures, or translates academic prose while addressing overclaiming, writing strategy, and selected LaTeX layout issues. |
| [wentorai/research-plugins](https://github.com/wentorai/research-plugins)<br>[academic-translation-guide](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/writing/polish/academic-translation-guide/SKILL.md) | Provides a workflow and checkpoints for academic translation, post-editing, and Chinglish correction. |

### Citations and LaTeX

| Repository / Skill | Purpose |
|---|---|
| [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills)<br>[bib-search-citation](https://github.com/bahayonghang/academic-writing-skills/blob/1c04e89cbac219661ef026a34ca5805a357d7c21/academic-writing-skills/bib-search-citation/SKILL.md) | Searches and filters local BibTeX, BibLaTeX, and Zotero exports and generates LaTeX or Typst citation snippets. |
| [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills)<br>[latex-paper-en](https://github.com/bahayonghang/academic-writing-skills/blob/1c04e89cbac219661ef026a34ca5805a357d7c21/academic-writing-skills/latex-paper-en/SKILL.md) | Repairs and improves English LaTeX papers, covering compilation, formatting, citations, section logic, tables, pseudocode, and submission readiness. |
| [serenakeyitan/citation-check-skill](https://github.com/serenakeyitan/citation-check-skill)<br>[citation-check-skill](https://github.com/serenakeyitan/citation-check-skill/blob/b9deb7077099f56b05c9b6ecea744c2ca0a6d324/SKILL.md) | Freezes an exhaustive claim list from documents, slides, PDFs, or images, then checks citations, numbers, and claim-source alignment against the web or user-provided documents. |
| [yunshenwuchuxun/latex-paper-skills](https://github.com/yunshenwuchuxun/latex-paper-skills)<br>[paper-from-zero](https://github.com/yunshenwuchuxun/latex-paper-skills/blob/d0f106108cb09e448604a56ce973d35b340cf497/.codex/skills/paper-from-zero/SKILL.md) | Builds a literature map, innovation and contribution framing, claim-evidence matrix, and outline contract from a fixed topic before routing to review or empirical LaTeX writing and result backfill. |

### Scientific Plotting

| Repository / Skill | Purpose |
|---|---|
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)<br>[academic-plotting](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/academic-plotting/SKILL.md) | Generates architecture diagrams and matplotlib/seaborn paper figures from manuscript context or experiment data, with chart-type selection. |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>[scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/e12d68309994d5643c7c2ee00ce883f570916b7d/skills/scientific-visualization/SKILL.md) | Produces journal-ready multi-panel figures with error bars, significance annotations, colorblind-safe palettes, and venue formatting. |

### Pre-submission Checks

| Repository / Skill | Purpose |
|---|---|
| [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills)<br>[paper-audit](https://github.com/bahayonghang/academic-writing-skills/blob/1c04e89cbac219661ef026a34ca5805a357d7c21/academic-writing-skills/paper-audit/SKILL.md) | Performs reviewer-style diagnosis, submission gates, blocker triage, and revision roadmaps for .tex, .typ, or .pdf manuscripts. |
| [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills)<br>[self-review](https://github.com/lingzhi227/agent-research-skills/blob/9e6c085d65e313e475e921fdfe795ac11eb7589e/skills/self-review/SKILL.md) | Runs an ensemble self-review of PDF or LaTeX manuscripts using the NeurIPS form, three reviewer personas, and reflection refinement. |

### Peer Review and Reviewer Response

| Repository / Skill | Purpose |
|---|---|
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)<br>[academic-paper-reviewer](https://github.com/Imbad0202/academic-research-skills/blob/2aabdf6d56ade6e4e5e52eb468f9c6c4d392988d/academic-paper-reviewer/SKILL.md) | Performs multi-perspective manuscript review with dynamic editor, peer-reviewer, and Devil's Advocate personas. |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)<br>[nature-response](https://github.com/Yuan1z0825/nature-skills/blob/4170a8a6262642841699c55d468e21ff70a2fe34/skills/nature-response/SKILL.md) | Drafts, audits, or revises point-by-point responses, rebuttals, revision cover letters, and marked manuscript excerpts. |

### End-to-end Workflows

| Repository / Skill | Purpose |
|---|---|
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)<br>[academic-pipeline](https://github.com/Imbad0202/academic-research-skills/blob/2aabdf6d56ade6e4e5e52eb468f9c6c4d392988d/academic-pipeline/SKILL.md) | Orchestrates a ten-stage pipeline spanning research, writing, integrity checks, review, revision, re-review, and finalization. |
| [ZimoLiao/scholaraio](https://github.com/ZimoLiao/scholaraio)<br>[ScholarAIO skill suite](https://github.com/ZimoLiao/scholaraio/blob/0b1f5536e772bf21ff946e68b7b8eeb032febc40/.claude/skills/setup/SKILL.md) | Provides coding agents with an integrated research workspace for paper libraries, search, ingestion, knowledge graphs, scientific tools, writing, and citation checks. |
| [TobiasBlask/open-paper-machine](https://github.com/TobiasBlask/open-paper-machine)<br>[Open Academic Paper Machine](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/writing-engine/SKILL.md) | A Claude Code plugin that orchestrates ideation, literature, methods, writing, figures, LaTeX, verification, peer review, and submission engines. |
| [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine)<br>[paper-spine](https://github.com/WUBING2023/PaperSpine/blob/d4529208cda72aa075767611b0265b95b709b550/src/skill/SKILL.md) | Uses a 12-stage, contribution-first, results-as-validation, reviewer-aware gate system to turn materials or drafts into auditable LaTeX, PDF, Word, submission, and response artifacts. |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex)<br>[academic-research-suite](https://github.com/Imbad0202/academic-research-skills-codex/blob/73ab70ad071ea51357a52086e705e3b766cbc5b2/skills/academic-research-suite/SKILL.md) | Packages deep research, paper writing, review, full pipelines, and experiment planning behind one Codex-native router while retaining upstream ARS evidence, integrity, and safety boundaries. |
| [LMDHQ-0420/ResearchPilot-Skills](https://github.com/LMDHQ-0420/ResearchPilot-Skills)<br>[ResearchPilot-Skills v2.0 router](https://github.com/LMDHQ-0420/ResearchPilot-Skills/blob/416d9b77e231bdaec2879a5ded12dafa238e0911/skills/ResearchPilot-Skills-zh/research%5BSTART%5D/SKILL.md) | Connects bilingual stage skills for direction exploration, idea refinement, experiment and implementation design, coding iteration, and section-by-section paper writing into a resumable project-file workflow. |

<!-- CATALOG:END -->

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding or updating an entry. Do not hand-edit the generated tables above. Update `data/skills.yaml`, then run:

```bash
python3 scripts/render_readmes.py --write
python3 scripts/validate_data.py
python3 scripts/render_readmes.py --check
```

## License

Original catalog content, documentation, and scripts in this repository are licensed under the [MIT License](LICENSE). Each third-party project remains governed by its own license; license metadata in [data/skills.yaml](data/skills.yaml) does not alter upstream terms.
