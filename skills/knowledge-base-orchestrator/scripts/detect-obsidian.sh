#!/bin/bash

# 检测 Obsidian 是否已安装
# Detect if Obsidian is installed

set -e

echo "正在检测 Obsidian（黑曜石笔记软件）..."
echo "Detecting Obsidian..."

# 检测操作系统 (Detect OS)
OS="$(uname -s)"

case "${OS}" in
    Darwin*)
        # macOS
        echo "检测到系统：macOS"
        if [ -d "/Applications/Obsidian.app" ]; then
            echo "✅ Obsidian 已安装（installed）"
            echo "路径（path）: /Applications/Obsidian.app"
            exit 0
        else
            echo "❌ Obsidian 未安装（not installed）"
            exit 1
        fi
        ;;
    Linux*)
        # Linux
        echo "检测到系统：Linux"
        if command -v obsidian &> /dev/null; then
            echo "✅ Obsidian 已安装（installed）"
            echo "路径（path）: $(which obsidian)"
            exit 0
        elif [ -f "/usr/local/bin/obsidian" ]; then
            echo "✅ Obsidian 已安装（installed）"
            echo "路径（path）: /usr/local/bin/obsidian"
            exit 0
        else
            echo "❌ Obsidian 未安装（not installed）"
            exit 1
        fi
        ;;
    MINGW*|MSYS*|CYGWIN*)
        # Windows
        echo "检测到系统：Windows"
        if [ -f "/c/Program Files/Obsidian/Obsidian.exe" ]; then
            echo "✅ Obsidian 已安装（installed）"
            echo "路径（path）: C:\\Program Files\\Obsidian\\Obsidian.exe"
            exit 0
        elif [ -f "/c/Program Files (x86)/Obsidian/Obsidian.exe" ]; then
            echo "✅ Obsidian 已安装（installed）"
            echo "路径（path）: C:\\Program Files (x86)\\Obsidian\\Obsidian.exe"
            exit 0
        else
            echo "❌ Obsidian 未安装（not installed）"
            exit 1
        fi
        ;;
    *)
        echo "❌ 不支持的操作系统（unsupported OS）: ${OS}"
        exit 2
        ;;
esac
