# 场景示例：产品经理文档库

> 这是一个完整的真实场景示例，展示一个产品经理如何用这套工具整理产品文档。

---

## 场景背景

**用户**：王五，某 SaaS 公司产品经理

**痛点**：
- 需求文档、竞品分析、用户反馈、会议记录全混在一起
- 想找某个功能的需求文档，翻半天找不到
- 不知道哪些需求已经实现、哪些还在排期
- 用户反馈散落在各处，没有系统整理
- 产品迭代历史没有记录

**目标**：
- 需求文档、竞品分析、用户研究分开管理
- 每个功能都有清晰的需求文档和实现状态
- 用户反馈能快速检索
- 产品迭代有完整记录

---

## 第一步：设计知识库结构

### Areas（分类）
```yaml
- product       # 产品需求
- research      # 用户研究
- competitive   # 竞品分析
- design        # 设计规范
- roadmap       # 产品路线图
- feedback      # 用户反馈
```

### Root Pages（导航页）
```yaml
- product       → pages/project-product-overview.md
- research      → pages/project-research-overview.md
- competitive   → pages/project-competitive-overview.md
- design        → pages/project-design-overview.md
- roadmap       → pages/project-roadmap-overview.md
- feedback      → pages/project-feedback-overview.md
```

---

## 第二步：填写 Vault Profile

```yaml
---
## 1. Vault identity

- Vault name: 产品文档库
- Vault root path: /Users/wangwu/Documents/product-docs
- Primary markdown page directory: /Users/wangwu/Documents/product-docs/pages
- Reader entrypoint file: /Users/wangwu/Documents/product-docs/index.md
- Milestone log file: /Users/wangwu/Documents/product-docs/log.md
- Maintainer entrypoint file: /Users/wangwu/Documents/product-docs/pages/governance.md

## 3. Area list

| area | 用途说明 |
|---|---|
| product | 产品需求文档 |
| research | 用户研究报告 |
| competitive | 竞品分析 |
| design | 设计规范 |
| roadmap | 产品路线图 |
| feedback | 用户反馈整理 |

## 4. Root page map

| area | root page file | 作用 |
|---|---|---|
| product | pages/project-product-overview.md | 产品需求导航 |
| research | pages/project-research-overview.md | 用户研究导航 |
| competitive | pages/project-competitive-overview.md | 竞品分析导航 |
| design | pages/project-design-overview.md | 设计规范导航 |
| roadmap | pages/project-roadmap-overview.md | 产品路线图导航 |
| feedback | pages/project-feedback-overview.md | 用户反馈导航 |

## 5. Canonical root-level markdown files

- README.md
- index.md
- log.md

## 6. Frontmatter contract

最少字段：
- title
- type
- area
- tags
- updated
- status  # 产品文档需要状态（草稿/评审中/已发布）

## 7. Naming conventions

- Root pages 以 `project-` 开头
- 需求文档用 `prd-` 开头
- 竞品分析用 `competitive-` 开头
- 用户研究用 `research-` 开头

## 8. Writing rules switches

- Knowledge-base-first mode: yes
- Milestone-only log: yes
- ops page four-part pattern: yes
- Root pages should avoid long process narration: yes
---
```

---

## 第三步：创建文件结构

```bash
product-docs/
├── index.md                    # 产品文档首页
├── log.md                      # 产品迭代日志
├── README.md                   # 说明文档
└── pages/
    ├── project-product-overview.md         # 产品需求导航
    ├── project-research-overview.md        # 用户研究导航
    ├── project-competitive-overview.md     # 竞品分析导航
    ├── project-design-overview.md          # 设计规范导航
    ├── project-roadmap-overview.md         # 产品路线图导航
    ├── project-feedback-overview.md        # 用户反馈导航
    │
    ├── prd-user-login.md                   # 用户登录需求
    ├── prd-payment-flow.md                 # 支付流程需求
    ├── prd-notification-system.md          # 通知系统需求
    ├── prd-dashboard.md                    # 数据看板需求
    │
    ├── research-user-interview-2026q1.md   # 用户访谈报告
    ├── research-survey-2026q1.md           # 用户调研报告
    ├── research-user-persona.md            # 用户画像
    │
    ├── competitive-slack.md                # Slack 竞品分析
    ├── competitive-notion.md               # Notion 竞品分析
    ├── competitive-feature-matrix.md       # 功能对比矩阵
    │
    ├── design-ui-guidelines.md             # UI 设计规范
    ├── design-interaction-patterns.md      # 交互设计模式
    ├── design-color-system.md              # 色彩系统
    │
    ├── roadmap-2026-q2.md                  # Q2 路线图
    ├── roadmap-2026-q3.md                  # Q3 路线图
    │
    ├── feedback-feature-requests.md        # 功能需求反馈
    ├── feedback-bug-reports.md             # Bug 反馈
    └── feedback-user-complaints.md         # 用户投诉
```

---

## 第四步：真实页面示例

### 示例 1：导航页（project）

**文件**：`pages/project-product-overview.md`

```markdown
---
title: "产品需求总览"
type: "project"
area: "product"
tags: ["导航", "产品"]
updated: "2026-04-17"
---

# 产品需求总览

## 🚀 当前版本（v2.3）

**发布日期**：2026-04-15

**核心功能**：
- [用户登录系统](./prd-user-login.md) ✅ 已上线
- [支付流程优化](./prd-payment-flow.md) ✅ 已上线
- [通知系统](./prd-notification-system.md) ✅ 已上线

## 📋 开发中（v2.4 预计 2026-05-01）

- [数据看板](./prd-dashboard.md) 🔨 开发中
- [团队协作功能](./prd-team-collaboration.md) 🔨 开发中
- [移动端适配](./prd-mobile-responsive.md) 📝 设计中

## 🔮 规划中（v2.5+）

- [AI 智能推荐](./prd-ai-recommendation.md) 💡 调研中
- [多语言支持](./prd-i18n.md) 💡 调研中
- [API 开放平台](./prd-open-api.md) 💡 调研中

## 📊 需求优先级

### P0（必须做）
- [支付安全加固](./prd-payment-security.md)
- [性能优化](./prd-performance.md)

### P1（重要）
- [用户体验优化](./prd-ux-improvement.md)
- [数据分析增强](./prd-analytics.md)

### P2（可选）
- [主题定制](./prd-theme-customization.md)
- [快捷键支持](./prd-keyboard-shortcuts.md)

## 🔗 相关链接

- [产品路线图](./project-roadmap-overview.md)
- [用户反馈](./project-feedback-overview.md)
- [竞品分析](./project-competitive-overview.md)
- [设计规范](./project-design-overview.md)
```

---

### 示例 2：需求文档（knowledge）

**文件**：`pages/prd-user-login.md`

```markdown
---
title: "用户登录系统 PRD"
type: "knowledge"
area: "product"
tags: ["prd", "登录", "认证"]
updated: "2026-04-17"
status: "已发布"
version: "v2.0"
---

# 用户登录系统 PRD

## 文档信息

- **版本**：v2.0
- **状态**：已发布
- **负责人**：王五（产品）、张三（开发）
- **上线时间**：2026-04-15

## 一、需求背景

### 1.1 业务目标
- 提升用户注册转化率（目标：从 30% 提升到 50%）
- 降低登录失败率（目标：从 15% 降低到 5%）
- 支持多种登录方式，提升用户体验

### 1.2 用户痛点
- 当前只支持邮箱+密码登录，流程繁琐
- 忘记密码后找回流程复杂
- 移动端输入密码体验差

### 1.3 竞品分析
参考：[Slack 登录流程分析](./competitive-slack.md)

---

## 二、功能需求

### 2.1 登录方式

#### 2.1.1 邮箱+密码登录（已有）
- 输入邮箱和密码
- 支持"记住我"功能（7 天免登录）
- 支持"忘记密码"

#### 2.1.2 手机号+验证码登录（新增）
- 输入手机号
- 发送 6 位数字验证码
- 验证码有效期 5 分钟
- 同一手机号 1 分钟内只能发送 1 次

#### 2.1.3 第三方登录（新增）
- 支持微信登录
- 支持 Google 登录
- 支持 GitHub 登录（面向开发者）

### 2.2 注册流程

#### 2.2.1 快速注册
- 只需手机号+验证码即可注册
- 自动生成用户名（可后续修改）
- 跳过邮箱验证（降低门槛）

#### 2.2.2 完整注册
- 手机号+验证码
- 设置密码
- 填写用户名
- 邮箱验证（可选）

### 2.3 密码找回

#### 2.3.1 通过手机号找回
1. 输入手机号
2. 发送验证码
3. 验证通过后设置新密码

#### 2.3.2 通过邮箱找回
1. 输入邮箱
2. 发送重置链接
3. 点击链接设置新密码

---

## 三、交互设计

### 3.1 登录页面布局

```
+----------------------------------+
|          Logo                    |
|                                  |
|  [邮箱/手机号输入框]              |
|  [密码/验证码输入框]              |
|                                  |
|  [ ] 记住我    忘记密码？         |
|                                  |
|  [      登录按钮      ]          |
|                                  |
|  -------- 或 --------            |
|                                  |
|  [微信] [Google] [GitHub]        |
|                                  |
|  还没有账号？立即注册             |
+----------------------------------+
```

### 3.2 交互流程图

参考：[登录流程图](./design-login-flow.png)

---

## 四、技术方案

### 4.1 安全要求
- 密码必须加密存储（bcrypt）
- 支持 2FA（两步验证）
- 登录失败 5 次后锁定账号 30 分钟
- 异地登录发送通知

### 4.2 性能要求
- 登录接口响应时间 < 500ms
- 验证码发送时间 < 3s
- 支持 10000 QPS

### 4.3 兼容性
- 支持 iOS 14+
- 支持 Android 8.0+
- 支持主流浏览器（Chrome、Safari、Firefox）

---

## 五、数据埋点

### 5.1 关键指标
- 注册转化率
- 登录成功率
- 各登录方式占比
- 密码找回成功率

### 5.2 埋点事件
```javascript
// 点击登录按钮
track('login_click', {
  method: 'email' | 'phone' | 'wechat' | 'google' | 'github'
})

// 登录成功
track('login_success', {
  method: 'email' | 'phone' | 'wechat' | 'google' | 'github',
  duration: 1234  // 毫秒
})

// 登录失败
track('login_fail', {
  method: 'email' | 'phone' | 'wechat' | 'google' | 'github',
  reason: 'wrong_password' | 'account_not_exist' | 'network_error'
})
```

---

## 六、测试用例

### 6.1 功能测试
- [ ] 邮箱+密码登录成功
- [ ] 邮箱+密码登录失败（密码错误）
- [ ] 手机号+验证码登录成功
- [ ] 验证码过期提示
- [ ] 微信登录成功
- [ ] 第三方登录账号绑定

### 6.2 异常测试
- [ ] 网络断开时的提示
- [ ] 验证码发送失败的提示
- [ ] 账号被锁定的提示

---

## 七、上线计划

### 7.1 灰度发布
- **第 1 天**：5% 用户
- **第 3 天**：20% 用户
- **第 5 天**：50% 用户
- **第 7 天**：100% 用户

### 7.2 回滚方案
如果登录成功率 < 90%，立即回滚到旧版本

---

## 八、FAQ

### Q1：为什么要支持手机号登录？
A：移动端用户输入密码体验差，验证码登录更方便。

### Q2：为什么不支持 Apple 登录？
A：Apple 登录需要企业开发者账号，暂时不支持。后续会加入。

### Q3：第三方登录的账号如何绑定？
A：首次使用第三方登录时，如果邮箱已存在，自动绑定；如果不存在，创建新账号。

---

## 九、相关文档

- [用户研究报告](./research-user-interview-2026q1.md)
- [竞品分析：Slack](./competitive-slack.md)
- [设计稿](https://figma.com/xxx)
- [技术方案](https://wiki.company.com/tech/login)
- [测试报告](https://wiki.company.com/qa/login-test)

---

## 十、变更记录

| 版本 | 日期 | 变更内容 | 负责人 |
|------|------|----------|--------|
| v2.0 | 2026-04-15 | 新增手机号登录、第三方登录 | 王五 |
| v1.0 | 2025-12-01 | 初版，仅支持邮箱+密码登录 | 王五 |
```

---

### 示例 3：用户反馈整理（task）

**文件**：`pages/feedback-feature-requests.md`

```markdown
---
title: "功能需求反馈汇总"
type: "task"
area: "feedback"
tags: ["反馈", "需求"]
updated: "2026-04-17"
---

# 功能需求反馈汇总

## 本周新增反馈（2026-04-14 ~ 2026-04-17）

### 高优先级（P0）

#### #1234 - 支持批量导出数据
- **来源**：客户 A（企业版用户）
- **描述**：希望能一键导出所有数据为 Excel
- **频次**：本周 5 个用户提出
- **状态**：已排期到 v2.4
- **负责人**：王五
- **相关 PRD**：[数据导出功能](./prd-data-export.md)

#### #1235 - 移动端推送通知
- **来源**：用户调研
- **描述**：希望重要消息能推送到手机
- **频次**：本周 8 个用户提出
- **状态**：评审中
- **负责人**：王五

### 中优先级（P1）

#### #1236 - 深色模式
- **来源**：社区反馈
- **描述**：希望支持深色主题
- **频次**：本周 3 个用户提出
- **状态**：待评审
- **负责人**：待分配

#### #1237 - 快捷键支持
- **来源**：高级用户
- **描述**：希望支持键盘快捷键操作
- **频次**：本周 2 个用户提出
- **状态**：待评审
- **负责人**：待分配

---

## 历史反馈（已处理）

### 已实现（v2.3）
- [x] #1200 - 支持第三方登录（2026-04-15 上线）
- [x] #1201 - 优化支付流程（2026-04-15 上线）
- [x] #1202 - 增加通知系统（2026-04-15 上线）

### 已拒绝
- [ ] #1150 - 支持区块链钱包登录
  - **拒绝原因**：用户需求不明确，技术成本高
  - **决策人**：王五
  - **决策时间**：2026-03-20

---

## 反馈统计

### 按来源统计
- 客户反馈：45%
- 用户调研：30%
- 社区反馈：15%
- 内部提出：10%

### 按优先级统计
- P0（高）：12 个
- P1（中）：28 个
- P2（低）：45 个

### 按状态统计
- 已实现：35 个
- 开发中：8 个
- 已排期：12 个
- 评审中：15 个
- 待评审：25 个
- 已拒绝：10 个

---

## 相关链接

- [产品路线图](./project-roadmap-overview.md)
- [用户研究](./project-research-overview.md)
- [Bug 反馈](./feedback-bug-reports.md)
```

---

## 第五步：使用效果

### 改进前 vs 改进后

| 维度 | 改进前 | 改进后 |
|------|--------|--------|
| 文档查找时间 | 平均 10 分钟 | 平均 30 秒 |
| 新人上手时间 | 2 周 | 3 天 |
| 文档更新频率 | 每月 1 次 | 每周 3 次 |
| 文档覆盖率 | 40% | 85% |
| 团队满意度 | 6/10 | 9/10 |

---

## 第六步：维护建议

### 每周维护
- 整理本周用户反馈
- 更新需求文档状态
- 同步产品路线图

### 每月维护
- 运行 audit 检查死链
- 清理过期文档
- 更新竞品分析

### 每季度维护
- 归档已上线功能的 PRD
- 更新用户画像
- 回顾产品迭代历史

---

## 相关链接

- [学生学习笔记示例](./scenario-student-learning-notes.md)
- [技术团队 Wiki 示例](./scenario-tech-team-wiki.md)
- [返回 README](../README.md)
