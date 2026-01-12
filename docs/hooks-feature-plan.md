# Hooks 配置功能实施计划

**版本**: v3.0.0
**日期**: 2026-01-12
**状态**: 待批准

---

## 一、功能概述

为 Claude Config Helper Skill 添加 Hooks 配置功能，帮助用户通过交互式问答创建和管理 Claude Code 的 hooks 配置。

### 目标
- 引导用户理解 10 种 Hook 事件类型
- 通过问答收集用户需求
- 自动生成正确的 `settings.json` 配置
- 提供常见 hooks 模板（格式化、保护、日志、通知）

### 与现有功能的关系
| 现有功能 | 新增功能 |
|----------|----------|
| Rules (.md) | Hooks (.json) |
| Commands (.md) | - |
| 文件创建 | JSON 配置生成 |

---

## 二、实施检查清单

### Phase 1: 核心资源文件创建

- [ ] **1.1** 创建 `resources/hooks/` 目录结构
- [ ] **1.2** 创建 `resources/hooks/question-flow-hooks.md` - Hooks 专用问卷流程
  - Step H1: 选择 Hook 事件类型（10种）
  - Step H2: 选择存储位置（用户级/项目级）
  - Step H3: 配置 Matcher（工具名/模式）
  - Step H4: 编写 Shell 命令
  - Step H5: 确认并生成
- [ ] **1.3** 创建 `resources/hooks/templates-hooks.md` - Hooks 模板集合
  - Template H-A: 代码格式化 Hook (PostToolUse)
  - Template H-B: 文件保护 Hook (PreToolUse)
  - Template H-C: 命令日志 Hook (PreToolUse + Bash)
  - Template H-D: 自定义通知 Hook (Notification)
  - Template H-E: Markdown 格式化 Hook (PostToolUse + Python脚本)

### Phase 2: 示例文件创建

- [ ] **2.1** 创建 `resources/hooks/examples/` 目录
- [ ] **2.2** 创建 `resources/hooks/examples/interaction-example-format-hook.md`
  - 完整的 TypeScript 格式化 hook 交互示例
- [ ] **2.3** 创建 `resources/hooks/examples/interaction-example-protect-hook.md`
  - 完整的文件保护 hook 交互示例
- [ ] **2.4** 创建 `resources/hooks/examples/interaction-example-log-hook.md`
  - 完整的命令日志 hook 交互示例
- [ ] **2.5** 创建 `resources/hooks/examples/generated-settings-format.json`
  - 生成的格式化配置示例
- [ ] **2.6** 创建 `resources/hooks/examples/generated-settings-protect.json`
  - 生成的文件保护配置示例

### Phase 3: 现有文件更新

- [ ] **3.1** 更新 `Skill.md`
  - 版本号: 2.0.0 → 3.0.0
  - description: 添加 "hooks configuration"
  - Overview: 添加 Hooks 功能说明
  - "When to Use": 添加 hooks 相关触发条件
  - "How This Skill Works": 更新工作流程
  - Resources: 添加 hooks 资源引用
  - Quick Reference: 添加 Hooks 配置类型表格

- [ ] **3.2** 更新 `resources/question-flow.md`
  - Step 1: 添加第 7 个选项 "7. Hooks (自动化钩子)"
  - 添加 Step 1 → Hooks 分支的跳转说明

- [ ] **3.3** 更新 `resources/file-templates.md`
  - 添加 Scenario H: 简单 Hook 配置
  - 添加 Scenario I: 多 Hook 配置
  - 添加 Scenario J: 带脚本的 Hook 配置

- [ ] **3.4** 更新 `resources/technical-reference.md`
  - 添加 "Hooks Configuration" 章节
  - JSON 格式说明
  - Matcher 语法 (ToolName, Pattern, *)
  - Exit Codes (0=允许, 2=阻止)
  - 环境变量 ($CLAUDE_PROJECT_DIR 等)
  - 常用工具名列表 (Bash, Edit, Write, Read, Glob, Grep)

- [ ] **3.5** 更新 `resources/examples.md`
  - 添加 Example 6: 简单格式化 Hook
  - 添加 Example 7: 文件保护 Hook

### Phase 4: 验证与文档

- [ ] **4.1** 验证所有资源文件引用路径正确
- [ ] **4.2** 确保 Skill.md 中的资源描述与实际内容一致
- [ ] **4.3** 检查 JSON 示例格式正确性

---

## 三、文件变更清单

### 新增文件 (8个)
```
resources/hooks/
├── question-flow-hooks.md           # 新增
├── templates-hooks.md               # 新增
└── examples/
    ├── interaction-example-format-hook.md    # 新增
    ├── interaction-example-protect-hook.md   # 新增
    ├── interaction-example-log-hook.md       # 新增
    ├── generated-settings-format.json        # 新增
    └── generated-settings-protect.json       # 新增
```

### 修改文件 (5个)
```
Skill.md                             # 修改
resources/question-flow.md           # 修改
resources/file-templates.md          # 修改
resources/technical-reference.md     # 修改
resources/examples.md                # 修改
```

---

## 四、关键设计决策

### 4.1 问卷流程设计

```
Step 1: 配置范围
├── 1-6: 现有选项 (rules/commands)
└── 7: Hooks → 跳转到 Hooks 专用流程

Hooks 专用流程:
Step H1: 选择事件类型
    ├── PreToolUse (工具调用前，可阻止)
    ├── PostToolUse (工具调用后)
    ├── Notification (通知时)
    ├── Stop (响应完成时)
    └── 其他 6 种...

Step H2: 存储位置
    ├── 用户级 (~/.claude/settings.json)
    └── 项目级 (.claude/settings.json)

Step H3: Matcher 配置
    ├── 特定工具 (Bash, Edit, Write...)
    ├── 多工具模式 (Edit|Write)
    └── 所有工具 (*)

Step H4: Shell 命令
    ├── 简单命令 (单行)
    ├── 管道命令 (jq处理)
    └── 脚本调用 (Python/Bash脚本)

Step H5: 生成配置
```

### 4.2 配置生成策略

**新配置** (settings.json 不存在或无 hooks):
```json
{
  "hooks": {
    "EventType": [...]
  }
}
```

**追加配置** (已有 hooks):
- 读取现有配置
- 合并新的 hook
- 提示用户确认

### 4.3 常用模板

| 模板 | 事件 | Matcher | 用途 |
|------|------|---------|------|
| 格式化 | PostToolUse | Edit\|Write | 自动运行 prettier/gofmt |
| 保护 | PreToolUse | Edit\|Write | 阻止敏感文件修改 |
| 日志 | PreToolUse | Bash | 记录所有命令 |
| 通知 | Notification | * | 桌面通知 |

---

## 五、技术规格

### 5.1 settings.json 结构
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' >> ~/.claude/log.txt"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write \"$(jq -r '.tool_input.file_path')\""
          }
        ]
      }
    ]
  }
}
```

### 5.2 Matcher 语法
- 单工具: `Bash`, `Edit`, `Write`, `Read`
- 多工具: `Edit|Write`, `Bash|Read`
- 全部: `*` 或空字符串 `""`

### 5.3 Exit Codes
- `0` - 允许操作继续
- `2` - 阻止操作（仅 PreToolUse）
- 其他 - 视为错误但不阻止

### 5.4 可用环境变量
- `$CLAUDE_PROJECT_DIR` - 项目目录
- stdin 接收 JSON 格式的 hook 数据

---

## 六、执行顺序

```
Phase 1 (核心资源) ──┬── 1.1 创建目录
                    ├── 1.2 question-flow-hooks.md
                    └── 1.3 templates-hooks.md
                           │
Phase 2 (示例文件) ──┬── 2.1 创建 examples 目录
                    ├── 2.2-2.4 交互示例
                    └── 2.5-2.6 生成配置示例
                           │
Phase 3 (更新现有) ──┬── 3.1 Skill.md
                    ├── 3.2 question-flow.md
                    ├── 3.3 file-templates.md
                    ├── 3.4 technical-reference.md
                    └── 3.5 examples.md
                           │
Phase 4 (验证) ─────┬── 4.1-4.3 验证与检查
```

---

## 七、风险与注意事项

1. **JSON 格式敏感**: hooks 配置为 JSON，需确保生成的配置语法正确
2. **安全提醒**: 需在文档中强调 hooks 安全风险（自动执行命令）
3. **兼容性**: 需处理已有 settings.json 的情况（追加 vs 覆盖）
4. **跨平台**: Shell 命令需考虑 Windows/Linux/macOS 差异

---

**等待批准后进入执行模式**
