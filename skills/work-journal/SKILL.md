---
name: work-journal
description: This skill should be used when the user asks to "record daily work", "write meeting notes", "save temporary ideas", "记录今天的工作", "写会议纪要", "保存临时想法", "整理工作记录", or "生成工作总结". It creates and maintains daily work journals with timestamps, project associations, meeting notes, and temporary ideas. It also manages a people table for name resolution and supports weekly knowledge distillation from journal entries.
---

# Work Journal

每日工作记录与总结的技能。用于记录会议纪要、临时想法、项目进展，并自动建立项目关联、人名链接和时间线索引。

## 核心功能

1. **每日记录**：按日期创建工作记录，支持时间戳格式
2. **会议录音处理**：支持语音转录，自动提取要点
3. **临时想法保存**：快速记录灵感，标记是否可沉淀
4. **项目关联**：自动建立项目软连接和知识页链接
5. **人名管理**：维护人名对照表，自动生成 Wiki 链接
6. **周期沉淀**：每周自动提取知识点到知识库

---

## Required input

执行前先读取：
- `references/journal-schema.md` — 记录格式规范
- `references/people-table-template.md` — 人名对照表模板
- `references/weekly-distill-checklist.md` — 周期沉淀检查清单
- `../../templates/journal-profile-template.md` — Journal 配置模板

需要用户提供：
- Vault root path
- Journal 目录位置（默认 `journals/`）
- 日期（默认当天）
- 项目名称（如有）
- 人名列表（如有会议）

---

## Core rules

### 1. 记录原则
- **时间戳必填**：每条记录必须有精确时间（格式：`HH:MM`）
- **项目标记**：涉及项目必须用 `[[项目名]]` 格式
- **人名标记**：参会人必须用 `[[人名]]` 格式
- **沉淀标记**：可沉淀知识用 `→ 沉淀: xxx → [[知识页]]` 标记

### 2. 语音转录处理
- 用户提供录音路径后，先询问是否需要转录
- 转转录后自动提取要点，不保留完整原文
- **必须询问确认**：人名、项目名是否正确（语音转录可能有误）

### 3. 人名处理
- 首次出现的人名，询问：姓名、职位/角色、常参与项目
- 自动更新 `people-table.md`
- 自动生成 `[[人名]]` Wiki 链接

### 4. 项目处理
- 首次出现的项目，询问：项目全称、项目类型、知识页是否已存在
- 自动创建/更新项目时间线页
- 自动建立项目与知识页的双向链接

### 5. 周期沉淀
- 每周一扫描上周 journal
- 识别 `→ 沉淀` 标记
- 提取稳定知识到对应知识页
- 更新 journal 页的沉淀链接

---

## Workflow

### 1. 用户请求处理

当用户请求记录工作时：
```
用户输入: "用 $work-journal 记录今天的会议"
    ↓
询问: 会议时间、参会人、项目名称
    ↓
询问: 是否有录音？路径？
    ↓
询问: 是否需要转录？
    ↓
（如有转录）询问: 人名/项目名是否正确？
    ↓
创建/更新当日 journal 页
```

### 2. 创建每日记录

执行步骤：
```
1. 确定日期（默认当天）
2. 检查 journal 目录是否存在，不存在则创建
3. 检查当月目录是否存在（journals/YYYY-MM/）
4. 创建或追加当日记录文件（YYYY-MM-DD.md）
5. 添加时间戳和内容
6. 更新项目索引
7. 更新人名对照表（如有新人物）
8. 更新 frontmatter（projects, people, tags）
```

### 3. 处理会议录音

```
1. 用户提供录音路径
2. 询问是否需要语音转录
3. 执行转录（使用外部工具）
4. 提取要点：
   - 关键决议
   - 参会人
   - 项目进展
   - 可沉淀知识点
5. 询问确认：人名是否正确？项目名是否正确？
6. 写入 journal 页
7. 录音文件路径记录在记录中
```

### 4. 临时想法处理

```
1. 用户输入想法内容
2. 询问：是否可沉淀到知识库？
3. 标记：
   - 可沉淀 → "→ 可沉淀: [知识点描述] → [[待创建知识页]]"
   - 不可沉淀 → 仅记录在时间线
4. 写入当日 journal
```

### 5. 项目关联

```
1. 提取记录中的项目名
2. 检查项目是否已存在：
   - 已存在 → 更新项目时间线页
   - 不存在 → 询问创建新项目
3. 创建/更新：
   - journals/project-[项目名]-timeline.md（时间线页）
   - pages/project-[项目名].md（知识页，如不存在）
4. 建立双向链接：
   - journal → [[项目名]]
   - 项目时间线 → 当日记录链接
```

### 6. 人名更新

```
1. 提取记录中人名
2. 检查人名对照表：
   - 已存在 → 直接使用 [[人名]] 链接
   - 不存在 → 询问详细信息（职位、常参与项目）
3. 更新 people-table.md
4. 在 journal 中使用 [[人名]] 链接
```

---

## Journal 页面格式

### Frontmatter 标准

```yaml
---
title: "YYYY-MM-DD 工作记录"
type: "journal"
date: "YYYY-MM-DD"
projects: ["项目A", "项目B"]
people: ["张三", "李四"]
tags: ["会议", "想法", "进展"]
sources: ["录音路径"]  # 可选
---
```

### 正文格式

```markdown
# YYYY-MM-DD 工作记录

## 时间线

### HH:MM - HH:MM [事件类型] [项目名]
**类型**: 会议/想法/进展/其他
**参会人**: [[张三]], [[李四]]
**会议录音**: `sources/meetings/YYYY-MM-DD-xxx.mp3`

**内容要点**:
1. 第一个要点
2. 第二个要点

**关键决议**:
- 决议1
- 决议2

**→ 沉淀**: [知识点描述] → [[知识页名]]

---

## 今日项目关联

| 项目 | 今日进展 | 相关知识页 |
|------|---------|-----------|
| [[项目A]] | 启动会完成 | [[项目管理方法]] |
```

---

## 周期沉淀机制

### 触发条件
- 每周一 09:00（可配置）
- 或用户手动触发："用 $work-journal 执行周期沉淀"

### 执行流程
```
1. 扫描 journals/YYYY-MM/ 上周所有记录
2. 识别标记：
   - "→ 沉淀" → 立即沉淀
   - "→ 可沉淀" → 评估后沉淀
3. 提取知识点：
   - 方法论 → knowledge 页
   - 操作流程 → ops 页
   - 项目结论 → project 页
4. 创建/更新知识页
5. 在 journal 页添加沉淀完成标记
6. 更新 WIKI-INDEX.md
7. 更新里程碑日志
```

---

## 询问清单

每次执行时，必须询问以下内容：

### 必问项
1. **日期**：今天是几号？记录哪一天的工作？
2. **内容类型**：会议纪要 / 临时想法 / 项目进展 / 其他？

### 会议相关
3. **会议时间**：几点到几点？
4. **参会人**：参会人姓名？（语音转录后需确认是否正确）
5. **项目名称**：涉及哪个项目？（需确认是否正确）
6. **是否有录音**：录音文件路径？
7. **是否需要转录**：是否需要语音转文字？

### 新人名出现时
8. **姓名确认**：人名是否正确？（语音转录可能有误）
9. **职位/角色**：此人职位或角色是什么？
10. **常参与项目**：此人常参与哪些项目？

### 新项目出现时
11. **项目全称**：项目全称是什么？
12. **项目类型**：是什么类型的项目？
13. **知识页**：是否已有对应知识页？没有是否需要创建？

### 临时想法
14. **是否可沉淀**：这个想法是否值得沉淀到知识库？

---

## Output expectations

每次记录完成后汇报：
- 创建/更新的 journal 页路径
- 添加的时间戳条目数
- 涉及的项目列表
- 涉及的人名列表
- 是否有可沉淀知识
- 是否更新了人名对照表
- 是否更新了项目索引

---

## Additional resources

- `references/journal-schema.md` — 记录格式详细规范
- `references/people-table-template.md` — 人名对照表模板
- `references/weekly-distill-checklist.md` — 周期沉淀检查清单
- `scripts/create_daily_journal.py` — 创建每日记录的辅助脚本
- `../../templates/journal-profile-template.md` — Journal 配置模板