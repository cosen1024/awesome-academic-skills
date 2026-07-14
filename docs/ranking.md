# 科研 Agent Skills 从“夯”到“拉”排名

核验日期：2026-07-13。

这是一份针对用户点名项目的源码审计版推荐榜，不是统一模型、统一论文任务下的盲测榜。所谓“写作质量”主要依据 `SKILL.md` 的写作方法、公开示例、claim–evidence 约束和防编造规则推断；没有公开样例或可复现实验时，不把 README 的“publication-ready”宣传当作已验证结果。

“拉”只表示在这组项目中的相对推荐度低，并不表示项目毫无价值。GitHub Star 和网络讨论只占 10%，热度不能替代科研质量。

## 评分方法

| 维度 | 权重 | 看什么 |
|---|---:|---|
| 科研与写作方法 | 30 | 是否先问题、贡献和证据，是否有清晰的段落、章节和审稿人视角 |
| 证据与防幻觉 | 20 | 引用核验、claim–evidence 映射、结果边界、禁止编造和人工确认点 |
| 工作流完整度 | 15 | 是否覆盖输入、阶段产物、恢复、审计、投稿或回复 |
| Skill 工程质量 | 15 | 路由、渐进加载、脚本、硬关卡、测试、宿主适配和安全边界 |
| 文档与安装 | 10 | README、依赖、安装、卸载、平台差异和限制是否写清楚 |
| 在线公开信号 | 10 | 2026-07-13 的 GitHub 活跃度、Star、公开讨论和第三方分析；不作为学术质量证据 |

等级：S（90–100，夯）· A（80–89，很强）· B（70–79，能用）· C（60–69，挑场景）· D（<60，拉/仅作辅助）。

## 综合排名

| 排名 | 项目 | 分数 | 等级 | 适合什么 | 主要加分项 | 主要扣分项 | Stars |
|---:|---|---:|:---:|---|---|---|---:|
| 1 | [Academic Research Skills for Codex](https://github.com/Imbad0202/academic-research-skills-codex) | 94 | S | Codex 全流程研究、写作、评审与实验规划 | 单入口路由、完整性门、引用与 Material Passport、安全边界、约 260 个测试文件 | 体量和学习成本高；CC BY-NC 4.0 禁止商业使用；Codex 适配仍有上游 Claude 概念映射 | 6,143 |
| 2 | [PaperSpine](https://github.com/WUBING2023/PaperSpine) | 91 | S | 从现有稿件或材料构建可投稿论文 | contribution-first、results-as-validation、12 阶段硬关卡、23 个测试文件、跨四宿主 | 安装器会写多个用户级目录；流程重；部分任务需要 LaTeX、Pandoc 与 GUI intake | 3,997 |
| 3 | [nature-skills](https://github.com/Yuan1z0825/nature-skills) | 89 | A | Nature 风格写作、阅读、图表、引用和回复 | 17 个细分 Skill、按需加载、第一手来源层级、Apache-2.0、持续维护和最高社区采用 | 各 Skill 成熟度不完全一致；不是 Nature 官方项目；部分绘图和检索需要额外环境 | 28,295 |
| 4 | [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | 85 | A | Nature 系列稿件从初稿到返修的专用栈 | journal-first、claim-driven、图文/统计/引用/投稿路由清楚，22 个 Skill | 默认假设偏 Nature，跨领域泛化较弱；自动化测试证据少于前三名 | 358 |
| 5 | [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 83 | A | 计算机与 AI 研究中的 Zotero、Obsidian、实验和写作协作 | question→evidence→experiment→claim 链路，45 个 Skill，知识库与实验产物衔接完整 | 主分支偏 Claude Code，其他宿主分支维护；套件庞大且包含较多通用开发 Skill；安装较侵入 | 4,606 |
| 6 | [latex-paper-skills](https://github.com/yunshenwuchuxun/latex-paper-skills) | 80 | A | ML/AI 的 LaTeX 综述或实证论文 | claim–evidence 矩阵、结果状态、issues 契约、两套公开 PDF 示例，主题到 PDF 路径具体 | 上游明确承认测试覆盖有限；主要针对 IEEE/ML 风格；LaTeX 和跨模型工具链较重 | 228 |
| 7 | [Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | 78 | B | ML/CV/NLP 章节写作和段落修订 | 一段一事、reverse outline、claim–evidence map、审稿人视角，短小易用 | 只有一个主 Skill；没有公开测试或成套输出基准；不负责完整科研运行时 | 5,068 |
| 8 | [literature-survey-skill](https://github.com/SNL-UCSB/literature-survey-skill) | 75 | B | 10–150 篇论文的深度综述和领域学习 | Intent→Triage→Deepen→Synthesize 设计很强，强制校准、分层阅读、依赖图和缺口矩阵 | 强依赖 NotebookLM 与账户认证；论文需上传；无测试和统一输出样例；维护历史短 | 43 |
| 9 | [research-writing-skill](https://github.com/Norman-bury/research-writing-skill) | 72 | B | 中文毕业论文和多学科模块化写作 | 入口路由、证据写作、实验/结果规划、LaTeX、统计和自审模块完整，多平台适配 | “所有任务都先计划/头脑风暴”等规则偏僵硬；自动化验证证据有限；与 ResearchPilot 并非可核验的同一仓库 | 2,775 |
| 10 | [ResearchPilot-Skills](https://github.com/LMDHQ-0420/ResearchPilot-Skills) | 70 | B | 中文计算型科研从方向到代码和分章节写作 | 中英双语、16 个阶段入口、文件化状态和 Claude/Codex/CodeBuddy 安装脚本 | v2.0 较新、没有测试文件；阶段命名与“七阶段”表述略复杂；公开独立分析较少 | 148 |
| 11 | [claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 68 | C | 需要 Python CLI/API、基金、海报和多格式输出的团队 | 有实际 Python 包、插件、28 个 Skill、持续维护和 API/CLI 接口 | 核心规则强制大量 AI 生成图，不适合所有论文；依赖 Anthropic/Parallel 等 API；公开研究论文示例不足 | 2,093 |
| 12 | [citation-check-skill](https://github.com/serenakeyitan/citation-check-skill) | 58 | D | 生成后做 claim 清点和人工核验清单 | 两遍结构、claim 固定、文档限定模式和结果状态表简单直接 | 联网 LLM 流程并非真正确定性；把任何四舍五入都判错过于机械；无脚本、测试或可复现准确率基准 | 191 |

## 场景纠偏

综合榜会惩罚窄工具，但窄工具在对应任务上可能更好：

- 只做系统性文献梳理：优先 `literature-survey-skill`，其单项可进 A 档。
- 只改 ML/CV/NLP 论文结构和段落：`Research-Paper-Writing-Skills` 比大套件更轻。
- 已有材料或旧稿，希望形成全套可审计产物：优先 PaperSpine。
- Codex 中跑完整研究—写作—评审闭环：优先 ARS Codex。
- Nature 系列稿件：先选 `nature-skills`；需要更强 journal-first 路由时叠加 `Nature-Paper-Skills`，不要把两套全部无脑加载。
- Zotero + Obsidian + 计算实验：Claude Scholar 更顺手。
- 中文毕业论文：旧 `research-writing-skill` 更成熟；ResearchPilot 的方向→代码→写作衔接更明确，但仍需观察 v2 稳定性。
- `citation-check-skill` 适合作为核验清单，不应代替 Crossref、OpenAlex、Semantic Scholar、原文逐页检查或人工判断。

## 网络分析如何使用

技术事实仍以仓库 README、`SKILL.md`、许可证和固定提交为准。以下二手材料只用于观察公开讨论重点，权重很低：

- ARS 的独立介绍普遍强调 human-in-the-loop 与完整性门：[EZPZ AI](https://ezpzai.com/en/2026-05-18-imbad0202-academic-research-skills-en/)、[TechJupJup](https://techjupjup.com/ko/guide/academic-research-skills-guide/)。
- `nature-skills` 的外部分析强调它是任务拆分与证据约束集合，而非 Nature 官方写作器：[0xpanda alpha lab](https://note.com/panda_lab/n/n3f50720b451c)。
- PaperSpine 与 Claude Scholar 的第三方概览支持其“完整流程、审计轨迹、Zotero/Obsidian 集成”的定位：[PaperSpine overview](https://whatisgithub.com/wubing2023/paperspine)、[Claude Scholar overview](https://gitwtfhub.com/galaxy-dawn/claude-scholar)。
- `latex-paper-skills` 的外部介绍认为它更适合已有 LaTeX 工作流的作者：[Agent2Research](https://agent2research.com/tools/latex-paper-skills-ai-latex-writing-management)。
- `claude-scientific-writer` 的公开讨论既认可其检索与迭代，也有人质疑推广性指令；本榜以当前源码中仍存在的强制生图和 API 依赖为主要扣分依据：[Reddit discussion](https://www.reddit.com/r/ClaudeAI/comments/1oim7ly/claude_scientific_writer_write_anything_with/)。
- `citation-check-skill` 的公开讨论证明需求真实，但没有提供准确率或可重复基准：[Reddit discussion](https://www.reddit.com/r/ClaudeAI/comments/1qn179k/built_a_citation_checker_skill_because_ai_slides/)。

## 限制

- 未在同一模型、同一论文和同一数据集上逐项运行，因此分数不是输出质量实测。
- Star 可能受曝光、发布时间和社区传播影响。
- 仓库快速更新后，评分可能失效；固定源码依据见 `data/skills.yaml`。
- 未执行安全审计，也未把任何项目认定为可自动提交论文的系统。
