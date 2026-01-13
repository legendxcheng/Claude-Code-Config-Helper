# Example Interaction: Creating a Command with Bash Execution

This example shows creating a git commit command that gathers context from git commands before creating a commit.

---

## Conversation Flow

**User**: "I need a command to help with git commits"

**Claude**: "I'll help you create a custom slash command for git commits. What would you like to configure?

1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions
6. Custom slash commands (reusable prompts you can invoke with /command-name)

Please tell me the number(s) or describe what you'd like to configure."

**User**: "6 - custom command"

**Claude**: "What would you like to name this command?"

**User**: "commit"

**Claude**: "What type of command would you like to create?

1. Simple command - A reusable prompt template
2. Command with arguments - Accepts parameters when invoked
3. Command with bash execution - Runs shell commands and uses their output
4. Advanced command - Includes hooks, specific model, or forked context"

**User**: "3 - I want it to show git status and diff first"

**Claude**: "Should this command be project-specific or personal?"

**User**: "project"

**Claude**: "Please provide a brief description for this command."

**User**: "Create a well-formatted git commit"

**Claude**: "What bash commands should be executed to gather context? Common git commands include:
- `git status` - Show current status
- `git diff HEAD` - Show all pending changes
- `git diff --staged` - Show only staged changes
- `git log --oneline -10` - Recent commits
- `git branch --show-current` - Current branch name"

**User**: "git status, git diff HEAD, git branch --show-current, and git log --oneline -5"

**Claude**: "What instructions should Claude follow after seeing the git context? What commit message format do you prefer?"

**User**: "Follow conventional commits format. If changes are too big, suggest splitting them. Always write clear commit messages."

**Claude**: "I'll create the following file:

**File**: ./.claude/commands/commit.md

**Contents**:
```markdown
---
description: Create a well-formatted git commit
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git log:*), Bash(git branch:*)
---

## Current Git Context

- **Status**: !`git status`
- **Pending Changes**: !`git diff HEAD`
- **Current Branch**: !`git branch --show-current`
- **Recent Commits**: !`git log --oneline -5`

## Your Task

Based on the git context above, help create a well-formatted commit.

### Guidelines

1. **Analyze the changes** - Understand what was modified and why
2. **Check scope** - If changes are too large or unrelated, suggest splitting into multiple commits
3. **Write commit message** using conventional commits format:
   ```
   type(scope): description

   [optional body]

   [optional footer]
   ```

   Types: feat, fix, docs, style, refactor, perf, test, build, ci, chore

4. **Stage files** if needed using `git add`
5. **Create the commit** with the generated message

### Quality Checks

- Commit message should be clear and descriptive
- First line should be under 72 characters
- Body should explain "why" not just "what"
- Reference issue numbers if applicable
```

Does this look good? Should I create this file?"

**User**: "yes"

**Claude**: [Creates file]

"✓ Created ./.claude/commands/commit.md

You can now use `/commit` to create well-formatted git commits. When invoked, the command will:
1. Show you the current git status and changes
2. Analyze what was modified
3. Generate an appropriate commit message
4. Create the commit

The command has permission to run git commands (add, status, commit, diff, log, branch). Would you like to create any other commands?"

---

## Generated File

See `generated-command-commit.md` for the complete generated command file.
