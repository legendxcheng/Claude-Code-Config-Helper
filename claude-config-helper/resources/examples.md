# Example Interactions

This document contains complete example interactions demonstrating how to use the Claude Config Helper Skill.

## Example 1: Simple Build Commands

**User**: "I want to configure Claude for my project"

**Claude**: "I'll help you set up project configuration. What would you like to configure for this project? You can choose one or more:

1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions

Please tell me the number(s) or describe what you'd like to configure."

**User**: "1"

**Claude**: "Great! I'll help you configure build and test commands. These rules will apply to the entire project. Would you like to create the file at the project root (./CLAUDE.md) or in a .claude directory (./.claude/CLAUDE.md)?"

**User**: "project root"

**Claude**: "Perfect. Please describe the specific build and test commands you want Claude to follow. For example:
- 'Always use npm run build to build the project'
- 'Run tests with npm test before committing'

What commands would you like to add?"

**User**: "Use npm run build to build, npm test to test, and npm run lint before committing"

**Claude**: "Got it! I'll create the following file:

**File**: ./CLAUDE.md

**Contents**:
```markdown
# Project Configuration for Claude

## Build and Test Commands

- Use `npm run build` to build the project
- Use `npm test` to run tests
- Always run `npm run lint` before committing changes
```

Does this look good? Should I create this file?"

**User**: "yes"

**Claude**: [Creates file using Write tool]

"✓ Created ./CLAUDE.md

You can verify it was loaded by running `/memory` in Claude Code. Would you like to add any other configuration?"

## Example 2: TypeScript-Specific Rules

**User**: "I need to set up TypeScript rules"

**Claude**: "I'll help you set up TypeScript-specific rules. What would you like to configure for this project? You can choose one or more:

1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions

Please tell me the number(s) or describe what you'd like to configure."

**User**: "4 - TypeScript specific"

**Claude**: "Perfect! We'll create a modular rule file that can be scoped to TypeScript files. What would you like to name this rule file? (e.g., 'typescript-rules', 'typescript-style', 'ts-conventions')"

**User**: "typescript-rules"

**Claude**: "Great! Please describe the specific rules you want Claude to follow for TypeScript files. For example:
- 'Use explicit return types for all functions'
- 'Prefer interfaces over type aliases'
- 'Avoid using any type'

What TypeScript rules would you like to add?"

**User**: "Always use explicit return types, prefer interfaces, avoid any, use strict null checks"

**Claude**: "Excellent! Should these rules apply to specific file types or paths?

- If YES: Please specify glob patterns (e.g., 'src/**/*.ts' for TypeScript files in src/)
- If NO: The rules will apply globally when this rule file is loaded

What would you prefer?"

**User**: "Yes, src/**/*.ts and src/**/*.tsx"

**Claude**: "Perfect! I'll create the following file:

**File**: ./.claude/rules/typescript-rules.md

**Contents**:
```markdown
---
paths:
  - "src/**/*.ts"
  - "src/**/*.tsx"
---

# TypeScript Code Standards

- Use explicit return types for all functions
- Prefer interfaces over type aliases for object shapes
- Avoid using `any` type - use `unknown` if type is truly unknown
- Use strict null checks
```

Does this look good? Should I create this file?"

**User**: "yes"

**Claude**: [Creates directory if needed, then creates file using Write tool]

"✓ Created ./.claude/rules/typescript-rules.md

This rule file will only apply when working with TypeScript files in the src/ directory. You can verify it was loaded by running `/memory` in Claude Code. Would you like to add any other configuration?"

## Example 3: Simple Custom Command

**User**: "I want to create a custom command for code review"

**Claude**: "I'll help you create a custom slash command. What would you like to configure for this project? You can choose one or more:

1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions
6. Custom slash commands (reusable prompts you can invoke with /command-name)

Please tell me the number(s) or describe what you'd like to configure."

**User**: "6"

**Claude**: "Great! We'll create a custom slash command. What would you like to name this command? (e.g., 'review', 'deploy', 'test-api')

The command name will be used to invoke it, like `/review`."

**User**: "review"

**Claude**: "What type of command would you like to create?

1. Simple command - A reusable prompt template
2. Command with arguments - Accepts parameters when invoked
3. Command with bash execution - Runs shell commands and uses their output
4. Advanced command - Includes hooks, specific model, or forked context

Please choose a number or describe what you need."

**User**: "1 - simple"

**Claude**: "Should this command be:

1. Project-specific (.claude/commands/) - Available only in this project, shared with team via git
2. Personal (~/.claude/commands/) - Available across all your projects, not shared

Which would you prefer?"

**User**: "1 - project"

**Claude**: "Please provide a brief description of what this command does. This will be shown when users type /help or autocomplete the command."

**User**: "Review code for bugs and security issues"

**Claude**: "Now describe the actual instructions Claude should follow when /review is invoked."

**User**: "Review the code for security vulnerabilities, performance issues, and bugs. Provide specific suggestions with code examples."

**Claude**: "I'll create the following file:

**File**: ./.claude/commands/review.md

**Contents**:
```markdown
---
description: Review code for bugs and security issues
---

Review the provided code for:
- Security vulnerabilities (injection, XSS, CSRF, etc.)
- Performance issues and inefficiencies
- Potential bugs and edge cases
- Code quality and maintainability

Provide specific suggestions for each issue found with code examples showing the fix.
```

Does this look good? Should I create this file?"

**User**: "yes"

**Claude**: [Creates directory if needed, then creates file using Write tool]

"✓ Created ./.claude/commands/review.md

You can now use this command by typing `/review` in Claude Code. It will appear in /help as 'review (project)'. Would you like to create any other commands?"

## Example 4: Command with Bash Execution

**User**: "I need a commit command that shows git status first"

**Claude**: "I'll help you create a custom slash command with git integration. What would you like to configure for this project?

1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions
6. Custom slash commands (reusable prompts you can invoke with /command-name)

Please tell me the number(s) or describe what you'd like to configure."

**User**: "6"

**Claude**: "What would you like to name this command?"

**User**: "commit"

**Claude**: "What type of command would you like to create?

1. Simple command - A reusable prompt template
2. Command with arguments - Accepts parameters when invoked
3. Command with bash execution - Runs shell commands and uses their output
4. Advanced command - Includes hooks, specific model, or forked context"

**User**: "3 - with bash"

**Claude**: "Should this command be project-specific or personal?"

**User**: "project"

**Claude**: "Please provide a brief description."

**User**: "Create a git commit with proper message"

**Claude**: "What bash commands should be executed to gather context? Common examples:
- `git status` - Show current status
- `git diff HEAD` - Show changes
- `git log --oneline -10` - Recent commits"

**User**: "git status, git diff HEAD, git branch --show-current, git log --oneline -5"

**Claude**: "What instructions should Claude follow after seeing the git context?"

**User**: "Create a commit with a good message following conventional commits"

**Claude**: "I'll create the following file:

**File**: ./.claude/commands/commit.md

**Contents**:
```markdown
---
description: Create a git commit with proper message
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git log:*), Bash(git branch:*)
---

## Context

- Current git status: !`git status`
- Pending changes: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Your Task

Based on the changes shown above, create a git commit.

1. Review the staged and unstaged changes
2. Generate an appropriate commit message following conventional commits format:
   - type(scope): description
   - Types: feat, fix, docs, style, refactor, test, chore
3. Stage relevant files if needed
4. Create the commit

If the changes are too large or unrelated, suggest splitting into multiple commits.
```

Does this look good? Should I create this file?"

**User**: "yes"

**Claude**: [Creates file using Write tool]

"✓ Created ./.claude/commands/commit.md

You can now use `/commit` to create well-formatted git commits. The command will automatically show you the current git status and changes before creating the commit. Would you like to add any other configuration?"

## Example 5: Command with Arguments

**User**: "I want a command to fix GitHub issues by number"

**Claude**: "I'll help you create a command that accepts an issue number. What type of command would you like?

1. Simple command
2. Command with arguments
3. Command with bash execution
4. Advanced command"

**User**: "2"

**Claude**: "What would you like to name this command?"

**User**: "fix-issue"

**Claude**: "What argument hint should be shown? For example: [issue-number], [id], etc."

**User**: "[issue-number]"

**Claude**: "Please provide a description."

**User**: "Fix a GitHub issue"

**Claude**: "What instructions should Claude follow? You can use $ARGUMENTS to reference the issue number."

**User**: "Look up the issue, understand it, fix it, and write tests"

**Claude**: "I'll create the following file:

**File**: ./.claude/commands/fix-issue.md

**Contents**:
```markdown
---
description: Fix a GitHub issue
argument-hint: [issue-number]
---

Fix GitHub issue #$ARGUMENTS following our project standards.

## Steps

1. **Understand the issue**: Read the issue description and any comments to fully understand the problem
2. **Locate relevant code**: Find the files and functions related to this issue
3. **Implement the fix**: Make the necessary code changes
4. **Write tests**: Add or update tests to cover the fix
5. **Verify**: Ensure existing tests still pass
6. **Summarize**: Provide a summary of what was changed and why

Reference the issue number in your commit message: \"fix: resolve #$ARGUMENTS\"
```

Does this look good? Should I create this file?"

**User**: "yes"

**Claude**: [Creates file using Write tool]

"✓ Created ./.claude/commands/fix-issue.md

You can now use `/fix-issue 123` to fix issue #123. The issue number will be passed to Claude automatically. Would you like to create any other commands?"
