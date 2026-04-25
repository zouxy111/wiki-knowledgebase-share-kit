#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export PYTHONPATH="${SCRIPT_DIR}${PYTHONPATH:+:${PYTHONPATH}}"

python3 -m wiki_knowledgebase_share_kit verify "$@"
exit $?


SKILLS=(
    knowledge-base-kit-guide
    knowledge-base-orchestrator
    knowledge-base-ingest
    knowledge-base-maintenance
    knowledge-base-audit
    knowledge-base-project-management
    knowledge-base-team-coordination
    knowledge-base-delivery-audit
    knowledge-base-working-profile
    work-journal
)
SKILL_COUNT=${#SKILLS[@]}

TARGET_DIR=""
VERBOSE=false

usage() {
    cat << EOF
Usage: $0 [OPTIONS] [SKILLS_DIR]

Verify that the 10-skill wiki-knowledgebase-share-kit is correctly installed.

OPTIONS:
    -v, --verbose      Show detailed output for each skill
    -h, --help         Show this help message

SKILLS_DIR:
    Directory to verify. If omitted, auto-detect from supported platforms.
EOF
}

# 自动检测平台
detect_platform() {
    local candidates=(
        "${HOME}/.kimi/skills"
        "${HOME}/.claude/skills"
        "${HOME}/.codex/skills"
        "${HOME}/.agents/skills"
    )
    for dir in "${candidates[@]}"; do
        if [ -d "$dir" ]; then
            echo "$dir"
            return 0
        fi
    done
    return 1
}

# 解析参数
while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        -*)
            log_error "Unknown option: $1"
            usage
            exit 1
            ;;
        *)
            TARGET_DIR="$1"
            shift
            ;;
    esac
done

if [ -z "$TARGET_DIR" ]; then
    TARGET_DIR=$(detect_platform) || {
        log_error "No skills directory detected. Please specify one."
        exit 1
    }
fi

TARGET_DIR="$(cd "$(dirname "$TARGET_DIR")" && pwd)/$(basename "$TARGET_DIR")"

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Wiki Knowledge Base Share Kit — Verification              ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
log_info "Checking directory: ${TARGET_DIR}"
echo ""

# 检查目标目录是否存在
if [ ! -d "$TARGET_DIR" ]; then
    log_error "Directory does not exist: ${TARGET_DIR}"
    exit 1
fi

# 检查每个 skill
total_checks=0
passed_checks=0
failed_skills=()

for skill_name in $SKILLS; do
    skill_dir="${TARGET_DIR}/${skill_name}"
    skill_ok=true
    issues=()

    # 检查目录是否存在
    if [ ! -d "$skill_dir" ]; then
        issues+=("Directory missing")
        skill_ok=false
    else
        # 检查 SKILL.md
        if [ ! -f "${skill_dir}/SKILL.md" ]; then
            issues+=("SKILL.md missing")
            skill_ok=false
        else
            # 检查 frontmatter
            if ! grep -qE "^name:\s*" "${skill_dir}/SKILL.md"; then
                issues+=("SKILL.md missing 'name' frontmatter")
                skill_ok=false
            fi
            if ! grep -qE "^description:\s*" "${skill_dir}/SKILL.md"; then
                issues+=("SKILL.md missing 'description' frontmatter")
                skill_ok=false
            fi
        fi

        # 检查 agents/openai.yaml
        if [ ! -f "${skill_dir}/agents/openai.yaml" ]; then
            issues+=("agents/openai.yaml missing")
            skill_ok=false
        fi

        # 检查 references/ 目录
        if [ ! -d "${skill_dir}/references" ]; then
            issues+=("references/ directory missing")
            skill_ok=false
        elif [ -z "$(ls -A "${skill_dir}/references")" ]; then
            issues+=("references/ directory is empty")
            skill_ok=false
        fi
    fi

    total_checks=$((total_checks + 1))

    if [ "$skill_ok" = true ]; then
        passed_checks=$((passed_checks + 1))
        if [ "$VERBOSE" = true ]; then
            log_ok "${skill_name}"
        fi
    else
        failed_skills+=("$skill_name")
        log_error "${skill_name}"
        for issue in "${issues[@]}"; do
            echo "      → ${issue}"
        done
    fi
done

# 检查冲突 skill（同名但非本项目的 skill）
echo ""
log_info "Checking for potential naming conflicts..."
conflicts=()
for skill_name in $SKILLS; do
    skill_dir="${TARGET_DIR}/${skill_name}"
    if [ -d "$skill_dir" ]; then
        # 检查是否真的是本项目的 skill（通过检查 SKILL.md frontmatter 中的 name 字段）
        if [ -f "${skill_dir}/SKILL.md" ]; then
            if ! grep -Eq "^name:[[:space:]]*${skill_name}[[:space:]]*$" "${skill_dir}/SKILL.md" 2>/dev/null; then
                conflicts+=("$skill_name")
                continue
            fi
            if [ "$skill_name" != "work-journal" ] && ! grep -q "wiki-knowledgebase-share-kit\|knowledge-base" "${skill_dir}/SKILL.md" 2>/dev/null; then
                conflicts+=("$skill_name")
            fi
        fi
    fi
done

if [ ${#conflicts[@]} -gt 0 ]; then
    log_warn "Potential conflicts detected (same name, different source):"
    for c in "${conflicts[@]}"; do
        echo "      → ${c}"
    done
else
    log_ok "No naming conflicts detected"
fi

# 汇总
echo ""
echo "══════════════════════════════════════════════════════════════"
if [ $passed_checks -eq $total_checks ]; then
    log_ok "Verification PASSED: ${passed_checks}/${total_checks} skills OK"
    echo ""
    echo "Your wiki-knowledgebase-share-kit is ready to use!"
    exit 0
else
    log_error "Verification FAILED: ${passed_checks}/${total_checks} skills OK"
    echo ""
    echo "Failed skills:"
    for s in "${failed_skills[@]}"; do
        echo "  - ${s}"
    done
    echo ""
    echo "Run the installer to fix:"
    echo "  ./install.sh ${TARGET_DIR}"
    exit 1
fi
