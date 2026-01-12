# Generated Command: Git Commit

This is an example of a command with bash execution for creating git commits.

---

## File Location

`.claude/commands/commit.md`

---

## File Contents

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

---

## Usage

```bash
# Create a commit based on current changes
/commit

# The command automatically gathers git context and creates a commit
```

---

## Key Features

### Bash Execution
The `!`command`` syntax executes bash commands before Claude processes the request:
- `!`git status`` - Shows staged/unstaged files
- `!`git diff HEAD`` - Shows all pending changes
- `!`git branch --show-current`` - Shows current branch
- `!`git log --oneline -5`` - Shows recent commits for context

### Allowed Tools
The `allowed-tools` field specifies which tools the command can use:
```yaml
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git log:*), Bash(git branch:*)
```

This allows the command to:
- Stage files with `git add`
- Check status with `git status`
- Create commits with `git commit`
- View changes with `git diff`
- View history with `git log`
- Check branch with `git branch`

---

## Customization Ideas

- Add `argument-hint: [message]` to accept a custom commit message
- Add pre-commit hooks validation
- Include branch naming convention checks
- Add support for signed commits
