# Stop Hook 配置实施计划

**项目**: Claude-Code-Config-Helper
**功能**: 任务完成后 Windows 11 系统通知
**日期**: 2026-01-13
**状态**: 待批准

---

## 一、配置需求总结

| 配置项 | 值 |
|--------|-----|
| Hook 事件 | Stop（Claude 响应完成时触发） |
| 存储位置 | 项目级配置文件 |
| Matcher | `""` (空字符串，适用于 Stop 事件) |
| 通知方式 | Windows Toast Notification |
| 通知文本 | "Claude Code - 任务已完成" |
| 点击行为 | 无跳转，通知消失 |

---

## 二、当前状态分析

### 现有文件
- ✅ `.claude/settings.local.json` - 存在，包含权限配置
- ❌ `.claude/settings.json` - 不存在

### 决策点：配置文件选择

**选项 A**: 创建新的 `.claude/settings.json`（推荐）
- 优点：分离 hooks 配置与权限配置
- 优点：可选择性提交到 git（团队共享）
- 缺点：新增一个配置文件

**选项 B**: 追加到现有 `.claude/settings.local.json`
- 优点：单一配置文件
- 缺点：local 文件不提交到 git（无法团队共享）
- 缺点：混合权限和 hooks 配置

**建议**: 选择 **选项 A**，理由：
1. hooks 配置是项目特定的自动化需求
2. settings.json 可以提交到 git，团队成员共享通知配置
3. settings.local.json 保留个人权限配置

---

## 三、实施检查清单

### 阶段 1: PowerShell 命令准备

- [ ] **1.1** 从模板提取 PowerShell Toast 命令
  - 源文件: `resources/hooks/templates-hooks.md:260`
  - 原始文本: `'Claude Code awaiting input'`

- [ ] **1.2** 修改通知文本
  - 目标文本: `'Claude Code - 任务已完成'`
  - 完整命令验证（确保引号转义正确）

### 阶段 2: JSON 配置构建

- [ ] **2.1** 构建 hooks JSON 结构
  ```json
  {
    "hooks": {
      "Stop": [
        {
          "matcher": "",
          "hooks": [
            {
              "type": "command",
              "command": "[PowerShell 命令]"
            }
          ]
        }
      ]
    }
  }
  ```

- [ ] **2.2** 验证 JSON 语法
  - 检查引号转义
  - 检查括号匹配
  - 检查逗号位置

### 阶段 3: 配置文件创建

- [ ] **3.1** 创建 `.claude/settings.json`
  - 路径: `E:\Claude-Code-Config-Helper\.claude\settings.json`
  - 内容: 上述 JSON 配置

- [ ] **3.2** 设置文件权限（如需要）
  - Windows 环境无需特殊权限

### 阶段 4: 验证与测试

- [ ] **4.1** 读取生成的配置文件，确认内容正确

- [ ] **4.2** 验证 JSON 格式
  - 使用 `jq` 或 Python 验证 JSON 有效性

- [ ] **4.3** 提供验证命令
  - 用户可运行 `/hooks` 命令查看配置
  - 或直接查看文件内容

- [ ] **4.4** 提供测试说明
  - 让用户执行一个简单任务（如 `ls`）
  - 观察任务完成后是否收到 Toast 通知

---

## 四、最终 JSON 配置预览

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -Command \"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null; $template = [Windows.UI.Notifications.ToastTemplateType]::ToastText01; $xml = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent($template); $xml.GetElementsByTagName('text')[0].AppendChild($xml.CreateTextNode('Claude Code - 任务已完成')) | Out-Null; [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Claude Code').Show([Windows.UI.Notifications.ToastNotification]::new($xml))\""
          }
        ]
      }
    ]
  }
}
```

---

## 五、执行顺序

```
阶段 1: PowerShell 命令准备
    ├── 1.1 提取模板命令
    └── 1.2 修改通知文本
        ↓
阶段 2: JSON 配置构建
    ├── 2.1 构建 hooks 结构
    └── 2.2 验证 JSON 语法
        ↓
阶段 3: 配置文件创建
    ├── 3.1 创建 settings.json
    └── 3.2 设置文件权限
        ↓
阶段 4: 验证与测试
    ├── 4.1 读取配置文件
    ├── 4.2 验证 JSON 格式
    ├── 4.3 提供验证命令
    └── 4.4 提供测试说明
```

---

## 六、风险与注意事项

### 风险点
1. **PowerShell 命令复杂度**
   - 长命令字符串中的引号转义容易出错
   - 缓解措施：逐步验证，使用 JSON 工具检查

2. **Windows 权限**
   - Toast 通知可能需要 Windows 通知权限
   - 缓解措施：在测试阶段提醒用户检查系统设置

3. **Stop 事件频率**
   - 每次 Claude 响应完成都会触发通知
   - 可能在短时间内收到多个通知
   - 缓解措施：在测试后根据用户反馈调整（如改用 SubagentStop）

### 注意事项
- 配置完成后，用户需重启 Claude Code 会话使配置生效
- Toast 通知点击后不会跳转到终端，用户需手动切换
- 如果不喜欢，可以随时删除此配置或修改事件类型

---

## 七、后续优化选项

如果用户在测试后发现问题，可考虑：

1. **调整事件类型**
   - 改用 `SubagentStop`（仅子任务完成时通知）
   - 减少通知频率

2. **添加声音提示**
   - 在 PowerShell 命令前添加 `[console]::beep(800,500);`
   - 双重提醒

3. **修改通知文本**
   - 更个性化的提示内容

---

## 八、批准确认

### 待确认问题

**Q1: 配置文件选择**
- ✅ 建议：创建新的 `.claude/settings.json`
- ⚠️ 替代：追加到 `.claude/settings.local.json`

请确认是否接受建议的**选项 A**？

### 批准后执行
一旦批准，将按照上述检查清单逐项执行，禁止偏离计划。

---

**等待用户批准**
