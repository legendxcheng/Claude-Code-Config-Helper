# Interaction Example: File Protection Hook

This example shows a complete conversation flow for creating a file protection hook that blocks edits to sensitive files.

---

## User Request

**User**: "I want to prevent Claude from modifying my .env files and anything in the secrets folder."

---

## Conversation Flow

### Step H1: Event Type

**Claude**: "I can help you set up a file protection hook! This will block Claude from editing sensitive files.

What kind of automation do you want to set up?

1. **PreToolUse** - Run before a tool executes (can block the operation) ← *Required for blocking*
2. **PostToolUse** - Run after a tool completes
3. **Notification** - Run when Claude sends notifications
4. Other options..."

**User**: "1 - I need to block the operation"

---

### Step H2: Storage Location

**Claude**: "PreToolUse is the right choice for blocking operations.

Where should this hook be stored?

1. **User settings** (`~/.claude/settings.json`) - Block these files in all projects
2. **Project settings** (`.claude/settings.json`) - Only this project"

**User**: "1 - I want this protection everywhere"

---

### Step H3: Matcher

**Claude**: "Which tools should this protection apply to?

1. **Specific tool** - Match a single tool
2. **Multiple tools** - Match several tools ← *Recommended: Edit|Write*
3. **All tools** - Match any tool"

**User**: "2 - both Edit and Write"

**Claude**: "Please confirm: `Edit|Write`"

**User**: "Yes"

---

### Step H4: Shell Command

**Claude**: "I'll create a command that blocks access to .env files and the secrets folder.

**How blocking works:**
- Exit code `0` = Allow the operation
- Exit code `2` = Block the operation

Here's the protection command:

```bash
python3 -c "import json, sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); sys.exit(2 if any(p in path for p in ['.env', '/secrets/']) else 0)"
```

This will:
- Block any file containing `.env` in the path
- Block any file in a `secrets` directory
- Allow all other files

Would you like to add more patterns to block?"

**User**: "Also block credentials.json"

**Claude**: "Updated! I'll add `credentials.json` to the blocked patterns."

---

### Step H5: Confirmation

**Claude**: "I'll create a hook with these settings:

- **Event**: PreToolUse (can block operations)
- **Storage**: User settings (`~/.claude/settings.json`)
- **Matcher**: `Edit|Write`
- **Blocked patterns**: `.env`, `/secrets/`, `credentials.json`

Here's the configuration:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import json, sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); sys.exit(2 if any(p in path for p in ['.env', '/secrets/', 'credentials.json']) else 0)\""
          }
        ]
      }
    ]
  }
}
```

This will be saved to: `~/.claude/settings.json`

**Important**: When Claude tries to edit a blocked file, the operation will be stopped and I'll receive feedback that the file is protected.

Do you want me to create this configuration?"

**User**: "Yes"

---

## File Creation

**Claude**: *Creates/updates `~/.claude/settings.json` with the configuration*

"Done! I've created the file protection hook.

**What happens now:**
- When I try to edit `.env`, files in `secrets/`, or `credentials.json`, the operation will be blocked
- I'll receive feedback that the file is protected and cannot be modified
- All other files can be edited normally

**To verify:**
- Run `/hooks` to see your registered hooks

**To test:**
- Ask me to edit a `.env` file and I should be blocked

Would you like to add any other protections?"

---

## What Happens When Blocked

When Claude attempts to edit a protected file:

1. The PreToolUse hook runs before the edit
2. The Python script checks if the file path matches any blocked pattern
3. If matched, it exits with code 2 (block)
4. Claude receives feedback: "Hook blocked this operation"
5. Claude will explain that the file is protected and suggest alternatives

---

## Alternative: Bash-based Protection

For systems without Python, here's a bash alternative:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read fp; echo \"$fp\" | grep -qE '(\\.env|/secrets/|credentials\\.json)' && exit 2 || exit 0; }"
          }
        ]
      }
    ]
  }
}
```

---

## Notes

- PreToolUse with exit code 2 is the only way to block operations
- The hook runs for every Edit/Write operation, so keep it fast
- Blocked operations provide feedback to Claude, who can explain why
- Consider using project-level settings for project-specific protections
