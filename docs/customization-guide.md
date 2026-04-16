# Customization Guide

## 目标

把这套分享包从“通用方法包”适配到你自己的 markdown/wiki 知识库，或适配到你自己的多人协同项目目录。

这套方法默认保留固定页面角色模型：
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

你真正要改的是：
- 路径
- area
- root pages
- 文件布局
- frontmatter 约束
- team project 目录路径
- 成员画像路径
- 共享项目的角色命名

---

## 第 1 步：先填写 vault profile（知识库维护 / 审计 / 可选同步）

复制：
- `templates/vault-profile-template.md`

填写至少这些字段：
- vault root
- pages directory
- reader entrypoint
- milestone log
- maintainer entrypoint
- allowed page roles
- area list
- root page table
- canonical root-level markdown files
- frontmatter schema
- naming conventions

如果这些没填，maintenance 和 audit 都无法稳定落地。
如果你还想把多人协同的稳定结果同步回知识库，也同样需要这份 profile。

---

## 第 2 步：定义你的 root pages

root page 是你的知识库主线入口。

推荐每个 area 至少有一个 root page，并明确：
- area 名
- 对应 root page 文件名
- 该 root page 的职责

例如：
- 产品文档主线
- 技术运维主线
- 研究资料主线
- 协作任务主线

不要求你沿用任何特定命名，但必须在 profile 里写清楚映射关系。

---

## 第 3 步：确认 frontmatter 规则

这套模板默认要求每个内容页有稳定 frontmatter。

推荐至少包含：
- `title`
- `type`
- `area`
- `tags`
- `updated`

如果你的 vault 还需要：
- `status`
- `owner`
- `created`
- `aliases`

也可以放进自己的 profile。

---

## 第 4 步：确认根目录允许出现哪些 markdown 文件

这是为了让 audit 能正确识别 **root-level stray markdown artifacts**。

你需要在 profile 里写清楚：
- 哪些 markdown 文件允许直接放在 vault 根目录
- 其他 markdown 文件是否都应该进 `pages/` 或其它指定目录

常见允许项可能是：
- `index.md`
- `log.md`
- `schema.md`
- `prompts.md`
- `README.md`

如果 profile 没有这条，审计无法稳定判断“根目录历史残片”。

---

## 第 5 步：尽量不要改的核心原则

如果你希望这套方法真的有效，尽量不要改掉：

### A. 知识库优先
- 默认不把一次性运行过程写进主叙事
- 只沉淀长期可检索的知识、规则、边界、排障经验

### B. 页面角色清晰
- `project`：导航 + 稳定总览
- `knowledge`：结构、概念、方法、判断框架
- `ops`：流程、排障、版本边界、回归方法
- `task`：分工、协同、回填顺序
- `overview`：治理、索引、全库入口

### C. 里程碑日志
- `log.md` 只写结构变化和治理变化
- 不写任务回放

---

## 第 6 步：如果你要启用多人协同，先复制共享项目目录模板

复制：
- `templates/team-project-workspace/`

该模板默认约定：

```text
team-project/
  project-brief.md
  team-roster.md
  shared-materials/
  members/
    <member-id>/
      member-context.md
      materials/
      questionnaire.md
      response.md
      assignment.md
      progress-update.md
      decision-distill.md
  coordination/
    alignment-summary.md
    task-board.md
    decision-register.md
    status.md
```

这套目录是多人协同的**公开接口**，不要随意改成难以预测的自由结构。

---

## 第 7 步：定义 `team-roster.md` 的最小字段

每位成员至少应记录：
- member id
- display name
- canonical profile path（可选）
- project folder path
- declared role
- expected contribution
- current status

固定建议：
- `project folder path` 默认就是 `members/<member-id>/`
- 如果已有长期画像，就把绝对路径写到 `canonical profile path`
- 如果没有长期画像，也不要失败；先通过第一轮问卷建立项目内画像

---

## 第 8 步：准备双层成员画像

### 跨项目成员画像
复制：
- `templates/member-capability-profile-template.md`

用来记录长期、稳定、可复用的内容，例如：
- strengths
- weaknesses / support needed
- preferred task granularity
- preferred output formats
- typical decision areas
- recurring constraints
- collaboration style
- reusable notes from past projects

### 项目内成员上下文
在 `members/<id>/member-context.md` 中记录本项目临时信息，例如：
- 本次负责模块
- 当前手头资料
- 本次可投入时间
- 对项目目标的理解
- 当前阻塞

---

## 第 9 步：接受固定状态机，不要退回一次性 prompt

多人协同默认不是“一次性生成一张问卷”，而是固定状态机：
1. Kickoff
2. Questionnaire
3. Alignment
4. Assignment
5. Follow-up
6. Distill / Closeout

并且这些文件必须支持 `status`：
- `questionnaire.md`
- `assignment.md`
- `coordination/alignment-summary.md`
- `coordination/task-board.md`
- `coordination/decision-register.md`

最少支持：
- `draft`
- `approved`
- `superseded`
- `blocked`

---

## 第 10 步：如果要同步回知识库，也不要新增第二套治理模型

多人协同的稳定结果可以同步回知识库，但要满足两个条件：
1. 有明确的 vault profile
2. 只有 `approved` 的稳定内容才允许同步

默认同步两类内容：
- 人物画像增量
- 稳定决策蒸馏

同步时仍沿用现有 page-role model：
- 不为 team coordination 新建第二套知识库治理模型
- 只把稳定内容写进 `project / knowledge / ops / task / overview` 中合适的位置

---

## 第 11 步：安装 skill 后怎么调用

### Maintenance
可以这样说：

```text
Use $knowledge-base-maintenance to integrate this task or chat into my markdown knowledge base.
Read the vault profile first, keep only durable conclusions or reusable troubleshooting knowledge, choose the right page role, and sync the target page, relevant root page, reader entry, and milestone log.
```

### Audit
可以这样说：

```text
Use $knowledge-base-audit to inspect my wiki vault.
Read the vault profile first, then check metadata completeness, dead links, orphan pages, root page coverage, page-boundary drift, noise regression, and stray markdown files at the vault root.
```

### Team Coordination
可以这样说：

```text
Use $knowledge-base-team-coordination to run this shared project workflow.
Read the project brief, team roster, shared materials, and member folders first.
If canonical member profiles exist, use them before drafting questionnaires.
If a vault profile is available, sync only approved, reusable decisions back into the knowledge base.
```

---

## 定制完成后的最小验收

你的配置完成后，至少应该能回答这些问题：
- root pages 是哪些？
- areas 是哪些？
- 哪些文件允许放在 vault 根目录？
- 哪些页面要进 `pages/`？
- `ops` 页是否默认采用“现象 / 根因 / 处理法 / 边界”？
- `log.md` 是否是 milestone-only？
- 多人协同项目目录是否完整？
- `team-roster.md` 是否能定位每个成员的目录和画像？
- 没有 canonical profile path 时，是否知道要先问卷建画像？
- 你是否明确只有 `approved` 的任务和决策可以作为后续事实源？
