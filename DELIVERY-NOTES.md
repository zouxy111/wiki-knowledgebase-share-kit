# DELIVERY NOTES

## 这份包适合直接发给谁

适合发给：
- 自己维护 markdown/wiki 知识库的人
- 已经在用 Codex / Claude / OpenClaw / Hermes / 类似 agent runtime 的人
- 想把“日志式 wiki”收敛成“知识库式 wiki”的团队
- 想把长文档导入做成 baseline → candidate → regression → promote 回路的人
- 想把 2 人及以上共享项目目录做成可问卷、可对齐、可派单、可蒸馏工作流的人
- 想让每位成员在自己的 wiki / 个人 agent 里并行工作，但最终统一同步回共享目录的人

## 发出去时最少要说的话

你可以直接附这句话：

```text
这是一个可复用的 wiki/markdown 知识库导入 + 维护 + 审计 + 多人协同分享包。
先看 START-HERE.md，再复制 5 个 skills。
如果你是知识库场景，先填 vault-profile-template.md；
如果你是多人协同场景，先复制 team-project-workspace 模板。
这套协作模式主推在 OpenClaw / Hermes 上运行，也适合把共享项目目录放到 NAS、网盘或共享 wiki 下同步。
```

## 这份包的交付边界

它已经包含：
- 可安装 skill
- 安装与配置说明
- vault profile 模板
- ingest iteration log 模板
- team project workspace 模板
- member capability profile 模板
- 示例 profile / 示例项目
- 使用口令示例
- 核心概念术语表（`GLOSSARY.md`）
- 协作接入模式说明文档
- ingest evaluation rubric

它不包含：
- 自动生成 profile 或 workspace 的脚本
- 针对某个平台的专用 installer
- 针对某个业务领域的唯一角色预设
- 多个成员各自独立 AI 的复杂编排系统

## 默认假设

- 使用者愿意先填写自己的 vault profile 或共享项目目录
- 使用者接受固定页面角色模型：`project / knowledge / ops / task / overview`
- 使用者可以自己决定 area / root pages / frontmatter 扩展项
- 使用者接受 ingest 先落 baseline，再比较 candidate，再决定是否 promote
- 使用者接受多人协同默认由单协调 AI 驱动
- 使用者接受 `draft / approved / superseded / blocked` 的状态门槛
- 使用者接受 shared project directory 才是正式协作事实源
- 使用者可以让每位成员在自己的个人 wiki 中，借助自己的 agent（如 OpenClaw / Hermes）并行准备内容

## 建议转发方式

优先让对方先看：
- `COVER-CN.md`
- `START-HERE.md`
- `GLOSSARY.md`
- `docs/collaboration-integration-patterns.md`
- `docs/team-coordination-workflow.md`
- `docs/ingest-evaluation-rubric.md`

如果只想附一句话，就用上面的转发文案。
