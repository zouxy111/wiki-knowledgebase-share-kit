---
name: knowledge-base-orchestrator
description: 总控技能（Master Skill），自动判断用户需求并调用对应的 skills，全程引导用户完成知识库维护。适合完全新手或想要一站式服务的用户。支持自动检测和安装 Obsidian，自动创建标准文件夹结构。
---

# Knowledge Base Orchestrator（知识库总控）

> **这是什么？** 一个"一键式"总控 skill，你只需要说"帮我整理笔记"，它会自动完成所有步骤。

---

## 核心能力

这是一个 **Orchestrator（总控/编排器）**，你只需要调用一次，它会：

1. ✅ **环境检测**（Environment Detection）
   - 检测 Obsidian 是否安装
   - 检测 vault（知识库文件夹）是否存在
   - 检测 vault profile（知识库配置文件）是否存在

2. ✅ **自动部署**（Auto Deployment）
   - 自动安装 Obsidian（如果用户同意）
   - 自动创建标准文件夹结构
   - 自动生成 vault profile

3. ✅ **智能路由**（Intelligent Routing）
   - 自动判断用户意图
   - 自动调用对应的 skill
   - 全程引导用户

4. ✅ **后续建议**（Follow-up Suggestions）
   - 执行完后给出下一步建议
   - 询问是否需要继续

---

## 使用方式

### 最简单的用法

```text
Use $knowledge-base-orchestrator to help me organize my notes.
```

或者中文：

```text
用 $knowledge-base-orchestrator 帮我整理笔记。
```

### 它会自动做什么

#### 第 1 步：环境检测（Environment Check）

**检测 Obsidian**：
```
Orchestrator：
"正在检测你的系统环境...

❌ 未检测到 Obsidian（黑曜石笔记软件）

Obsidian 是一个强大的 markdown（标记语言）笔记工具，推荐使用。

要我帮你安装吗？
1. 是，自动安装（推荐）
2. 否，我用其他编辑器（VS Code / Typora / Vim 等）
3. 我已经安装了，但在其他位置"
```

**检测 vault（知识库文件夹）**：
```
Orchestrator：
"你的笔记文件夹（vault）在哪里？

常见位置：
1. ~/Documents/my-vault（推荐）
2. ~/Dropbox/notes（云同步）
3. ~/iCloud/notes（iCloud 同步）
4. 自定义路径

如果还没有，我可以帮你创建。"
```

**检测 vault profile（知识库配置文件）**：
```
Orchestrator：
"我发现你还没有 vault profile（知识库配置文件）。

这个文件告诉工具：
- 你的笔记怎么分类（areas，领域分类）
- 导航页面在哪里（root pages，根页面）
- 文件命名规则是什么（naming conventions，命名约定）

我可以帮你自动生成，只需要回答几个问题。"
```

---

#### 第 2 步：自动部署（Auto Deployment）

**安装 Obsidian**（如果用户选择"是"）：

```
Orchestrator：
"好的！正在为你安装 Obsidian（黑曜石笔记软件）...

检测到你的系统是 macOS，使用 Homebrew（包管理器）安装。

[进度] 正在下载... ████████░░░░░░░░ 50%
[进度] 正在安装... ████████████████ 100%

✅ Obsidian 安装完成！
版本：v1.5.3

现在我来帮你创建知识库文件夹（vault）。"
```

**创建标准文件夹结构**：

```
Orchestrator：
"正在创建标准文件夹结构...

✅ 已创建：
  ~/Documents/my-vault/
  ├── index.md          # 导航首页（navigation homepage）
  ├── log.md            # 里程碑日志（milestone log）
  ├── README.md         # 说明文档（documentation）
  ├── .obsidian/        # Obsidian 配置（config）
  └── pages/            # 笔记目录（notes directory）
      ├── project-learning-overview.md   # 学习笔记导航
      ├── project-work-overview.md       # 工作文档导航
      └── governance.md                  # 维护规则（governance rules）

文件夹结构创建完成！"
```

**生成 vault profile（知识库配置文件）**：

```
Orchestrator：
"现在我来帮你生成 vault profile（知识库配置文件）。

请回答几个问题：

1. 你想怎么分类你的笔记？（areas，领域分类）
   推荐：
   - 学习笔记（learning）
   - 工作文档（work）
   - 个人项目（projects）
   
   你可以自定义，用逗号分隔：learning, work, projects"

用户："learning, work, projects"

Orchestrator：
"好的！

2. 你的笔记主要用于？
   - 个人学习
   - 团队协作
   - 产品管理
   - 其他"

用户："个人学习"

Orchestrator：
"明白了！

✅ vault profile（知识库配置文件）已生成：
  ~/Documents/my-vault/my-vault-profile.md

配置内容：
- Vault name（知识库名称）: 我的学习笔记
- Areas（领域分类）: learning, work, projects
- Root pages（根页面/导航页）: 已自动创建
- Frontmatter rules（元数据规则）: 已配置

现在用 Obsidian 打开这个文件夹吗？"
```

---

#### 第 3 步：智能路由（Intelligent Routing）

**判断用户意图**：

```
Orchestrator：
"环境准备完成！

现在你想做什么？

1. 📥 导入一本书/长文档（import long document，长文档导入）
   - 我有一本 markdown 书想导入
   - 我有一份很长的教程想拆分

2. ✍️ 整理现有笔记（organize existing notes，笔记整理）
   - 我有一些零散的笔记想整理
   - 我想把最近的任务结果沉淀进知识库

3. 🔍 检查知识库健康度（audit knowledge base，健康检查）
   - 检查有没有死链（dead links，失效链接）
   - 检查有没有孤立页面（orphan pages，无入口页面）
   - 检查导航是否完整

4. 👥 团队协调（team coordination，多人协作）
   - 我有一个多人项目需要协调
   - 我想给团队成员派发任务并跟踪

5. 🧠 记录协作画像（working profile，协作习惯）
   - 我想记录自己的工作习惯
   - 我想沉淀长期协作经验

6. 📝 写工作记录/日报（work journal，工作日志）
   - 我想写今天的工作记录
   - 我想生成周报

7. 📚 查看使用指南（view guide，使用指南）
   - 我想先了解这套工具怎么用

请选择（输入数字）："
```

**根据选择调用对应 skill**：

##### 选项 1：导入长文档

```
用户："1"

Orchestrator：
"好的！我会调用 knowledge-base-ingest（长文档导入工具）。

请提供：
1. 源文件路径（source file path，文件位置）
2. 这是什么类型的文档？
   - 书籍（book）
   - 教程（tutorial）
   - 技术文档（technical doc）
   - 其他"

用户："./my-book.md, 书籍"

Orchestrator：
"收到！正在分析文件...

文件信息：
- 文件大小：5000 行
- 检测到 50 个章节（chapters，章节）
- 预计拆分成 50 个页面（pages）

开始导入吗？"

用户："是"

Orchestrator：
"正在导入...

[进度] 拆分章节（splitting chapters）... ████████░░░░░░░░ 50%
[进度] 创建导航（creating navigation）... ████████████░░░░ 75%
[进度] 建立链接（building links）... ████████████████ 100%

✅ 导入完成！

已创建：
- 1 个总览页（overview page，概览页）
- 50 个章节页（chapter pages）
- 导航链接（navigation links）
- 相关链接（related links，关联链接）

现在运行 audit（健康检查）吗？"
```

##### 选项 2：整理笔记

```
用户："2"

Orchestrator：
"好的！我会调用 knowledge-base-maintenance（笔记整理工具）。

我会帮你：
1. 过滤临时内容（filter temporary content，过滤临时记录）
2. 按页面角色分类（classify by page roles，按角色分类）
   - project（项目文档）
   - knowledge（知识沉淀）
   - ops（操作手册）
   - task（任务清单）
   - overview（总览页）
3. 更新导航（update navigation，更新导航链接）
4. 更新日志（update log，更新里程碑日志）

请提供要整理的内容：
- 粘贴笔记内容
- 或提供文件路径（file path）"

用户："[粘贴笔记内容]"

Orchestrator：
"收到！正在分析...

内容分析：
- 类型（type）：知识沉淀（knowledge）
- 分类（area）：学习笔记（learning）
- 标签（tags）：python, tutorial

这段内容应该归类为：
- 页面角色（page role）: knowledge
- 分类（area）: learning
- 文件名建议（suggested filename）：python-basics.md

确认吗？"

用户："是"

Orchestrator：
"正在整理...

✅ 已完成：
- 创建页面（created page）：pages/python-basics.md
- 更新导航（updated navigation）：pages/project-learning-overview.md
- 更新日志（updated log）：log.md

现在运行 audit（健康检查）吗？"
```

##### 选项 3：健康检查

```
用户："3"

Orchestrator：
"好的！我会调用 knowledge-base-audit（健康检查工具）。

正在检查...

[进度] 检查元数据（checking metadata）... ████████░░░░░░░░ 25%
[进度] 检查死链（checking dead links）... ████████████░░░░ 50%
[进度] 检查孤立页（checking orphan pages）... ████████████████ 75%
[进度] 检查噪音回流（checking noise regression）... ████████████████ 100%

✅ 检查完成！

【P1 问题】（必须修复，must fix）
- ❌ 发现 3 个死链（dead links，失效链接）
  - pages/old-page.md → 文件不存在
  - pages/deleted.md → 文件不存在

- ❌ 发现 2 个孤立页（orphan pages，无入口页面）
  - pages/random-note.md → 没有导航入口（no navigation entry）
  - pages/temp.md → 没有导航入口

【P2 问题】（建议修复，should fix）
- ⚠️ 5 个页面缺少 frontmatter（元数据，metadata）
- ⚠️ 根目录有 2 个不该存在的 markdown 文件（stray files，游离文件）

【P3 问题】（可选修复，optional fix）
- 💡 部分页面标题不清晰（unclear titles）
- 💡 部分页面标签缺失（missing tags）

要我帮你修复这些问题吗？"
```

##### 选项 4：团队协调

```
用户："4"

Orchestrator：
"好的！我会调用 knowledge-base-team-coordination（团队协调工具）。

请提供：
1. 项目名称
2. 项目描述
3. 需要协调的团队成员数量
4. 项目类型（开发/文档/设计/其他）

收到后我会：
- 生成项目工作区
- 创建对应的成员问卷
- 设置任务跟踪页面"
```

##### 选项 5：协作画像

```
用户："5"

Orchestrator：
"好的！我会调用 knowledge-base-working-profile（协作画像工具）。

这个工具会：
- 从最近的交互中提取你的协作习惯
- 记录决策偏好和边界
- 区分"已确认"和"推断中"的信号

请提供：
1. 你想记录的时间范围（最近一周/一个月/自定义）
2. 是否有特定的协作场景想重点关注？"
```

##### 选项 6：工作记录/日报

```
用户："6"

Orchestrator：
"好的！我会调用 work-journal（工作记录工具）。

请提供：
1. 日期（默认今天）
2. 主要完成的工作项（可逐项输入）
3. 是否有会议纪要？
4. 是否有临时想法想记录？

完成后你可以选择：
- 生成日报
- 生成本周周报
- 查看历史工作记录"
```

##### 选项 7：查看使用指南

```
用户："7"

Orchestrator：
"好的！我会调用 knowledge-base-kit-guide（使用指南）。

这个工具会帮你：
- 了解所有 8 个 skills 的职责
- 查看推荐的学习路径
- 解决配置和使用中的问题

当前可用的 skills：
1. knowledge-base-kit-guide - 使用指南
2. knowledge-base-orchestrator - 总控/一键式（当前使用）
3. knowledge-base-ingest - 长文档导入
4. knowledge-base-maintenance - 知识库维护
5. knowledge-base-audit - 结构审计
6. knowledge-base-team-coordination - 团队协调
7. knowledge-base-working-profile - 协作画像
8. work-journal - 工作记录

有什么具体想了解的？"
```

---

#### 第 4 步：后续建议（Follow-up Suggestions）

```
Orchestrator：
"任务完成！

根据你的知识库状态，我建议：

🔄 日常工作流：
1. 📝 每次写完笔记后运行 work-journal（工作记录）
   - 记录当天的工作和会议纪要
   - 周末可生成周报

2. ✍️ 定期运行 maintenance（笔记整理，每周 1-2 次）
   - 把任务结果沉淀进知识库
   - 确保内容被正确分类和导航

📊 定期检查：
3. 🔍 定期运行 audit（健康检查，每周一次）
   - 检查死链（dead links，失效链接）和孤立页（orphan pages，无入口页面）
   - 保持知识库健康

👥 团队协作：
4. 👥 多人项目开始时运行 knowledge-base-team-coordination（团队协调）
   - 生成成员问卷，对齐后再派单
   - 跟踪任务进度和审批状态

5. 🧠 定期运行 knowledge-base-working-profile（协作画像）
   - 记录长期协作习惯和决策偏好
   - 帮助新成员快速了解团队

📚 学习资源：
6. 查看 GLOSSARY.md（术语表）了解更多概念
7. 查看 examples/（示例文件夹）了解真实案例

还需要我做什么吗？"
```

---

## 工作流程图（Workflow Diagram）

```
用户输入："帮我整理笔记"
  ↓
【环境检测 Environment Check】
  ├─ 检测 Obsidian
  │   ├─ 已安装 → 跳过
  │   └─ 未安装 → 询问是否安装
  │       ├─ 是 → 自动安装
  │       └─ 否 → 继续
  ├─ 检测 vault 文件夹
  │   ├─ 已存在 → 跳过
  │   └─ 不存在 → 自动创建
  └─ 检测 vault profile
      ├─ 已存在 → 跳过
      └─ 不存在 → 引导创建
  ↓
【智能路由 Intelligent Routing】
  ├─ 分析用户意图
  ├─ 询问用户选择（如果不明确）
  └─ 调用对应 skill
      ├─ knowledge-base-ingest（导入长文档）
      ├─ knowledge-base-maintenance（整理笔记）
      ├─ knowledge-base-audit（健康检查）
      ├─ knowledge-base-team-coordination（团队协调）
      ├─ knowledge-base-working-profile（协作画像）
      ├─ work-journal（工作记录）
      └─ knowledge-base-kit-guide（使用指南）
  ↓
【执行任务 Execute Task】
  ├─ 传递参数
  ├─ 监控进度
  └─ 处理错误
  ↓
【后续建议 Follow-up Suggestions】
  ├─ 输出执行报告
  ├─ 给出下一步建议
  └─ 询问是否继续
```

---

## 决策树（Decision Tree）

### 意图识别（Intent Recognition）

```
用户输入包含...
  ├─ "导入" / "书" / "长文档" / "import" / "book"
  │   → 调用 knowledge-base-ingest
  │
  ├─ "整理" / "维护" / "更新" / "organize" / "maintain"
  │   → 调用 knowledge-base-maintenance
  │
  ├─ "检查" / "审计" / "健康" / "audit" / "check"
  │   → 调用 knowledge-base-audit
  │
  ├─ "团队" / "协调" / "多人" / "team" / "coordination"
  │   → 调用 knowledge-base-team-coordination
  │
  ├─ "协作画像" / "working profile" / "协作习惯"
  │   → 调用 knowledge-base-working-profile
  │
  ├─ "工作记录" / "日报" / "journal" / "work log"
  │   → 调用 work-journal
  │
  ├─ "帮助" / "指南" / "怎么用" / "help" / "guide"
  │   → 调用 knowledge-base-kit-guide
  │
  └─ 不明确
      → 询问用户："你想做什么？"
```

---

## 术语表（Glossary）

| 英文术语 | 中文释义 | 说明 |
|---------|---------|------|
| Orchestrator | 总控/编排器 | 负责协调和调用其他 skills 的主控程序 |
| Environment Detection | 环境检测 | 检查系统环境和必要工具是否安装 |
| Auto Deployment | 自动部署 | 自动安装工具和创建文件结构 |
| Intelligent Routing | 智能路由 | 根据用户意图自动选择对应的功能 |
| Vault | 知识库文件夹 | 存放所有笔记的根目录 |
| Vault Profile | 知识库配置文件 | 描述知识库结构的配置文件 |
| Skill | 技能包 | 可被 AI 调用的功能模块 |
| Dead Link | 死链 | 指向不存在文件的链接 |
| Orphan Page | 孤立页面 | 没有导航入口的页面 |
| Frontmatter | 元数据/文件头 | Markdown 文件开头的 YAML 格式信息 |
| Page Role | 页面角色 | 页面的类型分类（project/knowledge/ops/task/overview） |
| Area | 分类/领域 | 知识库的主要分类（如 learning/work/projects） |
| Root Page | 根页/导航页 | 每个分类的主导航页面 |
| Milestone Log | 里程碑日志 | 记录重要变化的日志文件 |
| Navigation | 导航 | 页面之间的链接关系 |
| Audit | 审计/健康检查 | 检查知识库结构和内容质量 |

---

## 相关资源（Related Resources）

- [`GLOSSARY.md`](../../GLOSSARY.md) — 完整术语表
- [`START-HERE.md`](../../START-HERE.md) — 快速上手指南
- [`scripts/detect-obsidian.sh`](./scripts/detect-obsidian.sh) — Obsidian 检测脚本
- [`scripts/install-obsidian.sh`](./scripts/install-obsidian.sh) — Obsidian 安装脚本
- [`scripts/create-vault-structure.sh`](./scripts/create-vault-structure.sh) — 文件夹创建脚本
- [`references/environment-setup.md`](./references/environment-setup.md) — 环境配置详解
