# Awesome Academic Skills

[English](README_EN.md)

一份按科研工作流组织、可机器校验的公开 Agent Skills 清单。当前版收录 39 个高置信条目，覆盖从选题、文献、实验到投稿与审稿回复的 13 个环节。

## 收录边界

- 只收录公开 GitHub 源码，并能定位到项目自己的 `SKILL.md`、插件入口或 Skill 套件入口。
- 表格只展示仓库、固定版本 Skill 入口和用途，方便快速浏览；平台、安装、许可与核验元数据保留在 [data/skills.yaml](data/skills.yaml)。
- 所有技术事实只采用仓库 README、`SKILL.md` 或官方文档。
- `verified` 表示在标注日期核验了公开仓库、具体入口和安装说明，不表示已经运行第三方 Skill，也不构成安全、准确性或学术质量背书。
- 安装前请阅读上游依赖、权限、数据上传与许可证说明。
- 只有宣传页、无法审阅源码的产品、普通科研工具和 MCP 不进入主清单。

结构化事实源：[data/skills.yaml](data/skills.yaml)。筛选方法见 [docs/methodology.md](docs/methodology.md)，暂缓与排除项见 [docs/candidates.md](docs/candidates.md)。用户点名项目的源码审计版“从夯到拉”榜单见 [docs/ranking.md](docs/ranking.md)。

## 安装与使用

先按科研阶段选择条目，点击 Skill 名称打开核验时的固定版本源码，然后把链接交给你的 Agent：

```text
请安装这个 Agent Skill：<粘贴 Skill 链接>

先阅读该 Skill 与仓库 README 的官方安装说明，识别我当前使用的 Agent、安装目录和依赖；执行前说明将写入哪些目录、运行哪些脚本以及需要哪些权限，得到确认后再安装。不要猜测安装方式，也不要执行来源不明的代码。
```

不同项目可能采用 Skill 目录、插件、Python 包或安装脚本，并不存在可靠的统一命令。结构化清单仍保留每个项目的上游安装入口，供 Agent 核对和自动化使用。

## 清单

<!-- CATALOG:START -->

### 选题与 Idea

| 仓库 / Skill | 用途 |
|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>[scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/blob/e12d68309994d5643c7c2ee00ce883f570916b7d/skills/scientific-brainstorming/SKILL.md) | 用开放式对话生成研究想法、跨学科连接、可检验假设与潜在研究缺口。 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)<br>[brainstorming-research-ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/21-research-ideation/brainstorming-research-ideas/SKILL.md) | 用结构化框架探索问题空间、项目转向和已有工作的创新角度。 |
| [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)<br>[research-ideation](https://github.com/Galaxy-Dawn/claude-scholar/blob/2f7766fd541a723d4ddc6230b3277f948d61b093/skills/research-ideation/SKILL.md) | 将模糊选题收敛为研究问题卡、证据需求、证伪条件、方法选择和下一步行动，并可衔接 Zotero、Obsidian、实验分析与写作流程。 |

### 文献检索

| 仓库 / Skill | 用途 |
|---|---|
| [Mingyue-Cheng/academic-search](https://github.com/Mingyue-Cheng/academic-search)<br>[academic-search](https://github.com/Mingyue-Cheng/academic-search/blob/3ae684450bc0d24a9c4cb0b39ad08d3acb8f95fb/SKILL.md) | 跨多个学术来源检索论文、规范化元数据、分析引用、判断开放获取并导出参考文献。 |
| [cookjohn/cnki-skills](https://github.com/cookjohn/cnki-skills)<br>[cnki-search](https://github.com/cookjohn/cnki-skills/blob/20d65f660456daf53ad0f7c74494ac3b829b925f/skills/cnki-search/SKILL.md) | 通过 Chrome DevTools MCP 操作中国知网页面，按关键词检索并提取结构化结果。 |

### 论文阅读与知识管理

| 仓库 / Skill | 用途 |
|---|---|
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)<br>[nature-reader](https://github.com/Yuan1z0825/nature-skills/blob/4170a8a6262642841699c55d468e21ff70a2fe34/skills/nature-reader/SKILL.md) | 将 PDF、DOI、arXiv 或正文转换为图表对齐、可追溯的中英双语全文阅读稿。 |
| [huangkiki/dailypaper-skills](https://github.com/huangkiki/dailypaper-skills)<br>[paper-reader](https://github.com/huangkiki/dailypaper-skills/blob/ec6329c9ee6405f706d7a327937872ae75220774/skills/paper-reader/SKILL.md) | 面向计算机视觉与深度学习论文的精读、总结、批判性分析及 Zotero 论文读取。 |
| [SNL-UCSB/literature-survey-skill](https://github.com/SNL-UCSB/literature-survey-skill)<br>[survey](https://github.com/SNL-UCSB/literature-survey-skill/blob/18475960526bc0f3a64bced026d11ccce97a521b/SKILL.md) | 以 Intent、Triage、Deepen、Synthesize 四阶段组织 10–150 篇论文的分层阅读、证据摘录、跨论文矩阵与研究缺口分析。 |
| [cosen1024/llm-wiki-skill](https://github.com/cosen1024/llm-wiki-skill)<br>[llm-wiki-skill](https://github.com/cosen1024/llm-wiki-skill/blob/2f200cd945021a56376794ffecb3b19174de6f85/SKILL.md) | 把论文、笔记和网页逐步编译为可交叉引用、可查询、可维护的持久 Markdown 知识库。 |

### 研究设计

| 仓库 / Skill | 用途 |
|---|---|
| [zjYao36/Auto-Research-Refine](https://github.com/zjYao36/Auto-Research-Refine)<br>[research-refine-pipeline](https://github.com/zjYao36/Auto-Research-Refine/blob/a1f14495856afe1e400c65d84ce22f68a027ef75/research-refine-pipeline/SKILL.md) | 把模糊研究方向依次收敛为可评审研究方案和详细实验路线图。 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>[experimental-design](https://github.com/K-Dense-AI/scientific-agent-skills/blob/e12d68309994d5643c7c2ee00ce883f570916b7d/skills/experimental-design/SKILL.md) | 在收集数据前规划随机化、分组、区组、因子设计、重复与混杂控制。 |

### 实验与代码

| 仓库 / Skill | 用途 |
|---|---|
| [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills)<br>[paper-to-code](https://github.com/lingzhi227/agent-research-skills/blob/9e6c085d65e313e475e921fdfe795ac11eb7589e/skills/paper-to-code/SKILL.md) | 按规划、逐文件分析和依赖顺序生成三阶段流程，把机器学习论文转为可运行代码仓库。 |
| [jurgendn/agent-skills](https://github.com/jurgendn/agent-skills)<br>[reproducibility-audit](https://github.com/jurgendn/agent-skills/blob/ff8db273421cd0ec6cde55d84d802a4e9e5fdb26/skills/research-skills/artifact-and-reproducibility/reproducibility-audit/SKILL.md) | 审核代码、数据、配置、随机种子与文档是否足以复现目标结果，并定位断点。 |

### 数据分析

| 仓库 / Skill | 用途 |
|---|---|
| [allenai/asta-plugins](https://github.com/allenai/asta-plugins)<br>[analyze-data](https://github.com/allenai/asta-plugins/blob/1f9d837a48910a28a8f2aee23fc174db891ad234/plugins/asta-tools/skills/analyze-data/SKILL.md) | 用 DataVoyager 多代理流水线针对表格数据执行代码分析、生成图表并回答明确研究问题。 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>[statistical-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/e12d68309994d5643c7c2ee00ce883f570916b7d/skills/statistical-analysis/SKILL.md) | 指导检验选择、假设检查、效应量、功效分析、贝叶斯替代方案与 APA 风格报告。 |

### 论文写作

| 仓库 / Skill | 用途 |
|---|---|
| [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)<br>[research-paper-writing](https://github.com/Master-cai/Research-Paper-Writing-Skills/blob/77e7c2c1ba06f7d71844873147665437a03aac1b/research-paper-writing/SKILL.md) | 为 ML、CV、NLP 论文提供章节结构、段落流、论据对齐和审稿人视角的写作与修订流程。 |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)<br>[nature-writing](https://github.com/Yuan1z0825/nature-skills/blob/4170a8a6262642841699c55d468e21ff70a2fe34/skills/nature-writing/SKILL.md) | 基于作者提供的结论、结果、图表和笔记规划、起草或重构论文章节与整体论证。 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)<br>[ml-paper-writing](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/ml-paper-writing/SKILL.md) | 从研究代码仓组织顶级 ML/AI 会议论文的论证、引用、LaTeX 草稿与 camera-ready 准备。 |
| [Norman-bury/research-writing-skill](https://github.com/Norman-bury/research-writing-skill)<br>[research-writing-assistant](https://github.com/Norman-bury/research-writing-skill/blob/6f7959554b4614d879d79cb4ece9ed04a7c8a88c/SKILL.md) | 以路由、头脑风暴、分章写作、证据驱动引言、实验结果规划、LaTeX、统计和自审模块组织毕业论文与研究文章写作。 |
| [Boom5426/Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills)<br>[paper-workflow](https://github.com/Boom5426/Nature-Paper-Skills/blob/edf232f534d859d3db38b48654f50bfa5023dd90/skills/core/paper-workflow/SKILL.md) | 为 Nature 系列稿件路由初稿搭建、证据链修订、图文同步、统计与引用审计、投稿预检及审稿回复等专用 Skill。 |
| [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer)<br>[scientific-writing](https://github.com/K-Dense-AI/claude-scientific-writer/blob/44414bded0ea850658aac59c014f3d6bec6d1ca8/skills/scientific-writing/SKILL.md) | 通过实时检索、两阶段 IMRAD 写作、引用管理、报告规范、图表与 LaTeX 输出生成论文、综述、基金和科研报告。 |

### 润色与翻译

| 仓库 / Skill | 用途 |
|---|---|
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)<br>[nature-polishing](https://github.com/Yuan1z0825/nature-skills/blob/4170a8a6262642841699c55d468e21ff70a2fe34/skills/nature-polishing/SKILL.md) | 润色、重构或中译英学术文本，并处理 overclaim、语言策略和部分 LaTeX 排版问题。 |
| [wentorai/research-plugins](https://github.com/wentorai/research-plugins)<br>[academic-translation-guide](https://github.com/wentorai/research-plugins/blob/bf44b3cd617fa94c8a1b254c5d1987142ca3d631/skills/writing/polish/academic-translation-guide/SKILL.md) | 提供学术翻译、译后编辑与中式英语修正的流程和检查点。 |

### 引用与 LaTeX

| 仓库 / Skill | 用途 |
|---|---|
| [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills)<br>[bib-search-citation](https://github.com/bahayonghang/academic-writing-skills/blob/1c04e89cbac219661ef026a34ca5805a357d7c21/academic-writing-skills/bib-search-citation/SKILL.md) | 在本地 BibTeX/BibLaTeX 与 Zotero 导出库中检索、筛选并生成 LaTeX 或 Typst 引用片段。 |
| [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills)<br>[latex-paper-en](https://github.com/bahayonghang/academic-writing-skills/blob/1c04e89cbac219661ef026a34ca5805a357d7c21/academic-writing-skills/latex-paper-en/SKILL.md) | 修复英文论文的 LaTeX 编译与格式问题，并检查引用、章节逻辑、表格、伪代码和投稿准备。 |
| [serenakeyitan/citation-check-skill](https://github.com/serenakeyitan/citation-check-skill)<br>[citation-check-skill](https://github.com/serenakeyitan/citation-check-skill/blob/b9deb7077099f56b05c9b6ecea744c2ca0a6d324/SKILL.md) | 先固定提取文档、幻灯片、PDF 或图像中的全部可核验 claim，再逐条用网络或用户文档检查引用存在性、数字和 claim–source 对齐。 |
| [yunshenwuchuxun/latex-paper-skills](https://github.com/yunshenwuchuxun/latex-paper-skills)<br>[paper-from-zero](https://github.com/yunshenwuchuxun/latex-paper-skills/blob/d0f106108cb09e448604a56ce973d35b340cf497/.codex/skills/paper-from-zero/SKILL.md) | 从固定主题建立文献地图、创新与贡献框架、claim–evidence 矩阵和大纲契约，再路由到综述或实证论文的 LaTeX 写作与结果回填流程。 |

### 科研绘图

| 仓库 / Skill | 用途 |
|---|---|
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)<br>[academic-plotting](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/academic-plotting/SKILL.md) | 从论文上下文或实验数据生成架构图与 matplotlib/seaborn 论文图，并自动选择图表类型。 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>[scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/e12d68309994d5643c7c2ee00ce883f570916b7d/skills/scientific-visualization/SKILL.md) | 生成多面板、带误差线与显著性标注、色盲友好并符合期刊规格的投稿级图表。 |

### 投稿前检查

| 仓库 / Skill | 用途 |
|---|---|
| [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills)<br>[paper-audit](https://github.com/bahayonghang/academic-writing-skills/blob/1c04e89cbac219661ef026a34ca5805a357d7c21/academic-writing-skills/paper-audit/SKILL.md) | 对 .tex、.typ 或 .pdf 稿件做审稿人式诊断、投稿门控、阻塞项分级和修订路线图。 |
| [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills)<br>[self-review](https://github.com/lingzhi227/agent-research-skills/blob/9e6c085d65e313e475e921fdfe795ac11eb7589e/skills/self-review/SKILL.md) | 以 NeurIPS 审稿表和三个审稿人角色对 PDF 或 LaTeX 稿件做集成自审与反思修正。 |

### 同行评审与审稿回复

| 仓库 / Skill | 用途 |
|---|---|
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)<br>[academic-paper-reviewer](https://github.com/Imbad0202/academic-research-skills/blob/2aabdf6d56ade6e4e5e52eb468f9c6c4d392988d/academic-paper-reviewer/SKILL.md) | 用主编、三位同行评审者和 Devil's Advocate 等动态角色执行多视角论文评审。 |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)<br>[nature-response](https://github.com/Yuan1z0825/nature-skills/blob/4170a8a6262642841699c55d468e21ff70a2fe34/skills/nature-response/SKILL.md) | 起草、审计或修订逐点审稿回复、rebuttal、修订 cover letter 与标注修改稿片段。 |

### 综合工作流

| 仓库 / Skill | 用途 |
|---|---|
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)<br>[academic-pipeline](https://github.com/Imbad0202/academic-research-skills/blob/2aabdf6d56ade6e4e5e52eb468f9c6c4d392988d/academic-pipeline/SKILL.md) | 编排研究、写作、完整性检查、评审、修订、复审和最终定稿的十阶段流水线。 |
| [ZimoLiao/scholaraio](https://github.com/ZimoLiao/scholaraio)<br>[ScholarAIO skill suite](https://github.com/ZimoLiao/scholaraio/blob/0b1f5536e772bf21ff946e68b7b8eeb032febc40/.claude/skills/setup/SKILL.md) | 为编码 Agent 提供论文库、检索、摄取、知识图谱、科学软件、写作和引用检查的一体化科研工作区。 |
| [TobiasBlask/open-paper-machine](https://github.com/TobiasBlask/open-paper-machine)<br>[Open Academic Paper Machine](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/writing-engine/SKILL.md) | 以 Claude Code 插件编排选题、文献、方法、写作、图表、LaTeX、验证、同行评审和投稿引擎。 |
| [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine)<br>[paper-spine](https://github.com/WUBING2023/PaperSpine/blob/d4529208cda72aa075767611b0265b95b709b550/src/skill/SKILL.md) | 用贡献优先、结果验证贡献和审稿人视角的 12 阶段硬关卡，从材料或已有稿件生成可审计的 LaTeX、PDF、Word、投稿与回复产物。 |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex)<br>[academic-research-suite](https://github.com/Imbad0202/academic-research-skills-codex/blob/73ab70ad071ea51357a52086e705e3b766cbc5b2/skills/academic-research-suite/SKILL.md) | 以 Codex 原生单路由 Skill 编排深度研究、论文写作、评审、完整流水线和实验规划，并保留上游 ARS 的证据、完整性与安全边界。 |
| [LMDHQ-0420/ResearchPilot-Skills](https://github.com/LMDHQ-0420/ResearchPilot-Skills)<br>[ResearchPilot-Skills v2.0 router](https://github.com/LMDHQ-0420/ResearchPilot-Skills/blob/416d9b77e231bdaec2879a5ded12dafa238e0911/skills/ResearchPilot-Skills-zh/research%5BSTART%5D/SKILL.md) | 通过中英双语阶段 Skill 将方向探索、Idea 深化、实验与实现设计、编码迭代以及分章节论文写作串成可恢复的项目文件流程。 |

<!-- CATALOG:END -->

## 贡献

新增或更新条目前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。不要直接手改上面的生成表格：修改 `data/skills.yaml` 后运行：

```bash
python3 scripts/render_readmes.py --write
python3 scripts/validate_data.py
python3 scripts/render_readmes.py --check
```

## 许可证

本仓库的原创清单、文档和脚本采用 [MIT License](LICENSE)。每个第三方项目仍受其自身许可证约束；[data/skills.yaml](data/skills.yaml) 中的许可证元数据不改变上游条款。
