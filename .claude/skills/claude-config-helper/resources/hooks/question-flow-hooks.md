# Hooks Question Flow

This document defines the interactive question flow for configuring Claude Code hooks.

---

## Step H1: Select Hook Event Type

**Question**: "What kind of automation do you want to set up?"

Present these options:

| Option | Event Type | Description |
|--------|------------|-------------|
| 1 | PreToolUse | Run before a tool executes (can block the operation) |
| 2 | PostToolUse | Run after a tool completes (for post-processing) |
| 3 | Notification | Run when Claude sends notifications |
| 4 | Stop | Run when Claude finishes responding |
| 5 | UserPromptSubmit | Run when user submits a prompt |
| 6 | PermissionRequest | Run when permission dialog appears |
| 7 | SessionStart | Run when a session begins |
| 8 | SessionEnd | Run when a session ends |
| 9 | SubagentStop | Run when a subagent task completes |
| 10 | PreCompact | Run before context compaction |

**Common Use Cases by Event**:
- **PreToolUse**: Block edits to sensitive files, validate commands before execution
- **PostToolUse**: Auto-format code after edits, run linters, update logs
- **Notification**: Custom desktop notifications, Slack/Discord alerts
- **Stop**: Generate summaries, update task trackers

---

## Step H2: Select Storage Location

**Question**: "Where should this hook be stored?"

| Option | Location | Scope |
|--------|----------|-------|
| 1 | User settings (`~/.claude/settings.json`) | Applies to all projects |
| 2 | Project settings (`.claude/settings.json`) | Only this project |

**Guidance**:
- Choose **User settings** for personal preferences (notifications, logging)
- Choose **Project settings** for project-specific automation (formatting, protection)

---

## Step H3: Configure Matcher

**Question**: "Which tools should trigger this hook?"

Based on the event type selected in Step H1:

### For PreToolUse / PostToolUse / PermissionRequest:

| Option | Matcher | Description |
|--------|---------|-------------|
| 1 | Specific tool | Match a single tool (e.g., `Bash`, `Edit`, `Write`) |
| 2 | Multiple tools | Match several tools (e.g., `Edit|Write`) |
| 3 | All tools | Match any tool (`*`) |

**Common Tool Names**:
- `Bash` - Shell command execution
- `Edit` - File editing
- `Write` - File creation/overwrite
- `Read` - File reading
- `Glob` - File pattern matching
- `Grep` - Content searching
- `Task` - Subagent tasks
- `WebFetch` - Web requests

### For Other Events (Notification, Stop, etc.):

Matcher is typically empty (`""`) or `*` to match all occurrences.

**Follow-up if Option 1 or 2 selected**:
"Please specify the tool name(s). For multiple tools, separate with `|` (e.g., `Edit|Write`):"

---

## Step H4: Define Shell Command

**Question**: "What command should run when this hook triggers?"

### Input Format Options:

| Type | Description | Example |
|------|-------------|---------|
| Simple | Single command | `notify-send 'Claude' 'Task done'` |
| With jq | Process hook input JSON | `jq -r '.tool_input.command' >> log.txt` |
| Script | Call external script | `python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/format.py"` |

### Hook Input Data (via stdin):

For **PreToolUse** and **PostToolUse**, the hook receives JSON:
```json
{
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "/path/to/file.ts",
    "old_string": "...",
    "new_string": "..."
  }
}
```

For **Bash** tool specifically:
```json
{
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test",
    "description": "Run tests"
  }
}
```

### Common Command Patterns:

**1. Extract file path and process**:
```bash
jq -r '.tool_input.file_path' | { read fp; npx prettier --write "$fp"; }
```

**2. Log commands**:
```bash
jq -r '"Command: \(.tool_input.command)"' >> ~/.claude/command-log.txt
```

**3. Block based on condition (exit 2 to block)**:
```bash
jq -r '.tool_input.file_path' | grep -q '\.env' && exit 2 || exit 0
```

**4. Call Python script**:
```bash
python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/my_hook.py"
```

---

## Step H5: Confirm and Generate

**Summary Template**:

```
I'll create a hook with these settings:

- Event: [Event Type]
- Storage: [User/Project] settings
- Matcher: [Matcher Pattern]
- Command: [Shell Command]

This will be added to: [file path]
```

**If settings.json doesn't exist**:
```
The settings file doesn't exist yet. I'll create it with this hook configuration.
```

**If settings.json exists but has no hooks**:
```
I'll add a hooks section to your existing settings.
```

**If settings.json already has hooks**:
```
I'll add this hook to your existing hooks configuration.
Do you want to:
1. Add as a new hook (recommended)
2. Replace existing hooks for this event type
```

---

## Decision Tree Summary

```
User selects "Hooks" from main menu (option 7)
    │
    ▼
Step H1: Select Event Type
    │ (1-10 options)
    ▼
Step H2: Select Storage Location
    │ (User or Project)
    ▼
Step H3: Configure Matcher
    │ (Tool name, pattern, or *)
    ▼
Step H4: Define Shell Command
    │ (Simple, jq, or script)
    ▼
Step H5: Confirm and Generate
    │
    ▼
Create/Update settings.json
```

---

## Additional Questions (Context-Dependent)

### If user selects PreToolUse with blocking intent:

**Question**: "Do you want this hook to block the operation under certain conditions?"

- If yes: "Remember to use `exit 2` in your command to block. Other exit codes allow the operation."

### If user needs a script file:

**Question**: "Do you need to create a hook script file?"

- If yes: Guide through creating `.claude/hooks/` directory and script file
- Provide script template based on event type

### If user is unsure about command:

**Question**: "What do you want to achieve with this hook?"

Common answers and suggested commands:
| Goal | Suggested Command |
|------|-------------------|
| Format TypeScript files | `jq -r '.tool_input.file_path' \| { read f; [[ "$f" == *.ts ]] && npx prettier --write "$f"; }` |
| Block .env file edits | `jq -r '.tool_input.file_path' \| grep -q '\.env' && exit 2` |
| Log all bash commands | `jq -r '.tool_input.command' >> ~/.claude/bash-log.txt` |
| Desktop notification | `notify-send 'Claude Code' 'Awaiting input'` |
