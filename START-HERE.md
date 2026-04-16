# START HERE — 5 分钟快速上手

> **完全新手？** 这份文档会带你从零开始，5 分钟内跑通第一个示例。

---

## ⚠️ 开始前的准备（必读）

### 你需要先安装这些工具

这套工具需要配合 AI 助手使用，目前支持：

| AI 平台 | 是否支持 | 安装位置 |
|---------|---------|---------|
| **Codex** | ✅ 推荐 | `~/.codex/skills/` |
| **Claude Code** | ✅ 推荐 | `~/.claude/skills/` |
| **ChatGPT（支持 SKILL.md 的版本）** | ✅ 可用 | 按平台文档配置 |
| **其他平台** | ⚠️ 需自行适配 | - |

**如果你还没有安装 Codex 或 Claude Code**：
1. Codex 安装：[https://codex.ai](https://codex.ai)（示例链接，请替换为真实链接）
2. Claude Code 安装：[https://claude.ai/code](https://claude.ai/code)（示例链接，请替换为真实链接）

**如果你不想安装 AI 工具**：
- 你仍然可以手动使用这套方法，参考 [`docs/usage-sop.md`](./docs/usage-sop.md) 里的 checklist

---

## 📚 第一步：理解核心概念（2 分钟）

在开始之前，先快速了解 3 个核心概念：

### 1. 什么是 Skill？
**Skill = 给 AI 安装的”插件”**，让 AI 知道怎么帮你整理笔记。

本项目提供 4 个 skills：
- 📖 `knowledge-base-kit-guide` — 使用指南（新手先用这个）
- 📥 `knowledge-base-ingest` — 导入长文档/书籍
- ✍️ `knowledge-base-maintenance` — 整理笔记到知识库
- 🔍 `knowledge-base-audit` — 检查知识库健康度

### 2. 什么是 Vault？
**Vault = 你的笔记文件夹**
- Obsidian 用户：就是你的 Obsidian vault
- 普通用户：就是你存放 `.md` 文件的文件夹

### 3. 什么是 Vault Profile？
**Vault Profile = 你的知识库”说明书”**，告诉工具：
- 你的笔记放在哪里（路径）
- 有哪些分类（areas）
- 导航页面是哪些（root pages）

**👉 更多概念解释，请看：[`GLOSSARY.md`](./GLOSSARY.md)**

---

## 🚀 第二步：安装 Skills（1 分钟）

### 方法 1：使用 Codex 或 Claude Code

1. **复制 4 个 skill 文件夹**到你的 skills 目录：

```bash
# 如果你用 Codex
cp -r skills/knowledge-base-kit-guide ~/.codex/skills/
cp -r skills/knowledge-base-ingest ~/.codex/skills/
cp -r skills/knowledge-base-maintenance ~/.codex/skills/
cp -r skills/knowledge-base-audit ~/.codex/skills/

# 如果你用 Claude Code
cp -r skills/knowledge-base-kit-guide ~/.claude/skills/
cp -r skills/knowledge-base-ingest ~/.claude/skills/
cp -r skills/knowledge-base-maintenance ~/.claude/skills/
cp -r skills/knowledge-base-audit ~/.claude/skills/
```

2. **验证安装**：
   - 打开 Codex/Claude Code
   - 输入：`list skills` 或 `show available skills`
   - 应该能看到 4 个新 skills

### 方法 2：手动使用（不安装 AI 工具）

如果你不想用 AI 工具，可以：
1. 阅读 [`docs/usage-sop.md`](./docs/usage-sop.md) 里的 checklist
2. 手动按照规则整理笔记

---

## ⚙️ 第三步：配置你的 Vault Profile（2 分钟）

1. **复制模板**：
```bash
cp templates/vault-profile-template.md my-vault-profile.md
```

2. **填写最小配置**（只需填这 5 项）：

打开 `my-vault-profile.md`，填写：

```yaml
## 1. Vault identity

- Vault name: 我的笔记本                    # 随便起个名字
- Vault root path: /Users/yourname/Documents/my-notes  # 你的笔记文件夹路径
- Primary markdown page directory: /Users/yourname/Documents/my-notes/pages  # 笔记存放目录
- Reader entrypoint file: /Users/yourname/Documents/my-notes/index.md  # 导航首页
- Milestone log file: /Users/yourname/Documents/my-notes/log.md  # 日志文件
```

**💡 不知道怎么填？** 看这个完整示例：[`examples/example-vault-profile-generic.md`](./examples/example-vault-profile-generic.md)

---

## ✅ 第四步：验证安装（30 秒）

在 Codex/Claude Code 里输入：

```text
Use $knowledge-base-kit-guide to help me verify my setup.
My vault profile is at: ./my-vault-profile.md
```

AI 会检查你的配置是否正确，并告诉你下一步该做什么。

---

## 🎯 第五步：第一次使用（1 分钟）

### 场景 A：整理一段笔记到知识库

```text
Use $knowledge-base-maintenance to organize this content into my knowledge base.
Read my vault profile at ./my-vault-profile.md first.

Content to organize:
[粘贴你的笔记内容]
```

### 场景 B：检查知识库健康度

```text
Use $knowledge-base-audit to check my knowledge base.
Read my vault profile at ./my-vault-profile.md first.
```

### 场景 C：导入一本 markdown 书

```text
Use $knowledge-base-ingest to import this markdown book.
Read my vault profile at ./my-vault-profile.md first.
Source file: ./my-book.md
```

---

## 🆘 遇到问题？

### 问题 1：提示 "skill not found"
**原因**：skills 没有正确安装到目标目录

**解决**：
1. 检查路径是否正确：`ls ~/.codex/skills/` 或 `ls ~/.claude/skills/`
2. 确认 4 个文件夹都复制过去了
3. 重启 Codex/Claude Code

### 问题 2：提示 "vault profile not found"
**原因**：profile 文件路径不对

**解决**：
1. 确认 `my-vault-profile.md` 在当前目录
2. 使用绝对路径：`/full/path/to/my-vault-profile.md`

### 问题 3：不知道该填什么
**解决**：
1. 先看 [`GLOSSARY.md`](./GLOSSARY.md) 理解概念
2. 参考 [`examples/example-vault-profile-generic.md`](./examples/example-vault-profile-generic.md)
3. 在 [GitHub Issues](https://github.com/zouxy111/wiki-knowledgebase-share-kit/issues) 提问

---

## 📖 下一步学习

安装完成后，建议按顺序阅读：

1. **[`GLOSSARY.md`](./GLOSSARY.md)** — 理解 5 种页面角色（project/knowledge/ops/task/overview）
2. **[`docs/example-prompts.md`](./docs/example-prompts.md)** — 更多使用示例
3. **[`docs/customization-guide.md`](./docs/customization-guide.md)** — 进阶定制
4. **[`examples/`](./examples/)** — 真实场景示例

---

## 💬 中文快速命令（复制即用）

### 第一次使用（验证安装）
```text
用 $knowledge-base-kit-guide 帮我验证安装。
我的 vault profile 在：./my-vault-profile.md
```

### 整理笔记到知识库
```text
用 $knowledge-base-maintenance 把这段内容整理进我的知识库。
先读取 vault profile：./my-vault-profile.md

要整理的内容：
[粘贴你的笔记]
```

### 检查知识库健康度
```text
用 $knowledge-base-audit 审计我的知识库。
先读 vault profile：./my-vault-profile.md
检查死链、孤立页、metadata、页面边界漂移、噪音回流。
```

### 导入长文档/书籍
```text
用 $knowledge-base-ingest 把这本 markdown 书导入我的知识库。
先读 vault profile：./my-vault-profile.md
源文件：./my-book.md
```

---

## 🎓 完整学习路径

如果你想深入了解这套方法：

### 新手路径（1 小时）
1. ✅ 读完本文档（5 分钟）
2. 📖 阅读 [`GLOSSARY.md`](./GLOSSARY.md)（10 分钟）
3. 📝 填写 vault profile（15 分钟）
4. 🧪 跑一次 audit 验证（5 分钟）
5. ✍️ 整理一段笔记试试（15 分钟）
6. 📚 看完 [`docs/example-prompts.md`](./docs/example-prompts.md)（10 分钟）

### 进阶路径（3 小时）
1. 📖 阅读 [`docs/customization-guide.md`](./docs/customization-guide.md)
2. 📖 阅读 [`docs/usage-sop.md`](./docs/usage-sop.md)
3. 🔍 研究 [`examples/`](./examples/) 里的真实案例
4. ⚙️ 定制自己的 areas 和 root pages
5. 🔧 调整 frontmatter 规则

---

## 📌 核心原则（记住这 5 条）

1. **知识库优先**：只保留长期有用的内容，过滤掉临时过程
2. **页面角色清晰**：每个页面必须是 project/knowledge/ops/task/overview 之一
3. **导航必须完整**：每个页面都要能从首页找到
4. **里程碑日志**：log.md 只记录重要变化，不记录流水账
5. **定期审计**：每月至少跑一次 audit，检查结构健康度

---

## 🤝 需要帮助？

- 💬 [GitHub Issues](https://github.com/zouxy111/wiki-knowledgebase-share-kit/issues) — 提问和反馈
- 📖 [完整文档](./README.md) — 查看详细说明
- 📧 联系开发者：邹星宇、杨琦

---

## ✨ 快速对照：我该用哪个 skill？

| 你想做什么 | 用哪个 skill |
|-----------|-------------|
| 第一次安装，不知道怎么开始 | `knowledge-base-kit-guide` |
| 把一段笔记整理进知识库 | `knowledge-base-maintenance` |
| 导入一本 markdown 书 | `knowledge-base-ingest` |
| 检查知识库有没有死链、孤立页 | `knowledge-base-audit` |
| 记录今天的会议或工作 | `work-journal` |
| 不知道该用哪个 | `knowledge-base-kit-guide` |

---

## 📝 工作记录命令（可选功能）

### 记录会议
```text
用 $work-journal 记录今天的会议：
- 时间: 09:00 - 10:30
- 项目: 项目A启动会
- 参会人: 张三、李四
- 会议录音: ~/sources/meetings/2026-04-17.mp3
```

### 保存临时想法
```text
用 $work-journal 记录一个想法：
"能否用 TPM 的 OEE 概念衡量实验室设备利用率？"
```

### 生成工作总结
```text
用 $work-journal 生成本月工作总结，时间范围 2026-04-01 ~ 2026-04-30
```

### 周期沉淀
```text
用 $work-journal 执行本周沉淀
```

---

**🎉 恭喜！你已经完成了快速上手。现在可以开始整理你的笔记了！**
