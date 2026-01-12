# File Templates

This document contains templates for creating various configuration files.

## Scenario A: Global Project Rules (CLAUDE.md)

When creating a CLAUDE.md file:

1. **Choose location**: Use the location the user specified (root or .claude/)
2. **Structure the content**:
   - Add a clear heading describing the configuration category
   - Format user's rules as bullet points
   - Group related rules under appropriate headings
   - Use clear, concise language

**Template**:
```markdown
# Project Configuration for Claude

## [Category Name]

- [Rule 1]
- [Rule 2]
- [Rule 3]

## [Another Category if applicable]

- [Rule 4]
- [Rule 5]
```

**Example**:
```markdown
# Project Configuration for Claude

## Build and Test Commands

- Always use `npm run build` to build the project
- Run tests with `npm test` before committing
- Use `npm run lint` to check code style

## Code Style

- Use 2-space indentation for all files
- Use single quotes for strings in JavaScript/TypeScript
- Add trailing commas in multi-line objects and arrays
```

## Scenario B: Modular Rules (.claude/rules/)

When creating a modular rule file:

1. **Create directory**: If `.claude/rules/` doesn't exist, create it first
2. **Create the rule file**: Use the name the user specified (e.g., `typescript-rules.md`)
3. **Structure the content**:
   - If path-specific: Add YAML frontmatter with `paths` field
   - Add a clear heading
   - Format rules as bullet points
   - Be specific and actionable

**Template (without path restriction)**:
```markdown
# [Rule Category Name]

- [Rule 1]
- [Rule 2]
- [Rule 3]
```

**Template (with path restriction)**:
```markdown
---
paths:
  - "[glob pattern 1]"
  - "[glob pattern 2]"
---

# [Rule Category Name]

- [Rule 1]
- [Rule 2]
- [Rule 3]
```

**Example (TypeScript-specific rules)**:
```markdown
---
paths:
  - "src/**/*.ts"
  - "src/**/*.tsx"
---

# TypeScript Code Standards

- Use explicit return types for all functions
- Prefer interfaces over type aliases for object shapes
- Use strict null checks
- Avoid using `any` type - use `unknown` if type is truly unknown
```

## Scenario C: Multiple Files

If the user wants to configure multiple categories:

1. Create CLAUDE.md for global rules
2. Create separate files in `.claude/rules/` for specific categories
3. Explain the structure to the user after creation

## Scenario D: Simple Custom Command

When creating a simple custom command (no bash execution):

1. **Create directory**: If `.claude/commands/` doesn't exist, create it first
2. **Create the command file**: Use the name the user specified (e.g., `review.md`)
3. **Structure the content**:
   - Add YAML frontmatter with `description` field
   - Optionally add `argument-hint` if command accepts arguments
   - Add clear instructions for Claude

**Template (simple command)**:
```markdown
---
description: [Brief description of the command]
---

[Instructions for Claude when this command is invoked]
```

**Template (command with arguments)**:
```markdown
---
description: [Brief description of the command]
argument-hint: [argument placeholders]
---

[Instructions using $ARGUMENTS or $1, $2, etc.]
```

**Example (code review command)**:
```markdown
---
description: Review code for bugs, security issues, and best practices
---

Review the provided code for:
- Security vulnerabilities (injection, XSS, etc.)
- Performance issues
- Code style violations
- Potential bugs or edge cases

Provide specific suggestions for each issue found with code examples.
```

**Example (fix issue command with arguments)**:
```markdown
---
description: Fix a GitHub issue by number
argument-hint: [issue-number]
---

Fix issue #$ARGUMENTS following our coding standards.

1. First, understand the issue by reading its description
2. Identify the relevant files that need to be modified
3. Implement the fix
4. Write tests if applicable
5. Summarize the changes made
```

## Scenario E: Command with Bash Execution

When creating a command that executes bash commands:

1. **Create directory**: If `.claude/commands/` doesn't exist, create it first
2. **Create the command file**: Use the name the user specified
3. **Structure the content**:
   - Add YAML frontmatter with `description` and `allowed-tools`
   - Use `!`command`` syntax to execute bash commands
   - The output of bash commands will be available to Claude

**Template**:
```markdown
---
description: [Brief description of the command]
allowed-tools: Bash([command1]:*), Bash([command2]:*)
---

## Context

- [Context item]: !`[bash command]`
- [Another context]: !`[another command]`

## Your Task

[Instructions for what Claude should do with the context]
```

**Example (git commit command)**:
```markdown
---
description: Create a git commit with a well-formatted message
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git log:*)
argument-hint: [message]
---

## Context

- Current git status: !`git status`
- Staged and unstaged changes: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your Task

Based on the above changes, create a single git commit.

If a message was provided ($ARGUMENTS), use it as the commit message.
Otherwise, generate an appropriate commit message based on the changes.

Follow conventional commit format: type(scope): description
```

## Scenario F: Advanced Command

When creating a command with advanced features (hooks, specific model, forked context):

1. **Create directory**: If `.claude/commands/` doesn't exist, create it first
2. **Create the command file**: Use the name the user specified
3. **Structure the content**:
   - Add comprehensive YAML frontmatter
   - Include all required advanced options

**Template (with all options)**:
```markdown
---
description: [Brief description]
allowed-tools: [Tool list]
argument-hint: [Arguments]
model: [Model name, e.g., claude-sonnet-4-20250514]
context: fork
agent: [Agent type, e.g., general-purpose]
hooks:
  PreToolUse:
    - matcher: "[Tool name]"
      hooks:
        - type: command
          command: "[validation script]"
          once: true
---

[Command instructions]
```

**Example (deploy command with validation)**:
```markdown
---
description: Deploy to staging with pre-flight validation
allowed-tools: Bash(npm:*), Bash(git:*), Bash(docker:*)
context: fork
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-deploy.sh"
          once: true
---

## Pre-deployment Checks

- Current branch: !`git branch --show-current`
- Uncommitted changes: !`git status --porcelain`
- Test results: !`npm test`

## Deployment Steps

1. Ensure all tests pass
2. Build the application: `npm run build`
3. Deploy to staging environment
4. Verify deployment health
5. Report deployment status

Only proceed with deployment if all pre-flight checks pass.
```

## Scenario G: Namespaced Commands

When organizing related commands in subdirectories:

1. **Create subdirectory**: Create `.claude/commands/[namespace]/`
2. **Create command files**: Place related commands in the subdirectory
3. **Explain the naming**: Commands will show as "(project:[namespace])" in /help

**Example structure**:
```
.claude/commands/
├── review.md                    # /review (project)
├── frontend/
│   ├── component.md             # /component (project:frontend)
│   └── test-ui.md               # /test-ui (project:frontend)
└── backend/
    ├── api-test.md              # /api-test (project:backend)
    └── db-migrate.md            # /db-migrate (project:backend)
```

**Note**: If commands in different namespaces share the same name, they will both appear in /help with their namespace shown to distinguish them.

## File Creation Process

When creating files, follow this process:

1. **Summarize what you'll create**:
   ```
   I'll create the following file(s):
   - [File path]: [Brief description of contents]
   ```

2. **Show a preview** of the file content

3. **Ask for confirmation**:
   ```
   Does this look good? Should I create this file?
   ```

4. **Create the file** using the Write tool only after confirmation

5. **Confirm creation**:
   ```
   ✓ Created [file path]

   You can verify it was loaded by running `/memory` in Claude Code.
   ```

## Validation and Confirmation

Before creating any files:

1. **Validate the structure**:
   - YAML frontmatter is properly formatted (if applicable)
   - Glob patterns are valid
   - Rules are clear and actionable

2. **Show the user what will be created**:
   - Full file path
   - Complete file contents
   - Explanation of what the file does

3. **Get explicit confirmation**: Never create files without user approval

4. **After creation**:
   - Confirm the file was created
   - Explain how to verify it's loaded (`/memory` command)
   - Offer to create additional files if needed
