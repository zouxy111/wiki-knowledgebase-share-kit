---
name: knowledge-base-working-profile
description: This skill should be used when the user asks to remember or update how they work, distill collaboration preferences from ongoing conversations, maintain a working profile in a markdown/wiki knowledge base, 沉淀协作画像, 更新我的工作偏好, 记录我的决策习惯, or 从沟通过程中整理长期画像. It extracts stable collaboration-relevant signals such as preferences, decision heuristics, boundaries, and anti-patterns, keeps confirmed and inferred items separate, and refuses to store secrets or overly sensitive personal data.
---

# Knowledge Base Working Profile

把持续沟通中出现的**稳定协作信息**沉淀进 markdown/wiki 知识库。

它处理的不是“原始个人资料”，而是未来协作真正会反复用到的东西，例如：
- 稳定事实（仅限工作相关）
- 偏好
- 决策习惯
- 协作边界
- 反模式
- 仍待确认的画像信号

它和 `knowledge-base-maintenance` 的区别是：
- `knowledge-base-maintenance`：沉淀某次任务/聊天/排障的结果
- `knowledge-base-working-profile`：沉淀**这个人长期怎么合作、怎么判断、偏好什么、不喜欢什么**

默认目标不是“做人格克隆”，也不是“存个人隐私档案”，而是形成一个**可持续更新的 working profile**，减少反复解释与协作摩擦。

## Required input

执行前先读取：
- `references/working-profile-schema.md`
- `references/evidence-thresholds.md`
- `references/sensitivity-boundaries.md`
- `../../templates/vault-profile-template.md`
- `../../templates/working-profile-page-template.md`

默认需要这些输入：
- vault profile
- 当前 working profile page（如果已有）
- 本轮证据来源：当前对话、用户纠正、长期反馈、会议纪要、任务回顾等
- 如果 profile 里没有 working profile page：用户指定目标页

如果没有明确 working profile page，不要猜测文件路径。

## Core rules

- **只沉淀对未来协作有用的信息。**
- **先过敏感信息过滤，再判断是否入库。**
- **明确区分 confirmed / repeated / inferred。**
- **单次随口表达不等于稳定画像。**
- **允许时间变化和场景差异，不强行写成绝对人格标签。**
- **优先更新已有 profile，不频繁新建画像页。**
- **不写 secrets，不写高敏感个人信息，不写第三方隐私。**
- **重大画像变化应显式写入 change note，而不是悄悄覆盖。**

## What belongs in a working profile

### Good candidates
- 经多次重复出现的工作偏好
- 用户明确表达过的协作方式偏好
- 决策习惯与推进节奏
- 对输出风格、结构、颗粒度的稳定要求
- 明确的边界和禁区
- 常见不满意点或反模式

### Bad candidates
- 一次性情绪
- 临时状态
- 无法验证的私人推测
- 无助于未来合作的个人细节
- 账号、密码、证件、地址、财务账户、医疗隐私等高敏感信息

## Recommended workflow

### 1. Gather evidence first
先收集本轮真正可作为证据的材料：
- 当前对话中的明确表达
- 用户对你方案的修正
- 用户多次重复过的偏好
- 过往 working profile 中已有条目
- 近期任务里出现的新信号

### 2. Run the sensitivity gate
先按 `references/sensitivity-boundaries.md` 过滤：
- 哪些内容绝不应入库
- 哪些内容需要降级成模糊描述
- 哪些内容只适合短期上下文，不适合长期页面

### 3. Extract candidate signals
把证据转成候选画像信号，而不是直接照抄原话。

优先抽这些类型：
- Stable facts
- Preferences
- Decision heuristics
- Collaboration boundaries
- Anti-patterns
- Open questions / provisional signals

### 4. Assign evidence strength
使用 `references/evidence-thresholds.md` 的口径：
- `confirmed`：用户明确确认
- `repeated`：多次稳定出现
- `inferred`：当前可推断，但还不够稳

`inferred` 项默认应更克制，必要时放到 provisional 区域，而不是写死。

### 5. Update the working profile page
默认按 `../../templates/working-profile-page-template.md` 的结构更新。

写入时：
- 保留对未来协作真正有用的表述
- 压缩原始上下文
- 避免人格化夸张描述
- 保留必要 change notes
- 避免同义重复

### 6. Sync visibility surfaces carefully
根据 profile 中的 working profile visibility 决定同步范围：
- `maintainer-only`：只更新 profile 页面和维护入口
- `reader-visible`：可同步 reader entrypoint 或治理入口
- 如果未定义 visibility，默认按 `maintainer-only` 处理

### 7. Validate before finishing
检查：
- 有没有误写高敏感信息
- 有没有把一次性情绪写成长期标签
- 有没有把 inferred 写成 confirmed
- 是否保留了变化轨迹
- 页面是否仍然可维护、可扩展、可更新

## Output expectations

汇报时至少说明：
- 新增或更新了哪些 working profile 条目
- 哪些属于 confirmed / repeated / inferred
- 哪些候选信息被过滤掉，为什么
- 是否记录了 change note
- 是否同步了对应入口页

## Resources

### references/
- `references/working-profile-schema.md`：working profile 推荐结构与字段边界
- `references/evidence-thresholds.md`：如何判断 confirmed / repeated / inferred
- `references/sensitivity-boundaries.md`：哪些个人信息绝不应入库，哪些应降级处理

### templates/
- `../../templates/vault-profile-template.md`：working profile page 与 visibility 等配置入口
- `../../templates/working-profile-page-template.md`：推荐的 working profile 页面结构
