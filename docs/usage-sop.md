# Usage SOP

## 8 个 skill 的职责分工

### `knowledge-base-kit-guide`
用于：
- 解释这套分享包怎么安装
- 解释 `vault profile` 应该填什么
- 判断当前更适合用哪个 specialist skill
- 把用户从“我不知道从哪里开始”引到清晰下一步

### `knowledge-base-orchestrator`
用于：
- 零门槛初始化入口
- 检测已有 Obsidian / vault / profile
- 在用户同意时执行可选的 Obsidian 安装
- 创建 vault 骨架、生成 profile，并给出下一步路由

> 它是 onboarding coordinator，不是万能自动代理。

### `knowledge-base-ingest`
用于：
- 导入长 markdown 文档、书稿、教程或大章节
- 先按章节/主题拆分，再建立 parent-child / prev-next / related links
- 把第一次导入当成可测试基线，并通过对比、回归、重构继续优化结构
- 对超大源材料切到 close-reading mode，按 batch 分块精读并保留 rolling state

### `knowledge-base-maintenance`
用于：
- 把任务结果沉淀进知识库
- 把聊天结论写进合适页面
- 收敛根页、知识页、运维页的写法边界
- 把噪音挡在知识库外面

### `knowledge-base-audit`
用于：
- 做结构健康检查
- 检查 dead links、orphan pages、frontmatter、导航覆盖
- 检查 page-boundary drift、noise regression、root-level stray markdown files

### `knowledge-base-working-profile`
用于：
- 从持续沟通中提炼稳定的协作画像
- 沉淀偏好、决策习惯、协作边界和反模式
- 区分 confirmed / repeated / inferred，并过滤敏感个人信息

### `knowledge-base-team-coordination`
用于：
- 协调 2 人及以上的共享项目目录
- 生成成员级问卷、汇总对齐、生成派单草案
- 输出决策蒸馏，并在需要时同步到知识库

### `work-journal`
用于：
- 记录每日工作、会议纪要、临时想法
- 管理项目关联、人名表、时间线
- 从 journal 中提取周报和可沉淀知识

---

## 标准工作流

### 场景 A：完全新手，从零开始
1. 先用 `knowledge-base-orchestrator` 检查现状
2. 如需安装 Obsidian，再明确征得同意
3. 创建骨架、生成 `vault profile`
4. 再根据目标进入 specialist skill

也就是：**先初始化，再分流**。

### 场景 B：我想先搞明白，不急着自动化
1. 先用 `knowledge-base-kit-guide`
2. 理解 profile、页面角色和 skill 分工
3. 再进入对应 specialist skill

也就是：**先理解，再执行**。

### 场景 C：导入长文档 / 书籍
1. 先用 `knowledge-base-ingest` 做第一版导入基线
2. 基于测试结果继续优化拆分粒度、页面角色和链接结构
3. 如果导入规模较大，再用 `knowledge-base-audit` 做复检

也就是：**先落基线，再迭代，再审**。

### 场景 C2：超大文本 / 整本书 / 需要分块精读
1. 先用 `knowledge-base-ingest` 进入 close-reading mode
2. 生成 chunk、batch packet 和 reading state
3. 逐 batch 精读并写入 `batch-notes/*.json`
4. source 变化后优先只重跑 changed batches
5. 重跑 close-reading harness 刷新 rolling state
6. 用 synthesis 汇总 chapter / topic / glossary 候选结果
7. 生成 candidate pages、candidate link map 和 draft frontmatter
8. 最后再把稳定结构写回知识库

也就是：**先切块，再精读，再汇总，再落页**。

### 场景 D：任务完成后沉淀知识
1. 先用 `knowledge-base-maintenance`
2. 如果改动较大，再用 `knowledge-base-audit` 做复检

也就是：**先写，再审**。

### 场景 E：持续协作时沉淀 working profile
1. 先用 `knowledge-base-working-profile` 提炼稳定信号
2. 把敏感细节、一次性情绪和弱推断挡在长期画像外
3. 按 visibility 决定是否同步 reader-facing 入口

也就是：**先提炼，再分级，再决定可见范围**。

### 场景 F：多人共享项目
1. 先用 `knowledge-base-team-coordination` 建立 kickoff / questionnaire / alignment / assignment 流程
2. 只把已确认内容升级为 approved
3. 如需沉淀稳定知识，再交给 maintenance / working-profile

也就是：**先对齐，再派单，再蒸馏**。

### 场景 G：每日记录与周期沉淀
1. 用 `work-journal` 记录工作、会议、临时想法
2. 周期性提取可沉淀条目
3. 需要长期进入知识库的部分，再交给 maintenance

也就是：**先记时间线，再做蒸馏**。

---

## Ingest 的默认回路

1. 先读 vault profile 和 source markdown
2. 定义 ingestion map 与第一版导入基线
3. 建立 overview / chapter / topic 结构
4. 生成 TOC / glossary candidates / related-link suggestions
5. 为每轮保留最小 harness 产物
6. 基于测试结果比较拆分方案、页面角色和维护成本
7. 对入口页、来源链和关键导航做回归检查
8. 汇报版本差异与最终稳定形态

### 超大文本的 close-reading 回路

1. 先运行 `scripts/close_read_markdown.py`
2. 生成 `chunks/`、`batch-plan.json`、`reading-state.json`
3. 逐 batch 精读 `batch-packets/*.md`
4. 每轮把抽取结果写入 `batch-notes/<batch-id>.json`
5. 只要 source 有局部变更，就优先只重跑 changed batches
6. 重跑 harness，让后续 packet 读取最新 rolling state
7. 运行 `scripts/synthesize_knowledge.py`
8. 查看 candidate pages / candidate link map / frontmatter 是否合理
9. 只把 overview / chapter / topic 的稳定候选结构写回知识库

---

## Maintenance 的默认回路

1. 先读 vault profile
2. 先做噪音过滤
3. 判页面角色和 area
4. 优先更新已有页
5. 同步根页 / 读者入口 / 里程碑日志
6. 汇报哪些内容被保留、哪些被压缩

---

## Audit 的默认回路

1. 先读 vault profile
2. 查 frontmatter 和 metadata
3. 查 dead links / orphan pages / missing entrypoints
4. 查 root page coverage
5. 查 page-boundary drift
6. 查 noise regression
7. 查 root-level stray markdown files
8. 按 P1 / P2 / P3 输出

---

## Working Profile 的默认回路

1. 先读 vault profile 和当前 working profile 页面
2. 收集本轮可作为证据的互动信号
3. 先跑敏感信息过滤
4. 抽取 stable facts / preferences / heuristics / boundaries / anti-patterns / provisional signals
5. 标注 confirmed / repeated / inferred
6. 更新 working profile 页面并补 change notes
7. 按 visibility 规则决定是否同步 maintainer / reader 入口

---

## Team Coordination 的默认回路

1. 读取共享项目目录与 roster
2. 输出问卷草案
3. 读取成员回答并生成 alignment summary
4. 生成 assignment draft 与 task board
5. 在 follow-up 中处理补问、风险和变更
6. 结项时输出 decision distill / decision register

---

## Work Journal 的默认回路

1. 按日期创建或追加 journal 页面
2. 记录时间戳、项目关联、人名与来源
3. 标出“可沉淀 / 待沉淀”条目
4. 生成周报或周期蒸馏时，回收稳定知识
5. 需要长期进入知识库的内容再同步给 maintenance

---

## 什么时候不该用这些 skill

### 不该直接用 `knowledge-base-maintenance`
如果内容只是：
- 临时聊天
- 单次运行日志
- 长过程记录
- 原始素材镜像
- 还没沉淀成结论的草稿

### 不该直接把 `knowledge-base-orchestrator` 当万能工具
如果你已经明确知道：
- vault 在哪里
- profile 已经怎么配
- 这次要导入还是维护还是审计

那就直接进入 specialist skill，不必再绕一层 orchestrator。

### 不该把以下内容写进 working profile
- 一次性情绪
- 高敏感个人信息
- 与未来协作无关的私人细节
- 对第三方的私人评价
- 未经确认的强推断
