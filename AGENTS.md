# AGENTS.md

本仓库维护一份可公开发布、可机器校验的科研 Agent Skills 清单。

## 数据与文档

- `data/skills.yaml` 是条目事实的唯一来源；不要只改 README 表格。
- `README.md` 与 `README_EN.md` 的清单区由 `scripts/render_readmes.py` 生成。
- `docs/candidates.md` 保存待核验、暂缓或明确排除的候选，不应混入已验证主清单。
- 技术事实只采用项目自己的 GitHub README、`SKILL.md`、官方文档或官方安装入口。

## 收录规则

1. 仓库必须公开可访问，且能定位到公开源码、`SKILL.md` 或插件清单。
2. 不收录只有宣传页、产品落地页或无法审阅实现的服务。
3. 每项必须包含用途、平台、安装或入口、许可证、验证状态和核验日期。
4. `verified` 只表示源码与入口已核验，不代表执行测试、安全审计或学术质量背书。
5. 新增条目时保持 13 个科研工作流分类均有覆盖；只扩充有固定版本源码与第一手安装文档的高置信条目。
6. 第三方项目的名称、许可证和限制应按上游原文记录，不把本仓库的 MIT 许可证延伸到第三方内容。

## 修改与验证

修改前先运行 `git status --short`，保留已有未提交改动。完成后运行：

```bash
python3 scripts/validate_data.py
python3 scripts/render_readmes.py --check
python3 scripts/check_links.py --scope source
git status --short
```

如需重新生成 README：

```bash
python3 scripts/render_readmes.py --write
```

不要在仓库中记录 token、Cookie、账号凭据或私有服务地址。未经用户明确要求，不创建远程、不推送。
