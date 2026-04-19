# Local Overlay Example

这个目录只是一个 **结构示意**，说明怎样在不污染核心 8-skill package 的情况下承接本地定制。

## 目标

- 核心 skill 继续从本仓库安装
- 团队私有规则、路径、术语、审批流程放在本地 overlay
- 验证成熟后，再决定是否把某些做法回提到核心仓库

## 一个常见布局

```text
local-overlay/
├── README.md
├── team-conventions.md
├── private-root-page-map.md
├── prompt-fragments/
│   ├── ingest-team-rules.md
│   └── audit-risk-labels.md
└── references/
    └── internal-sop-links.md
```

## 使用方式

1. 先把本仓库的 8 个核心 skill 安装到 runtime。
2. 再把你团队私有的补充材料放到单独的 overlay 目录。
3. 在日常 prompt 里明确说明哪些本地资料属于 overlay。
4. 不要把私有路径、内部命名、客户专有字段直接写回核心 skill。

更多边界说明见 [`docs/core-vs-local-overlay.md`](../../docs/core-vs-local-overlay.md)。
