# Commands Customization 功能实施计划

## 概述

为 Claude Config Helper Skill 添加 Custom Slash Commands 配置支持，使用户能够通过交互式问答创建 `.claude/commands/` 目录下的自定义命令文件。

---

## 实施检查清单

### Phase 1: 更新 Skill.md 核心文件

- [ ] **1.1** 更新 Frontmatter 元数据
  - 更新 description 包含 commands 功能
  - 更新 version 为 1.1.0

- [ ] **1.2** 更新 Overview 章节
  - 在 "Current Features" 中添加 Custom commands configuration
  - 从 "Planned Features" 中移除该项

- [ ] **1.3** 更新 "When to Use This Skill" 章节
  - 添加触发条件：用户想创建自定义斜杠命令
  - 添加触发条件：用户问 "how do I create a slash command?"

- [ ] **1.4** 更新 "How This Skill Works" 章节
  - 调整步骤描述以涵盖 commands 和 rules 两种配置类型

### Phase 2: 更新 Question Flow 章节

- [ ] **2.1** 更新 Step 1: Determine Configuration Scope
  - 添加选项 6: "Custom slash commands (reusable prompts you can invoke with /command)"
  - 更新选项说明文本

- [ ] **2.2** 新增 Step 2 分支: Commands File Type
  - 添加判断逻辑：用户选择 commands 时的处理流程
  - 询问命令类型：简单命令 vs 带 Bash 执行的命令 vs 带 hooks 的命令
  - 询问命令位置：Project (.claude/commands/) vs Personal (~/.claude/commands/)

- [ ] **2.3** 新增 Step 3 分支: Collect Command Details
  - 询问命令名称
  - 询问命令描述 (description)
  - 询问是否需要参数 (argument-hint)
  - 询问命令的具体指令内容

- [ ] **2.4** 新增 Step 4 分支: Advanced Command Options (可选)
  - 询问是否需要 Bash 命令执行
  - 询问是否需要指定允许的工具 (allowed-tools)
  - 询问是否需要指定模型 (model)
  - 询问是否使用 fork 上下文 (context: fork)

### Phase 3: 新增 Creating Files - Commands 场景

- [ ] **3.1** 添加 Scenario D: Simple Custom Command
  - 无 frontmatter 或仅有 description 的简单命令
  - 提供模板和示例

- [ ] **3.2** 添加 Scenario E: Command with Bash Execution
  - 包含 allowed-tools 和 `!` 语法的命令
  - 提供模板和示例

- [ ] **3.3** 添加 Scenario F: Command with Full Configuration
  - 包含完整 frontmatter（allowed-tools, argument-hint, description, model, hooks 等）
  - 提供模板和示例

- [ ] **3.4** 添加 Scenario G: Namespaced Commands
  - 使用子目录组织相关命令
  - 说明命名空间显示规则

### Phase 4: 新增 Example Interactions

- [ ] **4.1** 添加 Example 3: Simple Command Creation
  - 展示创建简单代码审查命令的完整对话流程

- [ ] **4.2** 添加 Example 4: Command with Bash and Arguments
  - 展示创建带 Git 操作的 commit 命令

- [ ] **4.3** 添加 Example 5: Multiple Commands Setup
  - 展示一次配置多个相关命令的场景

### Phase 5: 更新 Technical Notes

- [ ] **5.1** 添加 Command File Structure 说明
  - Frontmatter 格式详解
  - 各字段用途和语法

- [ ] **5.2** 添加 Argument Placeholders 说明
  - `$ARGUMENTS` 用法
  - `$1`, `$2` 位置参数用法

- [ ] **5.3** 添加 Bash Execution 说明
  - `!` 前缀语法
  - allowed-tools 配置格式
  - 安全注意事项

- [ ] **5.4** 添加 File References 说明
  - `@` 前缀语法
  - 相对路径和绝对路径

- [ ] **5.5** 添加 Command Locations 说明
  - `.claude/commands/` - 项目级命令
  - `~/.claude/commands/` - 个人级命令
  - 命名空间和优先级规则

### Phase 6: 创建示例资源文件

- [ ] **6.1** 创建目录结构
  - 创建 `resources/commands/examples/` 目录

- [ ] **6.2** 创建 interaction-example-simple-command.md
  - 简单命令的完整交互示例

- [ ] **6.3** 创建 interaction-example-bash-command.md
  - 带 Bash 执行的命令交互示例

- [ ] **6.4** 创建 generated-command-review.md
  - 生成的简单代码审查命令示例

- [ ] **6.5** 创建 generated-command-commit.md
  - 生成的带 Bash 的 git commit 命令示例

- [ ] **6.6** 创建 generated-command-deploy.md
  - 生成的带 hooks 的部署命令示例

### Phase 7: 更新项目文档

- [ ] **7.1** 更新 README.md
  - 添加 Commands 配置功能说明
  - 更新功能列表
  - 添加 Commands 使用示例

### Phase 8: 验证和测试

- [ ] **8.1** 验证 Skill.md 语法正确性
  - YAML frontmatter 格式
  - Markdown 结构完整性

- [ ] **8.2** 验证示例文件
  - 所有生成的命令文件格式正确
  - 交互示例逻辑清晰

---

## 文件变更清单

| 文件路径 | 操作 |
|---------|------|
| `claude-config-helper/Skill.md` | 修改 |
| `claude-config-helper/resources/commands/examples/interaction-example-simple-command.md` | 新增 |
| `claude-config-helper/resources/commands/examples/interaction-example-bash-command.md` | 新增 |
| `claude-config-helper/resources/commands/examples/generated-command-review.md` | 新增 |
| `claude-config-helper/resources/commands/examples/generated-command-commit.md` | 新增 |
| `claude-config-helper/resources/commands/examples/generated-command-deploy.md` | 新增 |
| `README.md` | 修改 |

---

## 关键设计决策

### 1. Question Flow 设计

保持与现有 rules 配置相似的 4 步流程：
1. 确定配置范围 → 用户选择 commands
2. 确定命令类型 → 简单/带Bash/带hooks
3. 收集命令详情 → 名称、描述、参数、内容
4. 高级选项（可选）→ 工具、模型、上下文

### 2. 命令复杂度分级

| 级别 | 特征 | 适用场景 |
|-----|------|---------|
| 简单 | 仅 description + 内容 | 常用提示模板 |
| 中等 | + argument-hint + allowed-tools | 带参数的命令 |
| 高级 | + hooks + context + model | 复杂工作流 |

### 3. 与现有 Rules 功能的整合

- 共用 Step 1 的配置范围选择
- 根据用户选择分流到不同的处理路径
- 保持一致的交互风格和确认流程

---

## 预估工作量

| Phase | 复杂度 |
|-------|--------|
| Phase 1: 更新元数据和概述 | 低 |
| Phase 2: 更新 Question Flow | 中 |
| Phase 3: 新增 Creating Files 场景 | 中 |
| Phase 4: 新增 Example Interactions | 中 |
| Phase 5: 更新 Technical Notes | 中 |
| Phase 6: 创建示例资源文件 | 低 |
| Phase 7: 更新 README | 低 |
| Phase 8: 验证测试 | 低 |
