# Core Skills vs Local Overlay

这套仓库里的 `skills/` 目录应该尽量保持为 **shareable core**：
- 方法论稳定
- 不写死个人路径
- 不绑定单一团队命名
- 可以直接复制到别人的 runtime 里安装

真正和你团队环境强相关的内容，建议放进 **local overlay**，而不是直接改核心 skill。

## 什么属于 core

适合留在核心包里的内容：
- 通用 page-role 模型
- vault profile 的字段契约
- 审计 / ingest / maintenance 的固定 workflow
- 可公开复用的 prompt wording
- 不依赖私有路径和私有数据的 references

## 什么属于 local overlay

更适合放在 overlay 里的内容：
- 团队专有 root page 名称
- 特定项目 area 名称
- 私有 SOP、命名约定、审批路径
- 只在你自己的 runtime / workspace 有意义的 prompt 片段
- 实验性 skill 变体

## 推荐做法

1. 把本仓库当成 public core。
2. 在你自己的私有 workspace 或 runtime skills 目录里建立 overlay。
3. 在 overlay 里补团队私有 references、模板、示例 prompt。
4. 如果某个 overlay 规则被反复验证为通用，再考虑回提到 core。

## 一个轻量结构示例

```text
your-private-workspace/
├── runtime-skills/
│   ├── knowledge-base-kit-guide/          # 从本仓库安装而来
│   ├── knowledge-base-ingest/             # 从本仓库安装而来
│   └── your-team-overlay/                 # 你团队自己的 overlay
├── shared-project/
└── private-references/
```

## 什么时候该直接改 core

满足这些条件时，更适合改核心仓库：
- 这个改动不依赖你的本地路径或私有数据
- 它提升的是整个 kit 的复用性或可维护性
- 它能通过 catalog / validator / docs sync 这样的公共约束

## 什么时候不要改 core

以下情况优先放 overlay：
- 只是你团队自己的叫法
- 需要引用私有 wiki、内部文档或客户资料
- 只在一个项目里短期成立
- 还在试验阶段，没有证明能复用
