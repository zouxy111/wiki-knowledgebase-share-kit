# 术语表 / Glossary

> 这个文档解释项目中的核心概念，帮助新手快速理解。
> 文中若出现文件名或路径示例，默认用于解释概念；除非明确写成仓库链接，否则不代表这些文件真实存在于本仓库。

---

## 核心概念

### Vault（知识库）
你的 markdown 笔记存放的文件夹。
- **Obsidian 用户**：就是你的 Obsidian vault 文件夹
- **普通用户**：就是你存放 `.md` 文件的根目录
- **示例**：`/Users/yourname/Documents/my-notes`

### Skill（技能包）
一个可以被 AI 助手调用的工具包，包含特定功能的说明和脚本。
- **类比**：就像给 AI 安装一个"插件"
- **本项目当前提供 10 个 skills**：kit-guide、orchestrator、ingest、maintenance、audit、project-management、team-coordination、delivery-audit、working-profile、work-journal

### Vault Profile（知识库配置文件）
描述你的知识库结构的配置文件，告诉工具：
- 你的笔记放在哪里
- 有哪些分类（areas）
- 导航页面是哪些
- 文件命名规则是什么

**类比**：就像给你的知识库写一份"说明书"

---

## 5 种页面角色（Page Roles）

这套工具把所有笔记分成 5 种固定角色，每种角色有明确的用途：

### 1. `project`（项目文档）
**用途**：导航页、项目总览、长期边界说明

**适合放什么**：
- ✅ 产品需求文档总览
- ✅ 技术方案导航页
- ✅ 项目里程碑和边界说明

**不适合放什么**：
- ❌ 每日任务记录
- ❌ 详细执行过程
- ❌ 临时想法

**真实例子**：
```markdown
---
title: "移动端产品需求总览"
type: "project"
area: "product"
---

# 移动端产品需求总览

## 当前版本
- v2.3（2026-04-15 发布）

## 核心功能模块
- 示例文件名：`user-login.md`
- 示例文件名：`payment-flow.md`
- 示例文件名：`push-notification.md`

## 技术边界
- 最低支持 iOS 14+
- 最低支持 Android 8.0+
```

---

### 2. `knowledge`（知识沉淀）
**用途**：概念解释、方法论、技术指南、可复用的知识

**适合放什么**：
- ✅ React Hooks 使用指南
- ✅ 数据库设计原则
- ✅ 产品设计方法论
- ✅ 编程语言学习笔记

**不适合放什么**：
- ❌ "今天学了 React"这种流水账
- ❌ 具体项目的执行细节
- ❌ 临时调试记录

**真实例子**：
```markdown
---
title: "React Hooks 最佳实践"
type: "knowledge"
area: "engineering"
tags: ["react", "frontend", "hooks"]
updated: "2026-04-15"
---

# React Hooks 最佳实践

## 核心原则
1. 只在顶层调用 Hooks
2. 只在 React 函数中调用 Hooks

## 常用 Hooks 对比
| Hook | 用途 | 何时使用 |
|------|------|----------|
| useState | 状态管理 | 组件内部状态 |
| useEffect | 副作用 | API 调用、订阅 |
| useContext | 跨组件传值 | 避免 prop drilling |

## 实战案例
...
```

---

### 3. `ops`（操作手册）
**用途**：排障手册、操作流程、运维文档

**固定结构**（推荐）：
1. **现象**：出现了什么问题
2. **根因**：为什么会出现
3. **处理法**：怎么解决
4. **边界**：什么情况下适用

**适合放什么**：
- ✅ 服务器宕机排查手册
- ✅ 数据库备份流程
- ✅ 部署操作步骤
- ✅ 常见错误解决方案

**不适合放什么**：
- ❌ "2026-04-15 修了一个 bug"这种日志
- ❌ 单次操作的完整记录

**真实例子**：
```markdown
---
title: "Redis 连接超时排查手册"
type: "ops"
area: "operations"
tags: ["redis", "troubleshooting"]
updated: "2026-04-15"
---

# Redis 连接超时排查手册

## 现象
应用日志出现 `RedisConnectionException: Connection timeout`

## 根因
1. Redis 服务未启动
2. 防火墙阻止了 6379 端口
3. Redis 配置的 `bind` 地址不正确
4. 网络延迟过高

## 处理法
### 步骤 1：检查 Redis 服务状态
```bash
systemctl status redis
```

### 步骤 2：检查端口连通性
```bash
telnet redis-host 6379
```

### 步骤 3：检查配置文件
...

## 边界
- 适用于 Redis 5.0+
- 仅限 Linux 环境
```

---

### 4. `task`（任务清单）
**用途**：待办事项、协作分工、进行中的任务

**适合放什么**：
- ✅ 本周待办事项
- ✅ 项目任务分工
- ✅ Bug 修复清单

**不适合放什么**：
- ❌ 长期知识（应该放到 `knowledge`）
- ❌ 已完成的历史任务（应该归档或删除）

**真实例子**：
```markdown
---
title: "Q2 产品开发任务清单"
type: "task"
area: "product"
updated: "2026-04-15"
---

# Q2 产品开发任务清单

## 进行中
- [ ] 用户登录模块重构（@张三，预计 4/20 完成）
- [ ] 支付流程优化（@李四，预计 4/25 完成）

## 待开始
- [ ] 消息推送功能（@王五）

## 已完成
- [x] 数据库迁移（@张三，4/10 完成）
```

---

### 5. `overview`（总览页）
**用途**：知识库导航、治理规则、维护说明

**适合放什么**：
- ✅ 知识库首页（index.md）
- ✅ 维护规则说明
- ✅ 分类索引页

**真实例子**：
```markdown
---
title: "知识库导航"
type: "overview"
area: "governance"
---

# 知识库导航

## 主要分类
- 示例路径：`pages/project-product-overview.md`
- 示例路径：`pages/project-engineering-overview.md`
- 示例路径：`pages/project-operations-overview.md`

## 维护规则
- 每个页面必须有 frontmatter
- 新增页面必须加入导航
- 每月审计一次结构
```

---

## 其他术语

### Frontmatter（文件头部元数据）
Markdown 文件开头用 `---` 包裹的 YAML 格式信息。

**示例**：
```yaml
---
title: "我的笔记"
type: "knowledge"
area: "learning"
tags: ["python", "tutorial"]
updated: "2026-04-15"
---
```

**作用**：
- 让工具知道这个文件的类型、分类、标签
- 方便搜索和管理

---

### Area（领域/分类）
你的知识库的主要分类，比如：
- `product`（产品）
- `engineering`（工程）
- `operations`（运维）
- `research`（研究）

**类比**：就像图书馆的"文学类"、"科技类"、"历史类"

---

### Root Page（根页面）
每个 area 的主导航页面，是进入该分类的入口。

**示例**：
- `product` area 的 root page：`project-product-overview.md`
- `engineering` area 的 root page：`project-engineering-overview.md`

---

### Dead Link（死链）
指向不存在文件的链接。

**示例**：
```markdown
`./not-exist.md` ← 这是示例性路径；如果链接指向的目标不存在，就是死链
```

---

### Orphan Page（孤立页面）
没有任何入口链接指向的页面，用户无法通过导航找到。

**问题**：写了内容但找不到，等于白写。

---

### Noise Regression（噪音回流）
临时过程、流水账、低价值内容重新混入知识库。

**示例**：
- ❌ 在知识页里写"今天调试了 3 小时"
- ❌ 在项目总览里贴完整的聊天记录

---

### Milestone Log（里程碑日志）
只记录重要变化的日志文件（通常是 `log.md`）。

**应该记录**：
- ✅ 2026-04-15：完成产品 v2.0 重构
- ✅ 2026-03-20：迁移到新数据库架构

**不应该记录**：
- ❌ 2026-04-15：修了一个小 bug
- ❌ 2026-04-14：开了个会

---

## 快速对照表

| 我想写... | 应该用什么角色？ |
|----------|----------------|
| 项目需求文档 | `project` |
| React 学习笔记 | `knowledge` |
| 服务器宕机排查手册 | `ops` |
| 本周待办事项 | `task` |
| 知识库首页 | `overview` |
| 数据库设计原则 | `knowledge` |
| 部署操作步骤 | `ops` |
| Bug 修复清单 | `task` |
| 产品功能导航 | `project` |

---

## 还有疑问？

- 查看 [`examples/`](./examples/) 文件夹里的真实示例
- 阅读 [`docs/customization-guide.md`](./docs/customization-guide.md)
- 在 [GitHub Issues](https://github.com/zouxy111/wiki-knowledgebase-share-kit/issues) 提问
