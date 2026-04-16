# Questionnaire and Status Rules

## Questionnaire generation rule
问卷必须来自：
- 角色模板
- 加上项目定制

不要完全自由生成到失去可比性。

## Required question families
每位成员都至少覆盖：
1. 目标理解
2. 资料 / 证据掌握
3. 输出颗粒度
4. 依赖关系
5. 约束
6. 待确认决策

## Role-template examples
### 通用角色模板思路
- 事实 owner：强调证据来源、边界、未证实项
- 转译 owner：强调读者对象、表达方式、输出格式
- 审查 owner：强调验收门槛、风险点、冲突检查
- 执行 owner：强调输入完整度、依赖、完成定义

### QC 默认示例
- 技术事实 owner
- 表达转译 owner
- 评审审查 owner

这些只是示例层，不应写死为唯一产品角色模型。

## Status semantics
- `draft`：已生成，但未确认，不应作为正式事实源
- `approved`：已确认，可作为后续协调或同步依据
- `superseded`：曾经有效，但已被新版本替代
- `blocked`：当前信息不足或依赖未解决，不能继续推进

## Granularity mismatch handling
如果发现：
- 某成员回答过粗
- 某成员回答过细
- 不同成员的任务理解颗粒度不一致

则：
1. 在 `alignment-summary.md` 显式记录
2. 自动生成 follow-up questions
3. 在未补齐前，让 assignment 保持 `draft` 或 `blocked`
