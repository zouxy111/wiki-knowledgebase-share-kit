---
name: knowledge-base-delivery-audit
description: This skill should be used when the user wants to audit delivery completeness, handoff readiness, evidence gaps, acceptance gaps, greenlight readiness, or distinguish real completion from merely claimed completion. Use it for 交付审计, 验收检查, ready/blocked/greenlight, handoff review, delivery completeness, 回写是否完整, or project closeout gating. It reads project artifacts and checks evidence, decisions, routing, and readiness rather than doing vault-structure audit.
---

# Knowledge Base Delivery Audit

这个 skill 负责 **项目交付 / 回写 / 验收 / gate 审计**。

它不是：
- `knowledge-base-audit` 的同义词
- 知识库结构健康检查
- 多人协同问卷工具

它的职责是：
- 检查“任务声称完成”是否真的闭环
- 检查证据、决策、handoff、回写是否齐全
- 判断当前状态应是 `ready / blocked / greenlight pending`
- 明确缺口、风险和下一步补齐动作
- 判断结果该回原业务 area，还是仍停留在 task / draft 层

## When to use
- 用户说“这个项目完成了”，但需要严审是否真完成
- 用户要做交付前检查、handoff 检查、结项检查
- 用户要区分“口头完成”和“可 greenlight”
- 用户要审“该不该回写业务 area、该不该批准 closeout”

## When not to use
- 只是检查 dead links / orphan pages / metadata → 用 `knowledge-base-audit`
- 只是做项目拆解 / 周计划 / blocker 管理 → 用 `knowledge-base-project-management`
- 只是协调多人问卷与派单 → 用 `knowledge-base-team-coordination`

## Required input
默认优先读取：
- 项目 brief / 成功标准
- 当前任务板 / assignment / status artifacts
- 相关 evidence / deliverables / docs / decision records
- 如涉及知识库落页，则读取 vault profile 与目标 area 页面

## Core audit questions
1. 目标是否有清晰完成定义？
2. 已完成项有没有证据支撑？
3. 关键决策是否被记录？
4. 需要回写的业务知识是否已回到原 area？
5. handoff 所需材料是否齐全？
6. 当前更合理的状态是 `ready`、`blocked` 还是仍需补件？

## Output expectations
至少输出：
- 交付范围摘要
- 已满足项
- 缺口项
- 风险项
- 当前 gate 结论
- 需要谁补什么、补到哪份文件

## Recommended gate language
- `ready`：交付闭环基本成立，可进入人工确认 / closeout
- `blocked`：关键证据、决策或回写缺失
- `greenlight pending`：主体已齐，但仍需批准动作，不要提前宣告 greenlight

## Additional resources
- `references/audit-checklist.md`
- `references/evidence-model.md`
- `references/gate-model.md`
- `references/routing-boundaries.md`
- `../../docs/project-management-workflow.md`
- `../../templates/project-management/pm-delivery-gates.md`
