# Hooks Templates

This document contains ready-to-use templates for common hook configurations.

---

## Template H-A: Code Formatting Hook (PostToolUse)

**Use Case**: Automatically format code files after Claude edits them.

### TypeScript/JavaScript with Prettier

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -qE '\\.(ts|tsx|js|jsx)$'; then npx prettier --write \"$file_path\"; fi; }"
          }
        ]
      }
    ]
  }
}
```

### Go with gofmt

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -qE '\\.go$'; then gofmt -w \"$file_path\"; fi; }"
          }
        ]
      }
    ]
  }
}
```

### Python with Black

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -qE '\\.py$'; then black \"$file_path\" 2>/dev/null; fi; }"
          }
        ]
      }
    ]
  }
}
```

---

## Template H-B: File Protection Hook (PreToolUse)

**Use Case**: Block edits to sensitive files like `.env`, credentials, or lock files.

### Block Sensitive Files

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import json, sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); sys.exit(2 if any(p in path for p in ['.env', 'credentials', '.git/', 'package-lock.json', 'yarn.lock']) else 0)\""
          }
        ]
      }
    ]
  }
}
```

### Block Production Directory

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | grep -q '/prod/' && exit 2 || exit 0"
          }
        ]
      }
    ]
  }
}
```

### Block with Warning Message

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read fp; if echo \"$fp\" | grep -qE '(\\.env|secrets)'; then echo 'BLOCKED: Cannot modify sensitive file' >&2; exit 2; fi; }"
          }
        ]
      }
    ]
  }
}
```

---

## Template H-C: Command Logging Hook (PreToolUse)

**Use Case**: Log all bash commands executed by Claude for auditing or debugging.

### Simple Command Log

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> ~/.claude/bash-command-log.txt"
          }
        ]
      }
    ]
  }
}
```

### Timestamped Log

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"[\" + (now | strftime(\"%Y-%m-%d %H:%M:%S\")) + \"] \" + .tool_input.command' >> ~/.claude/bash-command-log.txt"
          }
        ]
      }
    ]
  }
}
```

### JSON Format Log

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -c '{timestamp: (now | todate), command: .tool_input.command, description: .tool_input.description}' >> ~/.claude/bash-commands.jsonl"
          }
        ]
      }
    ]
  }
}
```

---

## Template H-D: Custom Notification Hook

**Use Case**: Get custom notifications when Claude needs input or completes tasks.

### Linux (notify-send)

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' 'Awaiting your input'"
          }
        ]
      }
    ]
  }
}
```

### macOS (osascript)

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Awaiting your input\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

### Windows (PowerShell Toast)

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -Command \"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null; $template = [Windows.UI.Notifications.ToastTemplateType]::ToastText01; $xml = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent($template); $xml.GetElementsByTagName('text')[0].AppendChild($xml.CreateTextNode('Claude Code awaiting input')) | Out-Null; [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Claude Code').Show([Windows.UI.Notifications.ToastNotification]::new($xml))\""
          }
        ]
      }
    ]
  }
}
```

### Sound Alert (Cross-platform)

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo -e '\\a'"
          }
        ]
      }
    ]
  }
}
```

---

## Template H-E: Markdown Formatting Hook (PostToolUse with Script)

**Use Case**: Automatically fix markdown formatting issues and add language tags to code blocks.

### Settings Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/markdown_formatter.py\""
          }
        ]
      }
    ]
  }
}
```

### Script File: `.claude/hooks/markdown_formatter.py`

```python
#!/usr/bin/env python3
"""
Markdown formatter for Claude Code output.
Fixes missing language tags and spacing issues.
"""
import json
import sys
import re
import os

def detect_language(code):
    """Best-effort language detection from code content."""
    s = code.strip()

    # JSON detection
    if re.search(r'^\s*[{\[]', s):
        try:
            json.loads(s)
            return 'json'
        except:
            pass

    # Python detection
    if re.search(r'^\s*def\s+\w+\s*\(', s, re.M) or \
       re.search(r'^\s*(import|from)\s+\w+', s, re.M):
        return 'python'

    # JavaScript detection
    if re.search(r'\b(function\s+\w+\s*\(|const\s+\w+\s*=)', s) or \
       re.search(r'=>|console\.(log|error)', s):
        return 'javascript'

    # Bash detection
    if re.search(r'^#!.*\b(bash|sh)\b', s, re.M) or \
       re.search(r'\b(if|then|fi|for|in|do|done)\b', s):
        return 'bash'

    # SQL detection
    if re.search(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE)\s+', s, re.I):
        return 'sql'

    return 'text'

def format_markdown(content):
    """Format markdown content with language detection."""
    # Fix unlabeled code fences
    def add_lang_to_fence(match):
        indent, info, body, closing = match.groups()
        if not info.strip():
            lang = detect_language(body)
            return f"{indent}```{lang}\n{body}{closing}\n"
        return match.group(0)

    fence_pattern = r'(?ms)^([ \t]{0,3})```([^\n]*)\n(.*?)(\n\1```)\\s*$'
    content = re.sub(fence_pattern, add_lang_to_fence, content)

    # Fix excessive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.rstrip() + '\n'

# Main execution
try:
    input_data = json.load(sys.stdin)
    file_path = input_data.get('tool_input', {}).get('file_path', '')

    if not file_path.endswith(('.md', '.mdx')):
        sys.exit(0)  # Not a markdown file

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        formatted = format_markdown(content)

        if formatted != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(formatted)
            print(f"Fixed markdown formatting in {file_path}")

except Exception as e:
    print(f"Error formatting markdown: {e}", file=sys.stderr)
    sys.exit(1)
```

---

## Template H-F: Session Tracking Hook

**Use Case**: Track session start/end times for time logging.

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"Session started: $(date -Iseconds)\" >> ~/.claude/session-log.txt"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"Session ended: $(date -Iseconds)\" >> ~/.claude/session-log.txt"
          }
        ]
      }
    ]
  }
}
```

---

## Template H-G: Multiple Hooks Combined

**Use Case**: Apply multiple automations in a single configuration.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' >> ~/.claude/bash-log.txt"
          }
        ]
      },
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | grep -qE '(\\.env|secrets)' && exit 2 || exit 0"
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
            "command": "jq -r '.tool_input.file_path' | { read fp; [[ \"$fp\" == *.ts ]] && npx prettier --write \"$fp\"; exit 0; }"
          }
        ]
      }
    ],
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' 'Awaiting input'"
          }
        ]
      }
    ]
  }
}
```

---

## File Creation Process

### For New settings.json

1. **Summarize**: Show the complete configuration that will be created
2. **Preview**: Display the JSON content
3. **Confirm**: Ask user for approval
4. **Create**: Write the file to the appropriate location
5. **Verify**: Explain how to verify with `/hooks` command

### For Existing settings.json

1. **Read**: Load the existing configuration
2. **Merge**: Add new hooks while preserving existing ones
3. **Preview**: Show the merged result
4. **Confirm**: Ask user for approval
5. **Update**: Write the updated configuration
6. **Verify**: Confirm changes with `/hooks` command

### Script File Creation (if needed)

1. **Create directory**: `mkdir -p .claude/hooks/`
2. **Write script**: Create the Python/Bash script file
3. **Set permissions**: `chmod +x .claude/hooks/script_name.py`
4. **Update settings**: Add hook referencing the script
