---
name: Claude Config Helper
description: Guide users through creating project-level CLAUDE.md, .claude/rules/, .claude/commands/, and hooks configuration by asking questions about their needs and generating appropriate configuration files
version: 3.0.0
---

# Claude Config Helper

## Overview

This Skill helps users create and manage project-level configuration files for Claude Code through an interactive, question-based approach. Instead of requiring users to understand the full complexity of Claude Code's memory system, this Skill guides them through a conversation to understand their needs and automatically creates the appropriate configuration files.

**Current Features (v3.0.0)**:
- Project-level rules configuration (CLAUDE.md and .claude/rules/)
- Custom slash commands configuration (.claude/commands/)
- **Hooks configuration (settings.json)** ← New in v3.0.0
- Interactive question-based workflow
- Automatic file creation based on user needs

## When to Use This Skill

Invoke this Skill when users:
- Want to create CLAUDE.md files
- Ask about configuring Claude for their project
- Need to set up project-specific rules or preferences
- Want to create file-type specific rules
- Want to create custom slash commands
- **Want to set up automation hooks**
- **Ask about auto-formatting code**
- **Want to protect sensitive files**
- **Need to log Claude's commands**
- Ask "how do I configure Claude for my project?"
- Ask "how do I create a slash command?"
- Ask "how do I create a custom command?"
- **Ask "how do I set up hooks?"**
- **Ask "how do I auto-format files?"**
- **Ask "how do I block edits to certain files?"**

## How This Skill Works

This Skill follows a 4-step interactive workflow:

1. **Ask about configuration scope**: Understand what the user wants to configure (rules, commands, or hooks)
2. **Determine file type**: Based on their needs, decide whether to create CLAUDE.md, .claude/rules/, .claude/commands/, or settings.json files
3. **Collect specific content**: Guide the user to provide the actual rules, command instructions, or hook configuration
4. **Create files**: Generate the appropriate configuration files with proper structure

## Resources

This Skill uses modular resources for detailed guidance. Access these when needed:

### `resources/question-flow.md`
**Use when**: Starting the configuration process or guiding user through questions.
Contains the complete question flow for Steps 1-4, including:
- Step 1: Determine Configuration Scope (7 options, including Hooks)
- Step 2: Determine File Type (based on user choice)
- Step 2b: Determine Command Type (for custom commands)
- Step 3: Collect Specific Rules
- Step 3b: Collect Command Details
- Step 4: Path-Specific Rules

### `resources/file-templates.md`
**Use when**: Creating configuration files after collecting user requirements.
Contains templates for all file scenarios:
- Scenario A: Global Project Rules (CLAUDE.md)
- Scenario B: Modular Rules (.claude/rules/)
- Scenario C: Multiple Files
- Scenario D: Simple Custom Command
- Scenario E: Command with Bash Execution
- Scenario F: Advanced Command
- Scenario G: Namespaced Commands
- Scenario H: Simple Hook Configuration
- Scenario I: Multiple Hooks Configuration
- Scenario J: Hook with Script File
- File Creation Process and Validation

### `resources/examples.md`
**Use when**: Needing reference for interaction patterns or showing users examples.
Contains complete example interactions:
- Example 1: Simple Build Commands
- Example 2: TypeScript-Specific Rules
- Example 3: Simple Custom Command
- Example 4: Command with Bash Execution
- Example 5: Command with Arguments
- Example 6: Code Formatting Hook
- Example 7: File Protection Hook

### `resources/technical-reference.md`
**Use when**: Needing technical details about formats, syntax, or configurations.
Contains:
- Directory Creation guidance
- YAML Frontmatter Format (Rules and Commands)
- Argument Placeholders ($ARGUMENTS, $1, $2)
- Bash Execution Syntax (!`command`)
- Allowed Tools Format
- File References (@filepath)
- Glob Patterns
- File Locations
- Error Handling
- **Hooks Configuration (JSON format, matchers, exit codes)**

### `resources/hooks/question-flow-hooks.md`
**Use when**: User wants to configure hooks (automation).
Contains the complete hooks-specific question flow:
- Step H1: Select Hook Event Type (10 types)
- Step H2: Select Storage Location (user/project)
- Step H3: Configure Matcher (tool patterns)
- Step H4: Define Shell Command
- Step H5: Confirm and Generate

### `resources/hooks/templates-hooks.md`
**Use when**: Creating hook configurations.
Contains ready-to-use hook templates:
- Template H-A: Code Formatting Hook (Prettier, gofmt, Black)
- Template H-B: File Protection Hook (block sensitive files)
- Template H-C: Command Logging Hook (audit trail)
- Template H-D: Custom Notification Hook (desktop alerts)
- Template H-E: Markdown Formatting Hook (with script)
- Template H-F: Session Tracking Hook
- Template H-G: Multiple Hooks Combined

### `resources/hooks/examples/`
**Use when**: Needing reference for hooks interaction patterns.
Contains:
- `interaction-example-format-hook.md` - Code formatting setup
- `interaction-example-protect-hook.md` - File protection setup
- `interaction-example-log-hook.md` - Command logging setup
- `generated-settings-format.json` - Example output
- `generated-settings-protect.json` - Example output

## Quick Reference

### Configuration Types

| Type | File Location | Use Case |
|------|---------------|----------|
| Global Rules | `./CLAUDE.md` | Build commands, code style, general preferences |
| Modular Rules | `./.claude/rules/*.md` | File-type specific rules with glob patterns |
| Commands | `./.claude/commands/*.md` | Reusable slash commands |
| **Hooks** | `settings.json` | Automation: formatting, protection, logging, notifications |

### Command Types

| Type | Features |
|------|----------|
| Simple | Basic prompt template |
| With Arguments | Uses $ARGUMENTS or $1, $2, etc. |
| With Bash | Executes shell commands with !`command` |
| Advanced | Hooks, specific model, forked context |

### Hook Event Types

| Event | Trigger | Capability |
|-------|---------|------------|
| PreToolUse | Before tool execution | Can block (exit 2) |
| PostToolUse | After tool completion | Post-processing |
| Notification | When notifications sent | Custom alerts |
| Stop | When response complete | Cleanup tasks |
| UserPromptSubmit | When user submits prompt | Pre-processing |
| PermissionRequest | Permission dialog shown | Allow/deny |
| SessionStart | Session begins | Initialization |
| SessionEnd | Session ends | Cleanup |
| SubagentStop | Subagent completes | Task follow-up |
| PreCompact | Before compaction | Pre-compact tasks |

### Hook Storage Locations

| Location | File Path | Scope |
|----------|-----------|-------|
| User | `~/.claude/settings.json` | All projects |
| Project | `.claude/settings.json` | Current project only |

## Error Handling

1. **Directory doesn't exist**: Create with `mkdir -p`
2. **File already exists**: Ask user to overwrite or append
3. **Invalid patterns**: Explain and ask for correction
4. **Unclear requirements**: Ask clarifying questions
5. **settings.json exists**: Merge hooks into existing config

## After File Creation

Always:
1. Confirm the file was created
2. Explain verification method:
   - Rules: `/memory` command
   - Commands: `/help` command
   - **Hooks: `/hooks` command**
3. Ask if they want to add more configuration

## Security Reminder (Hooks)

When creating hooks, remind users:
- Hooks run automatically with their environment credentials
- Review hook commands carefully before enabling
- Don't hardcode sensitive information in hook commands
- Test hooks in a safe environment first
