#!/bin/bash

# 自动生成 vault profile
# Auto generate vault profile

set -e

# 日志函数
log_info()  { echo "ℹ️  $1"; }
log_warn()  { echo "⚠️  $1"; }
log_ok()    { echo "✅ $1"; }

# 获取 vault 路径 (Get vault path)
if [ -z "$1" ]; then
    echo "请提供 vault 路径（vault path）"
    echo "用法（usage）: $0 <vault_path> [vault_name] [areas]"
    echo "示例（example）: $0 ~/Documents/my-vault '我的笔记' 'learning,work,projects'"
    exit 1
fi

VAULT_PATH="$1"
VAULT_NAME="${2:-我的知识库}"
AREAS="${3:-learning,work,projects}"
TODAY="$(date +%Y-%m-%d)"

echo "正在生成 vault profile（知识库配置文件）..."
echo ""
echo "配置信息（Configuration）:"
echo "  - Vault 路径（path）: ${VAULT_PATH}"
echo "  - Vault 名称（name）: ${VAULT_NAME}"
echo "  - 分类（areas）: ${AREAS}"
echo ""

# 转换 areas 为数组 (Convert areas to array)
IFS=',' read -ra AREA_ARRAY <<< "$AREAS"

# 生成 vault profile (Generate vault profile)
PROFILE_PATH="${VAULT_PATH}/vault-profile.md"

cat > "${PROFILE_PATH}" << 'EOF'
# Vault Profile（知识库配置文件）

> 自动生成于（auto-generated）: __TODAY__

---

## 1. Vault identity（知识库基本信息）

- **Vault name**（知识库名称）: __VAULT_NAME__
- **Vault root path**（知识库根目录）: __VAULT_PATH__
- **Primary markdown page directory**（笔记存放目录）: __VAULT_PATH__/pages
- **Reader entrypoint file**（导航首页）: __VAULT_PATH__/index.md
- **Milestone log file**（里程碑日志）: __VAULT_PATH__/log.md
- **Maintainer entrypoint file**（维护者入口）: __VAULT_PATH__/pages/governance.md

---

## 2. Fixed page-role model（固定页面角色）

这套模板使用 5 种固定页面角色，**不要修改**：
- `project` — 项目文档、导航页
- `knowledge` — 知识沉淀、学习笔记
- `ops` — 操作手册、排障文档
- `task` — 任务清单、待办事项
- `overview` — 总览页、索引页

💡 **不理解这 5 种角色？** 先看 [`GLOSSARY.md`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/blob/main/GLOSSARY.md)

---

## 3. Area list（知识库分类）

| area（分类名） | 用途说明 |
|---|---|
EOF
if command -v python3 &> /dev/null; then
    python3 - "${PROFILE_PATH}" "${VAULT_NAME}" "${VAULT_PATH}" "${TODAY}" <<'PY'
from pathlib import Path
import sys
path, vault_name, vault_path, today = sys.argv[1:]
text = Path(path).read_text(encoding='utf-8')
text = text.replace('__VAULT_NAME__', vault_name).replace('__VAULT_PATH__', vault_path).replace('__TODAY__', today)
Path(path).write_text(text, encoding='utf-8')
PY
else
    log_warn "未检测到 python3，使用 sed 进行变量替换"
    sed -i.bak \
        -e "s|__VAULT_NAME__|${VAULT_NAME}|g" \
        -e "s|__VAULT_PATH__|${VAULT_PATH}|g" \
        -e "s|__TODAY__|${TODAY}|g" \
        "${PROFILE_PATH}"
    rm -f "${PROFILE_PATH}.bak"
fi

# 添加 areas (Add areas)
for area in "${AREA_ARRAY[@]}"; do
    area_trimmed=$(echo "$area" | xargs)
    case "$area_trimmed" in
        learning)
            echo "| \`learning\` | 个人学习笔记 |" >> "${PROFILE_PATH}"
            ;;
        work)
            echo "| \`work\` | 工作相关文档 |" >> "${PROFILE_PATH}"
            ;;
        projects)
            echo "| \`projects\` | 个人项目 |" >> "${PROFILE_PATH}"
            ;;
        *)
            echo "| \`${area_trimmed}\` | ${area_trimmed} 相关内容 |" >> "${PROFILE_PATH}"
            ;;
    esac
done

cat >> "${PROFILE_PATH}" << EOF

---

## 4. Root page map（导航页映射）

每个分类（area）至少需要一个导航页（root page）：

| area（分类） | root page file（导航页文件） | 作用 |
|---|---|---|
EOF

# 添加 root pages (Add root pages)
for area in "${AREA_ARRAY[@]}"; do
    area_trimmed=$(echo "$area" | xargs)
    echo "| \`${area_trimmed}\` | \`pages/project-${area_trimmed}-overview.md\` | ${area_trimmed} 的导航入口 |" >> "${PROFILE_PATH}"
done

cat >> "${PROFILE_PATH}" << 'EOF'

---

## 5. Canonical root-level markdown files（允许放在根目录的文件）

只有以下 markdown 文件允许直接放在 vault 根目录：
- `README.md` — 项目说明
- `index.md` — 导航首页
- `log.md` — 里程碑日志
- `vault-profile.md` — 本配置文件

💡 **其他 markdown 文件应该放在哪？**
- 放到 `pages/` 目录

---

## 6. Frontmatter contract（文件头部元数据规则）

每个笔记文件开头必须包含这些信息：

### 最少字段（必填）
```yaml
---
title: "笔记标题"
type: "knowledge"  # 必须是 project/knowledge/ops/task/overview 之一
area: "learning"   # 必须是你在上面定义的 area 之一
tags: ["python", "tutorial"]  # 标签，方便搜索
updated: "2026-04-17"  # 最后更新日期
---
```

### 可选字段
```yaml
status: "draft"  # 草稿/完成状态
owner: "张三"    # 负责人
created: "2026-04-01"  # 创建日期
```

---

## 7. Naming conventions（文件命名规则）

建议遵循以下命名规则：

- **Root pages（导航页）**：统一以 `project-` 开头
  - 示例：`project-learning-overview.md`

- **Ops pages（操作手册）**：用 `-ops` / `-runbook` / `-troubleshooting` 结尾
  - 示例：`redis-ops.md`、`deployment-runbook.md`

- **Task pages（任务清单）**：用 `-tasks` / `-todo` 结尾
  - 示例：`q2-tasks.md`、`weekly-todo.md`

- **Overview pages（总览页）**：用 `-overview` / `-index` 结尾
  - 示例：`workspace-overview.md`

---

## 8. Writing rules switches（写作规则开关）

请明确这几个开关（建议全部选 `yes`）：

- **Knowledge-base-first mode**（知识库优先模式）: `yes`
  - 💡 只保留长期有用的内容，过滤掉临时过程

- **Milestone-only log**（里程碑日志模式）: `yes`
  - 💡 log.md 只记录重要变化，不记录流水账

- **`ops` page four-part pattern**（ops 页四段式结构）: `yes`
  - 💡 ops 页统一写成：现象 / 根因 / 处理法 / 边界

- **Root pages should avoid long process narration**（根页避免长流水）: `yes`
  - 💡 导航页只做导航，不堆积执行细节

---

## 9. Maintenance expectations（维护要求）

每次实质更新至少同步这 4 个地方：
1. ✅ 目标页面本身
2. ✅ 对应的 root page（导航页）
3. ✅ reader entrypoint（index.md）
4. ✅ milestone log（log.md）

---

## 10. Audit priorities（审计优先级）

默认优先级（建议不修改）：
1. **结构问题**（死链、孤立页、缺失 frontmatter）
2. **导航问题**（缺少入口、root page 覆盖不全）
3. **治理漂移**（页面角色混乱、边界不清）
4. **噪音回流**（临时内容混入知识库）

---

## ✅ 配置完成

这个 vault profile 已经可以使用了！

**下一步（Next Steps）**：
1. 如果你还想继续走初始化入口：使用 `knowledge-base-orchestrator`
2. 如果你想先理解结构和 skill 分流：使用 `knowledge-base-kit-guide`
3. 如果你要导入长文档：使用 `knowledge-base-ingest`
4. 如果你要把结果沉淀进知识库：使用 `knowledge-base-maintenance`
5. 如果你要做结构检查：使用 `knowledge-base-audit`
6. 如果你要沉淀协作画像：使用 `knowledge-base-working-profile`
7. 如果你要协调多人项目：使用 `knowledge-base-team-coordination`
8. 如果你要记录每日工作 / 会议 / 周报：使用 `work-journal`

**需要帮助？**
- 📖 查看 [START-HERE.md](https://github.com/zouxy111/wiki-knowledgebase-share-kit/blob/main/START-HERE.md)
- 📖 查看 [GLOSSARY.md](https://github.com/zouxy111/wiki-knowledgebase-share-kit/blob/main/GLOSSARY.md)
- 📝 查看 [示例](https://github.com/zouxy111/wiki-knowledgebase-share-kit/tree/main/examples)
- 💬 提问 [GitHub Issues](https://github.com/zouxy111/wiki-knowledgebase-share-kit/issues)
EOF

echo "✅ vault profile 生成完成！"
echo "Vault profile generated successfully!"
echo ""
echo "文件位置（file location）: ${PROFILE_PATH}"
echo ""
echo "现在可以使用这个 profile 了（you can now use this profile）:"
echo "  Use \$knowledge-base-kit-guide with profile: ${PROFILE_PATH}"
echo "  Use \$knowledge-base-orchestrator if you still need guided setup"
echo "  Use \$knowledge-base-ingest / \$knowledge-base-maintenance / \$knowledge-base-audit / \$knowledge-base-working-profile / \$knowledge-base-team-coordination / \$work-journal as needed"
