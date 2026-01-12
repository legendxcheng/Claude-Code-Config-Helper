# Technical Reference

This document contains technical details for creating Claude configuration files.

## Directory Creation

- Always check if `.claude/rules/` or `.claude/commands/` directory exists before creating files
- Create directories using: `mkdir -p .claude/rules` or `mkdir -p .claude/commands`
- Handle both Windows and Unix-style paths

## YAML Frontmatter Format (Rules)

When adding path-specific rules, use this exact format:

```yaml
---
paths:
  - "pattern1"
  - "pattern2"
---
```

- Three dashes before and after
- `paths:` with a colon
- Each pattern on a new line with `  - ` (two spaces, dash, space)
- Patterns in double quotes

## YAML Frontmatter Format (Commands)

Command files support various frontmatter options:

```yaml
---
description: Brief description shown in /help
argument-hint: [arg1] [arg2]
allowed-tools: Bash(git:*), Bash(npm:*)
model: claude-sonnet-4-20250514
context: fork
agent: general-purpose
disable-model-invocation: false
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./validate.sh"
          once: true
---
```

| Field | Required | Description |
|-------|----------|-------------|
| `description` | Recommended | Shown in /help and autocomplete |
| `argument-hint` | Optional | Shows expected arguments, e.g., `[filename]` |
| `allowed-tools` | Required for bash | Tools the command can use |
| `model` | Optional | Specific model to use |
| `context` | Optional | Set to `fork` for isolated context |
| `agent` | Optional | Agent type when using `context: fork` |
| `disable-model-invocation` | Optional | Prevent Skill tool from invoking |
| `hooks` | Optional | Define command-scoped hooks |

## Argument Placeholders

Commands can accept arguments using placeholders:

**All arguments with `$ARGUMENTS`**:
```markdown
Fix issue #$ARGUMENTS following our coding standards.
# Usage: /fix-issue 123 high-priority
# $ARGUMENTS becomes: "123 high-priority"
```

**Positional arguments with `$1`, `$2`, etc.**:
```markdown
Review PR #$1 with priority $2 and assign to $3.
# Usage: /review-pr 456 high alice
# $1="456", $2="high", $3="alice"
```

## Bash Execution Syntax

Use the `!` prefix to execute bash commands:

```markdown
## Context

- Current status: !`git status`
- Changes: !`git diff HEAD`
- Branch: !`git branch --show-current`
```

**Important**:
- Commands must be included in `allowed-tools`
- Output is included in the command context
- Use for gathering information before Claude acts

## Allowed Tools Format

Specify which tools the command can use:

```yaml
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
```

Common patterns:
- `Bash(git:*)` - All git commands
- `Bash(npm:*)` - All npm commands
- `Bash(git add:*)` - Specific git subcommand
- `Read`, `Write`, `Edit` - File operations

## File References

Use `@` prefix to include file contents:

```markdown
# Review the implementation
Review the code in @src/utils/helpers.js

# Compare files
Compare @src/old-version.js with @src/new-version.js
```

## Glob Patterns

Common patterns to suggest:
- `**/*.ts` - All TypeScript files
- `src/**/*.ts` - TypeScript files in src/
- `*.{ts,tsx}` - TypeScript and TSX files
- `{src,lib}/**/*.ts` - TypeScript files in src/ or lib/

## File Locations

**Project-level configuration files**:
- `./CLAUDE.md` - Root level (visible, good for small projects)
- `./.claude/CLAUDE.md` - Hidden directory (cleaner, good for larger projects)
- `./.claude/rules/*.md` - Modular rules (best for complex projects)
- `./CLAUDE.local.md` - Personal, not committed to git

**Command files**:
- `./.claude/commands/*.md` - Project commands (shared with team via git)
- `~/.claude/commands/*.md` - Personal commands (available across all projects)

**Command naming and namespaces**:
- File name (without .md) = command name
- Subdirectories create namespaces: `.claude/commands/frontend/build.md` → `/build (project:frontend)`
- Project commands take precedence over personal commands with same name

## Error Handling

If issues occur:

1. **Directory doesn't exist**: Create it first with `mkdir -p`
2. **File already exists**: Ask user if they want to overwrite or append
3. **Invalid glob pattern**: Explain the issue and ask for correction
4. **Unclear rules/instructions**: Ask clarifying questions before creating files
5. **Invalid frontmatter**: Validate YAML syntax before creating
6. **Missing allowed-tools**: Remind user to add if command uses bash

## Best Practices for Asking Questions

When interacting with users:

1. **One question at a time**: Don't overwhelm users with multiple questions
2. **Provide clear options**: Give numbered choices when possible
3. **Include examples**: Show examples for each option
4. **Confirm understanding**: Repeat back what you understood before creating files
5. **Be patient**: Users may not know exactly what they want - help them discover it
6. **Explain as you go**: Briefly explain why you're asking each question
