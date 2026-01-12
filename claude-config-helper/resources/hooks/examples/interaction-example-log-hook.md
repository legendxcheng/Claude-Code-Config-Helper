# Interaction Example: Command Logging Hook

This example shows a complete conversation flow for creating a hook that logs all bash commands executed by Claude.

---

## User Request

**User**: "I want to keep a log of all the shell commands Claude runs for auditing purposes."

---

## Conversation Flow

### Step H1: Event Type

**Claude**: "I can help you set up a command logging hook! This will record all bash commands for auditing.

What kind of automation do you want to set up?

1. **PreToolUse** - Run before a tool executes ← *Log before execution*
2. **PostToolUse** - Run after a tool completes ← *Log after execution with results*
3. Other options..."

**User**: "1 - I want to log before execution"

---

### Step H2: Storage Location

**Claude**: "Where should this hook be stored?

1. **User settings** (`~/.claude/settings.json`) - Log commands across all projects
2. **Project settings** (`.claude/settings.json`) - Only log for this project"

**User**: "1 - I want to log everything"

---

### Step H3: Matcher

**Claude**: "Which tools should trigger logging?

1. **Bash only** - Log shell commands ← *Recommended for command auditing*
2. **Multiple tools** - Log several tool types
3. **All tools** - Log everything"

**User**: "1 - just Bash commands"

---

### Step H4: Shell Command

**Claude**: "What format would you like for the log?

**Option 1: Simple log (command only)**
```bash
jq -r '.tool_input.command' >> ~/.claude/bash-log.txt
```

**Option 2: With description**
```bash
jq -r '"\(.tool_input.command) - \(.tool_input.description // \"No description\")"' >> ~/.claude/bash-log.txt
```

**Option 3: Timestamped log**
```bash
jq -r '"[\(now | strftime(\"%Y-%m-%d %H:%M:%S\"))] \(.tool_input.command)"' >> ~/.claude/bash-log.txt
```

**Option 4: JSON format (for parsing)**
```bash
jq -c '{timestamp: (now | todate), command: .tool_input.command, description: .tool_input.description}' >> ~/.claude/bash-commands.jsonl
```

Which format would you prefer?"

**User**: "Option 3 - I want timestamps"

---

### Step H5: Confirmation

**Claude**: "I'll create a hook with these settings:

- **Event**: PreToolUse (logs before execution)
- **Storage**: User settings (`~/.claude/settings.json`)
- **Matcher**: `Bash`
- **Format**: Timestamped log

Here's the configuration:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"[\\(now | strftime(\\\"%Y-%m-%d %H:%M:%S\\\"))] \\(.tool_input.command)\"' >> ~/.claude/bash-log.txt"
          }
        ]
      }
    ]
  }
}
```

Log file location: `~/.claude/bash-log.txt`

Do you want me to create this configuration?"

**User**: "Yes"

---

## File Creation

**Claude**: *Creates/updates `~/.claude/settings.json` with the configuration*

"Done! I've created the command logging hook.

**What happens now:**
- Every bash command I run will be logged with a timestamp
- Log file: `~/.claude/bash-log.txt`

**Example log entries:**
```
[2024-01-15 14:30:25] npm install
[2024-01-15 14:30:45] git status
[2024-01-15 14:31:02] npm test
```

**To verify:**
- Run `/hooks` to see your registered hooks
- Run `cat ~/.claude/bash-log.txt` to view the log

**Note:** The log file will grow over time. You may want to rotate it periodically.

Would you like to add any other hooks?"

---

## Log Rotation (Optional Follow-up)

**User**: "How do I prevent the log file from getting too large?"

**Claude**: "You can set up log rotation. Here are some options:

**Option 1: Manual rotation**
```bash
# Archive and start fresh
mv ~/.claude/bash-log.txt ~/.claude/bash-log-$(date +%Y%m%d).txt
```

**Option 2: Keep last N lines**
Add a cleanup hook that runs periodically:
```bash
tail -n 1000 ~/.claude/bash-log.txt > ~/.claude/bash-log.tmp && mv ~/.claude/bash-log.tmp ~/.claude/bash-log.txt
```

**Option 3: Use logrotate (Linux)**
Create `/etc/logrotate.d/claude-bash-log`:
```
~/.claude/bash-log.txt {
    weekly
    rotate 4
    compress
    missingok
}
```"

---

## Sample Log Output

After running several commands, `~/.claude/bash-log.txt` might contain:

```
[2024-01-15 14:30:25] npm install
[2024-01-15 14:30:45] git status
[2024-01-15 14:31:02] npm test
[2024-01-15 14:35:18] ls -la src/
[2024-01-15 14:36:44] git add .
[2024-01-15 14:36:52] git commit -m "Add new feature"
```

---

## Notes

- The hook uses `jq` to parse the JSON input and extract the command
- `now | strftime()` generates the timestamp in jq
- `>>` appends to the log file (creates if doesn't exist)
- The hook doesn't block execution (exit code 0)
- Consider JSON format if you need to analyze logs programmatically
