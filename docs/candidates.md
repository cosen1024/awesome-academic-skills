# Candidates, holds, and exclusions

Last reviewed: 2026-07-13.

Items here are not part of the verified main catalog. A hold is not a negative judgement; it means the item has unresolved evidence, portability, license, or scope questions.

## Hold for a later review

| Candidate | Why it is held |
|---|---|
| [bytedance/deer-flow — systematic-literature-review](https://github.com/bytedance/deer-flow/tree/main/skills/public/systematic-literature-review) | Public source and a concrete `SKILL.md` exist, but the workflow is tightly coupled to DeerFlow's subagent runtime and bundled scripts. Revisit as a runtime-specific entry with explicit portability notes. |
| [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | Source and skills are public, but the repository license says CC BY-NC-SA 4.0 while at least one inspected skill declares CC-BY-4.0. Hold until the applicable terms are clarified or the catalog models per-skill license overrides. |
| [LigphiDonk/Oh-my--paper](https://github.com/LigphiDonk/Oh-my--paper) | A substantial Claude Code research plugin, but it overlaps heavily with the two end-to-end entries already selected. A later release can compare its concrete engines and runtime requirements. |
| [henry-y/openclaw-paper-tools](https://github.com/henry-y/openclaw-paper-tools) | Public OpenClaw paper utilities were found, but the current catalog prioritizes cross-agent or fully documented workflow entries. Revisit with an OpenClaw-specific section. |
| [zouchenzhen/docx-template-translator-skill](https://github.com/zouchenzhen/docx-template-translator-skill) | Public skill, but primarily a Word-template conversion utility rather than a core research-workflow capability. |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | Public general writing skill; academic use is plausible, but its scope is not specifically research or scholarly writing. |

## Not an installable research Skill

| Project | Decision |
|---|---|
| [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | A resource list, not an individual installable Agent Skill. |
| [pengsida/learning_research](https://github.com/pengsida/learning_research) | Research-learning material, not an Agent Skill package. |
| [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | A useful MCP server, but standalone MCP projects are outside the main list. |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | A useful document-processing tool, but not itself an Agent Skill. |
| Weights & Biases, TensorBoard, Overleaf, Tectonic | Supporting research tools rather than Agent Skills. |

## Local-only items excluded

The discovery notes mentioned `paper-submission-check`, `journal-adapt`, and `paper-review-helper` as private/local skills. They are excluded because no public source repository was available. They can be reconsidered only after a public repository and license exist.
