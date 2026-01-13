# Interaction Example: Code Formatting Hook

This example shows a complete conversation flow for creating an auto-formatting hook.

---

## User Request

**User**: "I want Claude to automatically format my TypeScript files after editing them."

---

## Conversation Flow

### Step H1: Event Type

**Claude**: "I can help you set up an auto-formatting hook! This will run automatically after Claude edits files.

What kind of automation do you want to set up?

1. **PreToolUse** - Run before a tool executes (can block the operation)
2. **PostToolUse** - Run after a tool completes (for post-processing) ← *Recommended for formatting*
3. **Notification** - Run when Claude sends notifications
4. **Stop** - Run when Claude finishes responding
5. Other options..."

**User**: "2"

---

### Step H2: Storage Location

**Claude**: "Great choice! PostToolUse is perfect for auto-formatting.

Where should this hook be stored?

1. **User settings** (`~/.claude/settings.json`) - Applies to all your projects
2. **Project settings** (`.claude/settings.json`) - Only this project"

**User**: "2 - just for this project"

---

### Step H3: Matcher

**Claude**: "Which tools should trigger this formatting hook?

1. **Specific tool** - Match a single tool
2. **Multiple tools** - Match several tools (e.g., `Edit|Write`) ← *Recommended*
3. **All tools** - Match any tool"

**User**: "2"

**Claude**: "Please specify the tool names separated by `|`:

Common tools for file operations:
- `Edit` - File editing
- `Write` - File creation/overwrite"

**User**: "Edit|Write"

---

### Step H4: Shell Command

**Claude**: "What formatting command should run? Here are some options:

**For TypeScript/JavaScript with Prettier:**
```bash
jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -qE '\\.(ts|tsx|js|jsx)$'; then npx prettier --write \"$file_path\"; fi; }
```

**For just TypeScript:**
```bash
jq -r '.tool_input.file_path' | { read fp; [[ \"$fp\" == *.ts ]] && npx prettier --write \"$fp\"; exit 0; }
```

Would you like to use one of these, or specify a custom command?"

**User**: "Use the first one for TypeScript and JavaScript"

---

### Step H5: Confirmation

**Claude**: "I'll create a hook with these settings:

- **Event**: PostToolUse
- **Storage**: Project settings (`.claude/settings.json`)
- **Matcher**: `Edit|Write`
- **Command**: Runs Prettier on .ts, .tsx, .js, .jsx files

Here's the configuration that will be created:

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

This will be saved to: `.claude/settings.json`

Do you want me to create this configuration?"

**User**: "Yes"

---

## File Creation

**Claude**: *Creates `.claude/settings.json` with the configuration*

"Done! I've created the formatting hook.

**What happens now:**
- Every time I edit or create a .ts, .tsx, .js, or .jsx file, Prettier will automatically format it
- Other file types won't be affected

**To verify:**
- Run `/hooks` to see your registered hooks
- Or check `.claude/settings.json` directly

**Prerequisites:**
- Make sure Prettier is installed: `npm install --save-dev prettier`

Would you like to add any other hooks?"

---

## Notes

- The hook uses `jq` to extract the file path from the hook input
- The grep pattern checks for TypeScript/JavaScript file extensions
- `exit 0` ensures the hook doesn't block even if formatting fails
- The hook only runs for matching file types, skipping others silently
