# 环境部署指南（Environment Setup Guide）

> 本文档说明 Orchestrator 如何自动检测和部署环境。

---

## 检测流程（Detection Flow）

### 1. 检测 Obsidian（Detect Obsidian）

**目的（Purpose）**：确认用户是否已安装 Obsidian 笔记软件

**检测方法（Detection Method）**：

#### macOS
```bash
# 检查应用程序目录（check Applications folder）
if [ -d "/Applications/Obsidian.app" ]; then
    echo "已安装（installed）"
fi
```

#### Windows
```bash
# 检查常见安装路径（check common installation paths）
if exist "C:\Program Files\Obsidian\Obsidian.exe" (
    echo "已安装（installed）"
)
```

#### Linux
```bash
# 检查命令是否可用（check if command is available）
if command -v obsidian &> /dev/null; then
    echo "已安装（installed）"
fi
```

**结果处理（Result Handling）**：
- ✅ **已安装**：跳过安装步骤
- ❌ **未安装**：询问用户是否安装
- ⚠️ **其他位置**：让用户提供路径

---

### 2. 检测 Vault（Detect Vault）

**目的（Purpose）**：确认用户的笔记文件夹是否存在

**检测方法（Detection Method）**：

```bash
# 询问用户 vault 路径（ask user for vault path）
read -p "你的笔记文件夹在哪里？" vault_path

# 检查路径是否存在（check if path exists）
if [ -d "$vault_path" ]; then
    echo "✅ 文件夹存在（folder exists）"
else
    echo "❌ 文件夹不存在（folder does not exist）"
fi
```

**结果处理（Result Handling）**：
- ✅ **已存在**：检查是否有标准结构
- ❌ **不存在**：询问是否创建
- ⚠️ **存在但结构不标准**：询问是否重新组织

---

### 3. 检测 Vault Profile（Detect Vault Profile）

**目的（Purpose）**：确认知识库配置文件是否存在

**检测方法（Detection Method）**：

```bash
# 检查 profile 文件（check profile file）
if [ -f "$vault_path/vault-profile.md" ]; then
    echo "✅ profile 存在（profile exists）"
else
    echo "❌ profile 不存在（profile does not exist）"
fi
```

**结果处理（Result Handling）**：
- ✅ **已存在**：验证配置是否完整
- ❌ **不存在**：引导用户创建
- ⚠️ **存在但不完整**：提示补充缺失字段

---

## 安装流程（Installation Flow）

### 1. 安装 Obsidian（Install Obsidian）

**支持的安装方式（Supported Installation Methods）**：

#### macOS - 使用 Homebrew
```bash
# 检查 Homebrew（check Homebrew）
if ! command -v brew &> /dev/null; then
    # 安装 Homebrew（install Homebrew）
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# 安装 Obsidian（install Obsidian）
brew install --cask obsidian
```

**优点（Advantages）**：
- ✅ 自动化程度高
- ✅ 可以自动更新
- ✅ 卸载方便

**缺点（Disadvantages）**：
- ⚠️ 需要先安装 Homebrew
- ⚠️ 下载速度可能较慢

---

#### Windows - 使用 winget
```powershell
# 检查 winget（check winget）
if (Get-Command winget -ErrorAction SilentlyContinue) {
    # 安装 Obsidian（install Obsidian）
    winget install Obsidian.Obsidian
}
```

**优点（Advantages）**：
- ✅ Windows 11 自带
- ✅ 安装快速

**缺点（Disadvantages）**：
- ⚠️ Windows 10 需要手动安装 winget
- ⚠️ 部分系统可能不支持

**备选方案（Fallback）**：
- 提供下载链接：https://obsidian.md
- 引导用户手动安装

---

#### Linux - 使用 AppImage
```bash
# 下载 AppImage（download AppImage）
wget https://github.com/obsidianmd/obsidian-releases/releases/download/v1.5.3/Obsidian-1.5.3.AppImage

# 添加执行权限（add execute permission）
chmod +x Obsidian-1.5.3.AppImage

# 移动到系统目录（move to system directory）
sudo mv Obsidian-1.5.3.AppImage /usr/local/bin/obsidian
```

**优点（Advantages）**：
- ✅ 跨发行版通用
- ✅ 不需要包管理器

**缺点（Disadvantages）**：
- ⚠️ 需要手动更新
- ⚠️ 需要 sudo 权限

---

### 2. 创建 Vault 结构（Create Vault Structure）

**标准结构（Standard Structure）**：

```
my-vault/
├── index.md          # 导航首页（navigation homepage）
├── log.md            # 里程碑日志（milestone log）
├── README.md         # 说明文档（documentation）
├── vault-profile.md  # 配置文件（configuration）
├── .obsidian/        # Obsidian 配置（Obsidian config）
└── pages/            # 笔记目录（notes directory）
    ├── governance.md                  # 维护规则（governance rules）
    ├── project-learning-overview.md   # 学习笔记导航
    ├── project-work-overview.md       # 工作文档导航
    └── project-projects-overview.md   # 项目导航
```

**创建步骤（Creation Steps）**：

1. **创建主目录（Create main directory）**
   ```bash
   mkdir -p ~/Documents/my-vault
   ```

2. **创建子目录（Create subdirectories）**
   ```bash
   mkdir -p ~/Documents/my-vault/pages
   mkdir -p ~/Documents/my-vault/.obsidian
   ```

3. **创建必要文件（Create essential files）**
   - `index.md` - 导航首页
   - `log.md` - 里程碑日志
   - `README.md` - 说明文档
   - `pages/governance.md` - 维护规则

4. **创建导航页（Create navigation pages）**
   - `pages/project-learning-overview.md`
   - `pages/project-work-overview.md`
   - `pages/project-projects-overview.md`

---

### 3. 生成 Vault Profile（Generate Vault Profile）

**配置项（Configuration Items）**：

#### 必填项（Required Fields）
- **Vault name**（知识库名称）
- **Vault root path**（知识库根目录）
- **Primary markdown page directory**（笔记存放目录）
- **Reader entrypoint file**（导航首页）
- **Milestone log file**（里程碑日志）

#### 可选项（Optional Fields）
- **Maintainer entrypoint file**（维护者入口）
- **Custom areas**（自定义分类）
- **Custom naming conventions**（自定义命名规则）

**生成方式（Generation Method）**：

1. **交互式询问（Interactive Prompts）**
   ```
   Orchestrator: "你想怎么分类你的笔记？"
   用户: "learning, work, projects"
   
   Orchestrator: "你的笔记主要用于？"
   用户: "个人学习"
   ```

2. **自动生成（Auto Generation）**
   - 根据用户回答生成完整的 profile
   - 包含所有必填字段
   - 包含推荐的配置

3. **验证配置（Validate Configuration）**
   - 检查路径是否存在
   - 检查配置是否完整
   - 检查格式是否正确

---

## 错误处理（Error Handling）

### 常见错误（Common Errors）

#### 1. Homebrew 安装失败（Homebrew Installation Failed）
**原因（Cause）**：
- 网络连接问题
- 权限不足
- 系统不兼容

**解决方案（Solution）**：
```
Orchestrator：
"❌ Homebrew 安装失败

可能的原因（possible causes）：
1. 网络连接问题（network issue）
2. 权限不足（insufficient permissions）

建议（suggestions）：
1. 检查网络连接
2. 使用 VPN 或镜像源
3. 手动安装 Homebrew：https://brew.sh

要手动下载 Obsidian 吗？"
```

---

#### 2. 文件夹创建失败（Folder Creation Failed）
**原因（Cause）**：
- 路径不存在
- 权限不足
- 磁盘空间不足

**解决方案（Solution）**：
```
Orchestrator：
"❌ 文件夹创建失败

错误信息（error message）：Permission denied

可能的原因（possible causes）：
1. 权限不足（insufficient permissions）
2. 父目录不存在（parent directory does not exist）

建议（suggestions）：
1. 检查路径是否正确
2. 使用 sudo 运行（如果需要）
3. 选择其他路径

要选择其他路径吗？"
```

---

#### 3. Profile 生成失败（Profile Generation Failed）
**原因（Cause）**：
- 配置不完整
- 格式错误
- 文件写入失败

**解决方案（Solution）**：
```
Orchestrator：
"❌ Profile 生成失败

错误信息（error message）：Invalid configuration

可能的原因（possible causes）：
1. 配置不完整（incomplete configuration）
2. 格式错误（format error）

建议（suggestions）：
1. 重新回答配置问题
2. 使用默认配置
3. 手动编辑 profile

要重新配置吗？"
```

---

## 验证流程（Verification Flow）

### 1. 验证 Obsidian 安装（Verify Obsidian Installation）

```bash
# 检查 Obsidian 是否可以启动（check if Obsidian can start）
if [ -d "/Applications/Obsidian.app" ]; then
    open -a Obsidian --args --version
fi
```

**验证项（Verification Items）**：
- ✅ 应用程序存在
- ✅ 可以正常启动
- ✅ 版本号正确

---

### 2. 验证 Vault 结构（Verify Vault Structure）

```bash
# 检查必要文件是否存在（check if essential files exist）
required_files=(
    "index.md"
    "log.md"
    "README.md"
    "pages/governance.md"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$vault_path/$file" ]; then
        echo "❌ 缺少文件（missing file）: $file"
    fi
done
```

**验证项（Verification Items）**：
- ✅ 所有必要文件存在
- ✅ 文件内容正确
- ✅ 文件格式正确

---

### 3. 验证 Vault Profile（Verify Vault Profile）

```bash
# 检查 profile 是否完整（check if profile is complete）
required_fields=(
    "Vault name"
    "Vault root path"
    "Primary markdown page directory"
    "Reader entrypoint file"
    "Milestone log file"
)

# 解析 profile 文件（parse profile file）
# 检查每个必填字段（check each required field）
```

**验证项（Verification Items）**：
- ✅ 所有必填字段存在
- ✅ 路径正确
- ✅ 格式正确

---

## 总结（Summary）

Orchestrator 的环境部署流程包括：

1. **检测阶段（Detection Phase）**
   - 检测 Obsidian
   - 检测 Vault
   - 检测 Vault Profile

2. **安装阶段（Installation Phase）**
   - 安装 Obsidian
   - 创建 Vault 结构
   - 生成 Vault Profile

3. **验证阶段（Verification Phase）**
   - 验证 Obsidian 安装
   - 验证 Vault 结构
   - 验证 Vault Profile

4. **错误处理（Error Handling）**
   - 提供清晰的错误信息
   - 给出解决建议
   - 提供备选方案

所有步骤都包含中英文对照，确保用户能够理解每个术语的含义。
