# DELIVERY NOTES

## 这份包适合直接发给谁

适合发给：
- 自己维护 markdown/wiki 知识库的人
- 已经在用 Codex / Claude / OpenClaw / Hermes / 类似 skills 目录机制的人
- 想把“日志式 wiki”收敛成“知识库式 wiki”的个人或团队
- 想在共享项目目录上跑多人协同、问卷派单、决策蒸馏的人
- 想给项目 owner 一套 milestone / blocker / delivery gate 工作面的团队

## 发出去时最少要说的话

你可以直接附这句话：

```text
这是一个可复用的 10-skill wiki/markdown 知识库维护 + 协作包。
先看 START-HERE.md，再复制 10 个 skills，填好 vault-profile-template.md。
默认先走知识库维护主线；如果需要项目管理 / 周计划 / 里程碑 / 多人协同 / ready 审计，再按需启用 project-management 主线。
```

## 这份包的交付边界

它已经包含：
- 10 个可安装 skill bundle
- 安装与配置说明
- vault profile / working profile / journal / member capability 模板
- PM area 模板族（portfolio / execution / risk / decision / delivery gates）
- 多人协同 team-project 模板
- 示例 profile 与 case study
- 使用提示词示例
- 核心概念术语表（`GLOSSARY.md`）
- Orchestrator 初始化脚本（环境检查、骨架创建、profile 生成）

它不包含：
- 针对所有 AI 平台的统一安装器
- 针对某个业务领域的强绑定 area/root page 预设
- 平台私有 API 适配层
- 完整的“万能自动代理”式后续治理

## 默认假设

- 使用者愿意先填写自己的 vault profile
- 使用者接受固定页面角色模型：`project / knowledge / ops / task / overview`
- 使用者可以自己决定 area / root pages / frontmatter 扩展项
- 使用者理解 Orchestrator 是初始化入口，不是全自动后续治理系统
- 使用者理解 PM 主线是**渐进式加载**，不是第一次使用就必须全部配置

## 建议转发方式

优先让对方先看：
- `START-HERE.md` — 5 分钟快速上手
- `GLOSSARY.md` — 核心概念解释
- `COVER-CN.md` — 中文封面说明（可选）
- `docs/project-management-workflow.md` — 只有当对方明确需要 PM 主线时

如果只想附一句话，就用 `COVER-CN.md` 末尾那段转发文案。
