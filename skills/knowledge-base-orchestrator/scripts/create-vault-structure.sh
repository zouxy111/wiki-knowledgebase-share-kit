#!/bin/bash

# 创建标准 vault 文件夹结构
# Create standard vault folder structure

set -e

# 日志函数
log_info()  { echo "ℹ️  $1"; }
log_warn()  { echo "⚠️  $1"; }
log_ok()    { echo "✅ $1"; }

# 获取 vault 路径 (Get vault path)
if [ -z "$1" ]; then
    echo "请提供 vault 路径（vault path）"
    echo "用法（usage）: $0 <vault_path>"
    echo "示例（example）: $0 ~/Documents/my-vault"
    exit 1
fi

VAULT_PATH="$1"
TODAY="$(date +%Y-%m-%d)"

echo "正在创建 vault 文件夹结构（folder structure）..."
echo "路径（path）: ${VAULT_PATH}"
echo ""

# 创建主目录 (Create main directory)
mkdir -p "${VAULT_PATH}"
echo "✅ 创建主目录（main directory）: ${VAULT_PATH}"

# 创建 pages 目录 (Create pages directory)
mkdir -p "${VAULT_PATH}/pages"
echo "✅ 创建笔记目录（notes directory）: ${VAULT_PATH}/pages"

# 创建 .obsidian 配置目录 (Create .obsidian config directory)
mkdir -p "${VAULT_PATH}/.obsidian"
echo "✅ 创建配置目录（config directory）: ${VAULT_PATH}/.obsidian"

echo ""
echo "正在创建必要文件（essential files）..."
echo ""

# 创建 index.md (Create index.md)
cat > "${VAULT_PATH}/index.md" << 'EOF'
---
title: "知识库导航"
type: "overview"
area: "governance"
updated: "__TODAY__"
---

# 知识库导航

欢迎来到你的知识库！

## 主要分类（Main Categories）
- [学习笔记](./pages/project-learning-overview.md)
- [工作文档](./pages/project-work-overview.md)
- [个人项目](./pages/project-projects-overview.md)

## 快速链接（Quick Links）
- [里程碑日志](./log.md)
- [维护规则](./pages/governance.md)

---

**提示（Tips）**：
- 所有笔记都放在 `pages/` 目录下
- 每个笔记都要有 frontmatter（元数据）
- 定期运行 audit（健康检查）保持知识库整洁
EOF

echo "✅ 创建导航首页（navigation homepage）: index.md"

# 创建 log.md (Create log.md)
cat > "${VAULT_PATH}/log.md" << EOF
---
title: "里程碑日志"
type: "overview"
area: "governance"
updated: "$(date +%Y-%m-%d)"
---

# 里程碑日志（Milestone Log）

记录知识库的重要变化（important changes）。

## $(date +%Y-%m-%d)
- 🎉 知识库初始化完成（vault initialized）
- 📁 创建标准文件夹结构（created standard folder structure）
- 📄 创建必要文件（created essential files）

---

**日志规则（Log Rules）**：
- 只记录重要变化（milestone changes only）
- 不记录日常任务（no daily tasks）
- 每条记录包含日期和简短描述
EOF

echo "✅ 创建里程碑日志（milestone log）: log.md"

# 创建 README.md (Create README.md)
cat > "${VAULT_PATH}/README.md" << 'EOF'
# 我的知识库

这是使用 wiki-knowledgebase-share-kit 创建的知识库。

## 快速开始（Quick Start）
1. 查看 [导航页](./index.md)
2. 阅读 [维护规则](./pages/governance.md)
3. 开始写第一篇笔记

## 文件结构（File Structure）
```
my-vault/
├── index.md          # 导航首页（navigation homepage）
├── log.md            # 里程碑日志（milestone log）
├── README.md         # 说明文档（documentation）
└── pages/            # 笔记目录（notes directory）
    ├── project-*-overview.md   # 导航页（navigation pages）
    └── *.md                    # 笔记文件（note files）
```

## 页面角色（Page Roles）
- `project` - 项目文档、导航页
- `knowledge` - 知识沉淀、学习笔记
- `ops` - 操作手册、排障文档
- `task` - 任务清单、待办事项
- `overview` - 总览页、索引页

## 维护建议（Maintenance Tips）
- 每周运行一次 audit（健康检查）
- 每次写完笔记后运行 maintenance（笔记整理）
- 定期清理临时文件（temporary files）
EOF

echo "✅ 创建说明文档（documentation）: README.md"

# 创建 governance.md (Create governance.md)
cat > "${VAULT_PATH}/pages/governance.md" << 'EOF'
---
title: "维护规则"
type: "overview"
area: "governance"
updated: "__TODAY__"
---

# 维护规则（Governance Rules）

## 文件命名规则（Naming Conventions）

### 导航页（Navigation Pages）
- 统一以 `project-` 开头
- 格式：`project-{area}-overview.md`
- 示例：`project-learning-overview.md`

### 知识页（Knowledge Pages）
- 使用清晰的描述性名称
- 用连字符分隔单词
- 示例：`python-basics.md`, `react-hooks-guide.md`

### 操作手册（Ops Pages）
- 以 `-ops` 或 `-runbook` 结尾
- 示例：`redis-ops.md`, `deployment-runbook.md`

### 任务清单（Task Pages）
- 以 `-tasks` 或 `-todo` 结尾
- 示例：`q2-tasks.md`, `weekly-todo.md`

## Frontmatter 规则（Metadata Rules）

每个文件必须包含（must include）：
```yaml
---
title: "页面标题"
type: "页面角色（project/knowledge/ops/task/overview）"
area: "分类（learning/work/projects）"
tags: ["标签1", "标签2"]
updated: "最后更新日期（YYYY-MM-DD）"
---
```

## 维护频率（Maintenance Frequency）

- **每天（Daily）**：写完笔记后运行 maintenance
- **每周（Weekly）**：运行 audit 检查健康度
- **每月（Monthly）**：清理临时文件和过期内容

## 质量标准（Quality Standards）

- ✅ 所有页面都有 frontmatter（元数据）
- ✅ 所有页面都能从导航找到（no orphan pages）
- ✅ 没有死链（no dead links）
- ✅ 根目录只保留必要文件
- ✅ 临时内容不进入知识库
EOF

echo "✅ 创建维护规则（governance rules）: pages/governance.md"

# 替换占位符（兼容无 perl 环境）
for file in "${VAULT_PATH}/index.md" "${VAULT_PATH}/pages/governance.md"; do
    if command -v perl &> /dev/null; then
        perl -0pi -e "s/__TODAY__/${TODAY}/g" "$file"
    elif command -v sed &> /dev/null; then
        sed -i.bak "s/__TODAY__/${TODAY}/g" "$file" && rm -f "${file}.bak"
    else
        log_warn "未检测到 perl 或 sed，请手动将 ${file} 中的 __TODAY__ 替换为 ${TODAY}"
    fi
done

# 创建默认导航页 (Create default navigation pages)
for area in learning work projects; do
    case "$area" in
        learning) area_title="Learning" ;;
        work) area_title="Work" ;;
        projects) area_title="Projects" ;;
        *) area_title="$area" ;;
    esac
    cat > "${VAULT_PATH}/pages/project-${area}-overview.md" << EOF
---
title: "${area_title} 总览"
type: "project"
area: "${area}"
updated: "$(date +%Y-%m-%d)"
---

# ${area_title} 总览

## 当前内容（Current Content）
（暂无内容，开始添加你的第一篇笔记吧！）

## 相关链接（Related Links）
- [知识库导航](../index.md)
- [维护规则](./governance.md)
EOF
    echo "✅ 创建导航页（navigation page）: pages/project-${area}-overview.md"
done

echo ""
echo "🎉 文件夹结构创建完成！"
echo "Folder structure created successfully!"
echo ""
echo "📁 已创建（Created）:"
echo "  ${VAULT_PATH}/"
echo "  ├── index.md          # 导航首页（navigation homepage）"
echo "  ├── log.md            # 里程碑日志（milestone log）"
echo "  ├── README.md         # 说明文档（documentation）"
echo "  ├── .obsidian/        # Obsidian 配置（config）"
echo "  └── pages/            # 笔记目录（notes directory）"
echo "      ├── governance.md                  # 维护规则（governance rules）"
echo "      ├── project-learning-overview.md   # 学习笔记导航"
echo "      ├── project-work-overview.md       # 工作文档导航"
echo "      └── project-projects-overview.md   # 项目导航"
echo ""
echo "下一步（Next Steps）:"
echo "1. 用 knowledge-base-kit-guide 或 knowledge-base-orchestrator 检查初始化状态"
echo "2. 确认或补充 vault-profile.md"
echo "3. 再进入 \$knowledge-base-ingest / \$knowledge-base-maintenance / \$knowledge-base-audit / \$knowledge-base-working-profile / \$knowledge-base-team-coordination / \$work-journal"
echo "4. 如果后续需要项目 owner / 里程碑 / blocker / handoff 主线，再按需启用 \$knowledge-base-project-management / \$knowledge-base-delivery-audit"
