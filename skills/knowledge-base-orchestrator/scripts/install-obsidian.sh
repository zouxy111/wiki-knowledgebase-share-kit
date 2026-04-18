#!/bin/bash

# 自动安装 Obsidian
# Auto install Obsidian

set -e

# 日志函数
log_warn() { echo "⚠️  $1"; }
log_info() { echo "ℹ️  $1"; }

echo "=========================================="
echo "📦 正在安装 Obsidian（黑曜石笔记软件）"
echo "   此脚本将下载并安装 Obsidian 到您的系统"
echo "   This script will download and install Obsidian"
echo "=========================================="

# 检测操作系统 (Detect OS)
OS="$(uname -s)"

case "${OS}" in
    Darwin*)
        # macOS
        echo "检测到系统：macOS"
        echo ""

        # 检查 Homebrew 是否安装 (Check if Homebrew is installed)
        if ! command -v brew &> /dev/null; then
            echo "❌ 未检测到 Homebrew（包管理器，package manager）"
            echo "正在安装 Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            echo "✅ Homebrew 安装完成"
            echo ""
        else
            echo "✅ Homebrew 已安装"
            echo ""
        fi

        # 安装 Obsidian (Install Obsidian)
        echo "正在通过 Homebrew 安装 Obsidian..."
        brew install --cask obsidian

        echo ""
        echo "✅ Obsidian 安装完成！"
        echo "路径（path）: /Applications/Obsidian.app"
        ;;

    Linux*)
        # Linux
        echo "检测到系统：Linux"
        echo ""

        # 获取最新版本 (Get latest version)
        echo "正在获取最新版本信息..."
        OBSIDIAN_VERSION=$(curl -s https://api.github.com/repos/obsidianmd/obsidian-releases/releases/latest | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tag_name','').lstrip('v'))" 2>/dev/null || echo "")
        if [ -z "$OBSIDIAN_VERSION" ]; then
            log_warn "无法获取最新版本，使用 fallback 版本 1.8.10"
            OBSIDIAN_VERSION="1.8.10"
        fi
        DOWNLOAD_URL="https://github.com/obsidianmd/obsidian-releases/releases/download/v${OBSIDIAN_VERSION}/Obsidian-${OBSIDIAN_VERSION}.AppImage"

        echo "正在下载 Obsidian ${OBSIDIAN_VERSION}..."
        wget -O /tmp/Obsidian.AppImage "${DOWNLOAD_URL}"

        # 添加执行权限 (Add execute permission)
        chmod +x /tmp/Obsidian.AppImage

        # 安装到用户目录或系统目录 (Install to user or system directory)
        INSTALL_DIR="${HOME}/.local/bin"
        if [ -d "$INSTALL_DIR" ]; then
            echo "正在安装到用户目录: ${INSTALL_DIR}"
            mv /tmp/Obsidian.AppImage "${INSTALL_DIR}/obsidian"
        else
            echo "正在安装到系统目录: /usr/local/bin"
            sudo mv /tmp/Obsidian.AppImage /usr/local/bin/obsidian
        fi

        echo ""
        echo "✅ Obsidian 安装完成！"
        echo "路径（path）: /usr/local/bin/obsidian"
        echo ""
        echo "运行命令（run command）: obsidian"
        ;;

    MINGW*|MSYS*|CYGWIN*)
        # Windows
        echo "检测到系统：Windows"
        echo ""

        # 检查 winget 是否可用 (Check if winget is available)
        if command -v winget &> /dev/null; then
            echo "正在通过 winget 安装 Obsidian..."
            winget install Obsidian.Obsidian

            echo ""
            echo "✅ Obsidian 安装完成！"
            echo "路径（path）: C:\\Program Files\\Obsidian\\Obsidian.exe"
        else
            echo "❌ 未检测到 winget（包管理器，package manager）"
            echo ""
            echo "请手动下载安装："
            echo "1. 访问（visit）: https://obsidian.md"
            echo "2. 点击 Download（下载）"
            echo "3. 运行安装程序（run installer）"
            exit 1
        fi
        ;;

    *)
        echo "❌ 不支持的操作系统（unsupported OS）: ${OS}"
        echo ""
        echo "请手动下载安装："
        echo "访问（visit）: https://obsidian.md"
        exit 2
        ;;
esac

echo ""
echo "🎉 安装完成！现在可以使用 Obsidian 了。"
echo "Installation complete! You can now use Obsidian."
