# Journal Profile Template

> **用途**：配置工作记录功能的目录和规则
> **用法**：复制本模板，填写后保存到 vault 根目录或合并到 `vault-profile-template.md`

---

## 13. Journal 配置

### 13.1 目录结构

- **Journal 根目录**: `journals/`
  - 💡 存放每日工作记录，按月归档

- **Journal 月度目录**: `journals/YYYY-MM/`
  - 💡 自动创建，如 `journals/2026-04/`

- **每日记录文件**: `journals/YYYY-MM/YYYY-MM-DD.md`
  - 💡 格式示例：`journals/2026-04/2026-04-17.md`

### 13.2 索引文件

- **项目索引**: `journals/project-索引.md`
  - 💡 所有项目的软连接中心

- **项目时间线**: `journals/project-{项目名}-timeline.md`
  - 💡 每个项目的记录时间线

- **人名对照表**: `journals/people-table.md`
  - 💡 统一管理所有人名链接

### 13.3 源文件目录

- **会议录音**: `sources/meetings/`
  - 💡 存放会议录音文件（MP3/WAV/M4A）

- **会议记录**: `sources/meeting-notes/`
  - 💡 存放会议文字记录

- **临时想法**: `sources/ideas/`
  - 💡 存放临时想法草稿

### 13.4 Page Role 扩展

新增 **`journal`** 角色（仅用于 journals/ 目录）：

| Role | 定义 | 写什么 | 不写什么 |
|------|------|--------|---------|
| `journal` | 工作记录页 | 会议纪要/临时想法/时间戳/项目进展 | 知识方法（应沉淀到 knowledge） |

### 13.5 周期沉淀配置

- **沉淀触发时间**: 每周一 09:00
- **沉淀范围**: 上周一 至 上周日
- **沉淀标记**: `→ 可沉淀` 和 `→ 沉淀`

### 13.6 人名链接规则

- **格式**: `[[人名]]`
- **新人名处理**: 首次出现时询问用户确认
  - 姓名是否正确？（语音转录可能出错）
  - 职位/角色？
  - 常参与项目？

### 13.7 项目链接规则

- **格式**: `[[项目名]]`
- **双向链接**:
  - journal → 项目时间线页
  - journal → 知识页（如已存在）

---

## ✅ 配置检查清单

- [ ] `journals/` 目录已创建
- [ ] `sources/meetings/` 目录已创建
- [ ] `people-table.md` 已创建（可空）
- [ ] `project-索引.md` 已创建（可空）
- [ ] 周期沉淀 cron 已配置（如使用自动化）

---

## 🆘 需要帮助？

- 查看 `skills/work-journal/references/journal-schema.md` 了解详细格式
- 查看 `skills/work-journal/references/weekly-distill-checklist.md` 了解沉淀规则