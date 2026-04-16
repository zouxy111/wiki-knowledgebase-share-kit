# Usage SOP

> 建议默认把填写后的 profile 保存成一个稳定文件，例如 `<vault-root>/vault-profile.md`，并在每次调用时显式给出这个**绝对路径**。  
> 多人协同场景下，也建议把共享项目目录保存成一个稳定路径，并在每次调用时显式给出该目录的**绝对路径**。

## 五个 skill 的职责分工

### `knowledge-base-kit-guide`
用于：
- 教用户怎么安装这套分享包
- 教用户怎么填写 `vault profile`
- 教用户怎么准备共享项目目录与成员画像
- 判断当前该先用 ingest / maintenance / audit / team coordination 中的哪一个
- 给第一次接触这套 kit 的人做分流说明

### `knowledge-base-ingest`
用于：
- 把长 markdown 文档、书稿、教程或大章节导入知识库
- 先按章节/主题拆分，再建立 parent-child / prev-next / related links，并生成 TOC / glossary candidates / related-link suggestions
- 把长文档重组为 overview + chapter + topic 页面群
- 把第一次导入视为**stable baseline**
- 用统一 rubric 比较 **baseline / candidate**，并在回归检查后再决定是否晋升

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
- 检查 page-boundary drift
- 检查 noise regression
- 检查 vault 根目录 stray markdown files

### `knowledge-base-team-coordination`
用于：
- 读取共享项目目录并理解 project brief / roster / shared materials
- 基于成员画像生成**角色化问卷草案**
- 汇总回答并输出 alignment summary
- 生成成员级 assignment 与共享 task-board 草案
- 跟进执行、必要时补问或重分配
- 在关键节点与结项时输出 decision distill / decision register
- 如提供 vault profile，则把稳定决策和成员画像增量同步回知识库

---

## 标准工作流

### 场景 A：导入长文档 / 书籍
1. 先用 `knowledge-base-ingest` 做第一版导入基线
2. 根据本轮目标只改一类主要结构问题，产出 candidate
3. 用 `docs/ingest-evaluation-rubric.md` 比较 baseline 与 candidate
4. 跑最小回归检查
5. 只有在 candidate 更优且无关键回归时，才 promote 为新基线
6. 如导入规模较大，再用 `knowledge-base-audit` 做复检

也就是：**先落基线，再迭代，再审**。

### 场景 B：任务完成后沉淀知识
1. 先用 `knowledge-base-maintenance`
2. 如果改动较大，再用 `knowledge-base-audit` 做复检

也就是：**先写，再审**。

### 场景 C：怀疑知识库已经乱了
1. 先用 `knowledge-base-audit`
2. 根据问题清单，再用 `knowledge-base-maintenance` 去修

也就是：**先查，再写**。

### 场景 D：多人协同项目刚启动
1. 用 `knowledge-base-team-coordination` 读取共享项目目录
2. 输出 Kickoff 摘要与成员级问卷草案
3. 待成员回答后进入 Alignment 与 Assignment

也就是：**先 intake，再问卷，再对齐，再派单**。

### 场景 E：多人协同项目执行中
1. 更新 `progress-update.md`
2. 再用 `knowledge-base-team-coordination` 做 follow-up
3. 必要时发起补问、任务重排、风险升级

### 场景 F：多人协同项目结项
1. 用 `knowledge-base-team-coordination` 生成成员级 `decision-distill.md`
2. 汇总到 `coordination/decision-register.md`
3. 如提供 vault profile，则同步稳定知识回知识库

---

## Ingest 的默认回路

1. 先读 vault profile 和 source markdown
2. 先做 ingestion map，并定义当前 stable baseline
3. 先拆分，再决定落页
4. 建立 parent-child / prev-next / related links
5. 同步 overview / root page / reader entry / milestone log
6. 产出 TOC / glossary candidates / related-link suggestions
7. 为这一轮保留最小 harness 产物：ingestion map / manifest / toc / 候选术语 / related suggestions / regression checklist
8. 用 ingest rubric 比较 baseline 与 candidate 的结构质量
9. 对入口页、来源链和关键导航做回归检查
10. 记录本轮 decision：`promote / rework / drop`

推荐配套：
- `docs/ingest-evaluation-rubric.md`
- `templates/ingest-iteration-log-template.md`

---

## 推荐协作接入模式

### 主推平台
- **OpenClaw**
- **Hermes**

### 推荐工作方式
- coordinator AI 负责读取 shared project directory，并驱动 Kickoff → Questionnaire → Alignment → Assignment → Follow-up → Distill
- 每位成员可以在自己的 wiki / 私有资料区里整理资料和草稿
- 每位成员可以用自己的 OpenClaw / Hermes / 其他 agent 协助回答问卷、整理回应、更新进展
- 但 coordinator 默认只把**已同步回 shared project directory 的 markdown 文件**视为正式输入

### 推荐同步拓扑
1. 把 `team-project/` 独立放在 NAS / 网盘同步目录里
2. 把 `team-project/` 直接嵌入共享 wiki / 共享知识库子目录中

无论使用哪种拓扑：
- shared project directory 都是唯一事实源
- 个人 wiki / 私有资料区不是 coordinator 的默认事实源

详见：`docs/collaboration-integration-patterns.md`

---

## Team Coordination 的固定状态机

### 1. Kickoff
读取：
- `project-brief.md`
- `team-roster.md`
- `shared-materials/`
- `members/<id>/member-context.md`
- 可选：canonical member profiles

输出：
- 项目理解摘要
- 成员级 `questionnaire.md` 草案

### 2. Questionnaire
要求：
- 问题必须是“角色模板 + 项目定制”生成
- 必须覆盖：目标理解、证据掌握、输出颗粒度、依赖关系、约束、待确认决策

### 3. Alignment
读取：
- `members/<id>/response.md`

输出：
- `coordination/alignment-summary.md`
- 明确：共识、冲突点、缺口、待确认项、颗粒度不一致

### 4. Assignment
输出：
- `members/<id>/assignment.md`
- `coordination/task-board.md`

默认先是 `draft`，确认后再 `approved`。

### 5. Follow-up
读取：
- `members/<id>/progress-update.md`

输出：
- 补问
- 任务重排
- 风险升级
- 依赖提醒

### 6. Distill / Closeout
输出：
- `members/<id>/decision-distill.md`
- `coordination/decision-register.md`
- 如提供 vault profile，再把稳定内容同步回知识库

---

## 什么情况下不要混用 skill

- 用户要跑长文档导入结构迭代：用 `knowledge-base-ingest`，不要让 maintenance 假装 ingest
- 用户要写 durable knowledge：用 `knowledge-base-maintenance`
- 用户要查结构健康：用 `knowledge-base-audit`
- 用户要做多人项目问卷 / 对齐 / 派单 / 跟进 / 决策蒸馏：用 `knowledge-base-team-coordination`

---

## 最小验收清单

### 知识库侧
- [ ] root pages 有覆盖主要内容
- [ ] `index.md` / reader entrypoint 已同步
- [ ] `log.md` 没退化成任务回放
- [ ] `ops` 页没有退化成流水日志
- [ ] 没有明显 dead links / orphan pages / stray markdown

### ingest 侧
- [ ] 有 stable baseline
- [ ] candidate 改动目标明确
- [ ] rubric 已打分
- [ ] regression 已检查
- [ ] decision 已记录为 promote / rework / drop

### 多人协同侧
- [ ] `team-project/` 结构完整
- [ ] `team-roster.md` 能定位成员目录和 canonical profile 路径
- [ ] 问卷 / alignment / assignment / decision 都带有 `status`
- [ ] 只有 `approved` 的任务和决策被后续流程或知识库同步当作事实源
