#!/bin/bash

# Wiki Knowledge Base Share Kit — 一键安装脚本
# One-click installer for the 10-skill knowledge-base package

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SCRIPT_DIR}/skills"

# 10 个核心 skill 列表
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

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 参数解析
DRY_RUN=false
BACKUP=false
TARGET_DIR=""
LAST_INSTALL_ACTION=""

usage() {
    cat << EOF
Usage: $0 [OPTIONS] [TARGET_DIR]

Install the 10-skill wiki-knowledgebase-share-kit to your AI platform's skills directory.

OPTIONS:
    -d, --dry-run      Show what would be installed without making changes
    -b, --backup       Backup existing skills before overwriting
    -h, --help         Show this help message

TARGET_DIR:
    Explicitly specify the skills directory. If omitted, auto-detect from supported platforms.

SUPPORTED PLATFORMS (auto-detected in order):
    ~/.kimi/skills       (Kimi CLI)
    ~/.claude/skills     (Claude Code)
    ~/.codex/skills      (Codex)
    ~/.agents/skills     (Generic agents)

EXAMPLES:
    $0                              # Auto-detect and install
    $0 --dry-run                    # Preview installation
    $0 --backup ~/.agents/skills    # Install with backup
    $0 ~/.kimi/skills               # Install to specific directory
EOF
}

log_info()  { echo -e "${BLUE}ℹ️  $1${NC}"; }
log_ok()    { echo -e "${GREEN}✅ $1${NC}"; }
log_warn()  { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }

# 即使父目录还不存在，也尽量把目标解析成稳定的绝对路径
resolve_target_dir_path() {
    local path="$1"
    local base tail

    case "$path" in
        "~")
            path="$HOME"
            ;;
        "~/"*)
            path="${HOME}/${path#~/}"
            ;;
    esac

    if [[ "$path" != /* ]]; then
        path="${PWD}/${path}"
    fi

    tail=""
    while [ ! -d "$path" ]; do
        base="$(basename "$path")"
        tail="/${base}${tail}"
        if [ "$path" = "/" ]; then
            break
        fi
        path="$(dirname "$path")"
    done

    if [ -d "$path" ]; then
        path="$(cd "$path" && pwd -P)"
    fi

    printf '%s%s\n' "${path%/}" "$tail"
}

# 检测平台并返回 skills 目录
detect_platform() {
    local candidates=(
        "${HOME}/.kimi/skills"
        "${HOME}/.claude/skills"
        "${HOME}/.codex/skills"
        "${HOME}/.agents/skills"
    )

    for dir in "${candidates[@]}"; do
        # 处理符号链接：如果指向已存在的目录，则视为有效
        if [ -e "$dir" ]; then
            if [ -L "$dir" ]; then
                local real_dir
                real_dir="$(readlink -f "$dir" 2>/dev/null || readlink "$dir" 2>/dev/null || true)"
                if [ -n "$real_dir" ] && [ -d "$real_dir" ]; then
                    echo "$dir"
                    return 0
                fi
            elif [ -d "$dir" ]; then
                echo "$dir"
                return 0
            fi
        fi
    done

    # 未检测到任何平台，询问用户
    return 1
}

# 解析符号链接获取真实路径
resolve_symlink() {
    local path="$1"
    if [ -d "$path" ]; then
        (
            cd "$path" && pwd -P
        )
    elif [ -L "$path" ]; then
        readlink -f "$path" 2>/dev/null || readlink "$path" 2>/dev/null || echo "$path"
    else
        echo "$path"
    fi
}

# 检查目录是否已包含本项目的 skill
is_same_target() {
    local src="$1"
    local dest="$2"
    local src_real dest_real
    src_real="$(resolve_symlink "$src")"
    dest_real="$(resolve_symlink "$dest")"
    [ "$src_real" = "$dest_real" ]
}

# 安装单个 skill
install_skill() {
    local skill_name="$1"
    local src="${SKILLS_DIR}/${skill_name}"
    local dest="${TARGET_DIR}/${skill_name}"
    LAST_INSTALL_ACTION="error"

    if [ ! -d "$src" ]; then
        log_error "Source directory not found: $src"
        return 1
    fi

    if [ -L "$dest" ] && is_same_target "$src" "$dest"; then
        log_warn "${skill_name} is already a symlink to source — skipping"
        LAST_INSTALL_ACTION="skipped"
        return 0
    fi

    if [ -e "$dest" ]; then
        if [ "$BACKUP" = true ]; then
            local backup_name="${skill_name}.backup.$(date +%Y%m%d_%H%M%S)"
            if [ "$DRY_RUN" = false ]; then
                mv "$dest" "${TARGET_DIR}/${backup_name}"
                log_ok "Backed up existing skill: ${skill_name} → ${backup_name}"
            else
                log_info "[DRY-RUN] Would backup: ${dest} → ${TARGET_DIR}/${backup_name}"
            fi
        else
            if [ "$DRY_RUN" = false ]; then
                log_warn "Overwriting existing skill: ${skill_name}"
                rm -rf "$dest"
            else
                log_info "[DRY-RUN] Would overwrite: ${dest}"
            fi
        fi
    fi

    if [ "$DRY_RUN" = false ]; then
        cp -r "$src" "$dest"
        log_ok "Installed: ${skill_name}"
    else
        log_info "[DRY-RUN] Would copy: ${src} → ${dest}"
    fi

    LAST_INSTALL_ACTION="installed"
}

# 主逻辑
main() {
    echo ""
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║  Wiki Knowledge Base Share Kit — Installer                 ║"
    echo "║  10-skill knowledge-base package installer                 ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo ""

    # 解析参数
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -d|--dry-run)
                DRY_RUN=true
                shift
                ;;
            -b|--backup)
                BACKUP=true
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
                if [ -z "$TARGET_DIR" ]; then
                    TARGET_DIR="$1"
                else
                    log_error "Multiple target directories specified"
                    usage
                    exit 1
                fi
                shift
                ;;
        esac
    done

    # 检测目标目录
    if [ -z "$TARGET_DIR" ]; then
        log_info "Detecting AI platform..."
        TARGET_DIR=$(detect_platform) || {
            log_error "No supported AI platform detected."
            echo ""
            echo "Supported platforms (checked in order):"
            echo "  ~/.kimi/skills       (Kimi CLI)"
            echo "  ~/.claude/skills     (Claude Code)"
            echo "  ~/.codex/skills      (Codex)"
            echo "  ~/.agents/skills     (Generic agents)"
            echo ""
            echo "Please create one of these directories first, or specify a target directory:"
            echo "  $0 ~/.kimi/skills"
            exit 1
        }
        log_ok "Detected platform skills directory: ${TARGET_DIR}"
    else
        TARGET_DIR="$(resolve_target_dir_path "$TARGET_DIR")"
        log_info "Using specified directory: ${TARGET_DIR}"
    fi

    # 创建目标目录（如果不存在）
    if [ ! -d "$TARGET_DIR" ]; then
        if [ "$DRY_RUN" = false ]; then
            mkdir -p "$TARGET_DIR"
            log_ok "Created directory: ${TARGET_DIR}"
        else
            log_info "[DRY-RUN] Would create directory: ${TARGET_DIR}"
        fi
    fi

    # 检查前置条件
    log_info "Checking prerequisites..."
    local missing=0
    for skill_name in "${SKILLS[@]}"; do
        if [ ! -d "${SKILLS_DIR}/${skill_name}" ]; then
            log_error "Missing source skill: ${skill_name}"
            missing=$((missing + 1))
        fi
    done
    if [ $missing -gt 0 ]; then
        log_error "${missing} skill(s) missing from ${SKILLS_DIR}"
        exit 1
    fi
    log_ok "All ${SKILL_COUNT} skills found in source directory"

    # 执行安装
    echo ""
    if [ "$DRY_RUN" = true ]; then
        log_info "DRY-RUN MODE — No changes will be made"
    fi
    if [ "$BACKUP" = true ]; then
        log_info "BACKUP MODE — Existing skills will be backed up"
    fi
    echo ""

    local installed=0
    local skipped=0
    for skill_name in "${SKILLS[@]}"; do
        install_skill "$skill_name"
        case "$LAST_INSTALL_ACTION" in
            installed)
                installed=$((installed + 1))
                ;;
            skipped)
                skipped=$((skipped + 1))
                ;;
        esac
    done

    echo ""
    if [ "$DRY_RUN" = true ]; then
        log_info "Dry-run complete. ${installed} skills would be installed."
        if [ $skipped -gt 0 ]; then
            log_info "${skipped} skills are already linked to source and would be skipped."
        fi
        echo ""
        echo "Run without --dry-run to perform the actual installation:"
        echo "  $0 ${TARGET_DIR}"
    else
        log_ok "Installation complete! ${installed}/${SKILL_COUNT} skills installed."
        if [ $skipped -gt 0 ]; then
            log_info "${skipped} skills were already linked to source and were skipped."
        fi
        echo ""
        echo "Next steps:"
        echo "  1. Copy templates:  cp templates/vault-profile-template.md ./my-vault-profile.md"
        echo "  2. Verify install:  ./verify-installation.sh"
        echo "  3. Read START-HERE.md for usage guidance"
        echo ""
        echo "Quick start:"
        echo "  Use \$knowledge-base-orchestrator for guided onboarding"
        echo "  Use \$knowledge-base-kit-guide to understand the structure first"
        echo "  Use \$knowledge-base-project-management only when you need project / milestone / blocker workflows"
    fi
}

main "$@"
