# Usage SOP

## 五个 skill 的职责分工

### `knowledge-base-kit-guide`
用于：
- 教用户怎么安装这套分享包
- 教用户怎么填写 `vault profile`
- 判断当前该先用 ingest / maintenance / working-profile / audit 中的哪一个
- 给第一次接触这套 kit 的人做分流说明

### `knowledge-base-ingest`
用于：
- 把长 markdown 文档、书稿、教程或大章节导入知识库
- 先按章节/主题拆分，再建立 parent-child / prev-next / related links，并生成 TOC / glossary candidates / related-link suggestions
- 把长文档重组为 overview + chapter + topic 页面群
- 避免把整本书直接作为一个超长页面写回 wiki
- 把第一次导入视为可测试基线，再根据测试、回归和版本对比持续优化结构
- 作为轻量 harness / 回归底座，持续沉淀结构版本差异与回归结果

### `knowledge-base-maintenance`
用于：
- 把任务结果沉淀进知识库
- 把聊天结论写进合适页面
- 收敛根页、知识页、运维页的写法边界
- 把噪音挡在知识库外面

### `knowledge-base-working-profile`
用于：
- 从持续沟通中提炼稳定的协作画像
- 沉淀偏好、决策习惯、协作边界和反模式
- 区分 confirmed / repeated / inferred，而不是把一次表达写死
- 过滤敏感个人信息，避免把 working profile 做成隐私档案

### `knowledge-base-audit`
用于：
- 做结构健康检查
- 检查 dead links、orphan pages、frontmatter、导航覆盖
- 检查 page-boundary drift
- 检查 noise regression
- 检查 vault 根目录 stray markdown files

---

## 标准工作流

### 场景 A：导入长文档 / 书籍
1. 先用 `knowledge-base-ingest` 做第一版导入基线
2. 根据测试结果继续优化拆分粒度、页面角色和链接结构
3. 如果导入规模较大，再用 `knowledge-base-audit` 做复检

也就是：**先落基线，再迭代，再审**。

### 场景 B：任务完成后沉淀知识
1. 先用 `knowledge-base-maintenance`
2. 如果改动较大，再用 `knowledge-base-audit` 做复检

也就是：**先写，再审**。

### 场景 C：怀疑知识库已经乱了
1. 先用 `knowledge-base-audit`
2. 根据问题清单，再用 `knowledge-base-maintenance` 去修

也就是：**先查，再写**。

### 场景 D：周期巡检
定期只跑 `knowledge-base-audit`，看有没有：
- 入口丢失
- 页面边界漂移
- 根页堆流水
- `ops` 页退化成日志
- `log.md` 变任务回放

### 场景 E：持续协作时沉淀 working profile
1. 先用 `knowledge-base-working-profile` 提炼本轮稳定信号
2. 把一次性情绪、敏感细节和弱推断挡在长期画像外
3. 只在需要公开可见时再同步 reader-facing 入口

也就是：**先提炼，再分级，再决定可见范围**。

---

## Ingest 的默认回路

1. 先读 vault profile 和 source markdown
2. 先做 ingestion map，并定义第一版导入基线
3. 先拆分，再决定落页
4. 建立 parent-child / prev-next / related links
5. 同步 overview / root page / reader entry / milestone log
6. 产出 TOC / glossary candidates / related-link suggestions
7. 为这一轮保留最小 harness 产物：ingestion map / manifest / toc / 候选术语 / related suggestions / regression checklist
8. 基于测试结果比较不同拆分方案的可用性与维护成本
9. 调整页面角色、链接架构和章节粒度
10. 对入口页、来源链和关键导航做回归检查
11. 汇报版本差异、结构决策和最终稳定形态

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

## 什么时候不该用 maintenance

如果内容只是：
- 临时聊天
- 单次运行日志
- 长过程记录
- 原始素材镜像
- 还没沉淀成结论的草稿

默认不该直接进知识库。

---

## 什么时候不该用 audit

如果你已经明确知道：
- 这次要改哪一页
- 这次要把什么结论写进去

那就直接用 maintenance，不必先做审计。

---

## 输出要求

### maintenance
至少说明：
- 改了哪些页
- 为什么归到该页面角色
- 是否同步了入口和日志
- 哪些内容被判为噪音

### working-profile
至少说明：
- 更新了哪些画像条目
- 哪些属于 confirmed / repeated / inferred
- 哪些内容因敏感或证据不足被过滤
- 是否记录了 change note
- 是否同步了对应入口页

### audit
至少说明：
- audit summary
- P1 / P2 / P3 findings
- 影响页面
- 建议修复顺序
- 是否存在 root-level stray files

---

## 为什么 ingest 不是一次性动作

长篇知识源的第一次导入，通常只能得到一个**可测试版本**，而不是最终版本。

真正稳定的知识库结构，往往要经过：
- 拆分粒度调整
- 页面角色重构
- 链接架构优化
- 入口页与来源链的回归检查

因此 `knowledge-base-ingest` 更像一个“测试驱动的结构整理回路”或“轻量 harness / 回归底座”，而不是一次性导入脚本。

---

## Working Profile 的默认回路

1. 先读 vault profile 和当前 working profile 页面
2. 收集本轮可作为证据的互动信号
3. 先跑敏感信息过滤
4. 抽取 stable facts / preferences / heuristics / boundaries / anti-patterns / provisional signals
5. 标注 confirmed / repeated / inferred
6. 更新 working profile 页面并补 change notes
7. 按 visibility 规则决定是否同步 maintainer / reader 入口
8. 检查是否误把一次性表达写成长期标签

---

## 什么时候不该用 working profile

如果内容只是：
- 一次性情绪
- 与未来协作无关的私人细节
- 高敏感个人信息
- 未经确认的强推断
- 对第三方的私人评价

默认不应写进 working profile。
