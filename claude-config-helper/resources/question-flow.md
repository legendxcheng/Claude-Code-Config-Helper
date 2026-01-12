# Question Flow

This document contains the detailed question flow for the Claude Config Helper Skill.

## Step 1: Determine Configuration Scope

Start by asking the user what they want to configure. Present clear options:

```
What would you like to configure for this project? You can choose one or more:

1. Build and test commands (e.g., "always use npm run build")
2. Code style and formatting preferences (e.g., "use 2-space indentation")
3. Architecture patterns and conventions (e.g., "follow repository pattern")
4. File-type specific rules (e.g., rules only for TypeScript files)
5. Other project-specific instructions
6. Custom slash commands (reusable prompts you can invoke with /command-name)
7. Hooks (automation: auto-format code, protect files, log commands, notifications)

Please tell me the number(s) or describe what you'd like to configure.
```

## Step 2: Determine File Type

Based on the user's answer from Step 1, decide which file type to create:

**If user chose options 1, 2, 3, or 5 (global rules)**:
- Recommend creating `./CLAUDE.md` or `./.claude/CLAUDE.md`
- Explain: "These rules will apply to the entire project"
- Ask: "Would you like to create the file at the project root (./CLAUDE.md) or in a .claude directory (./.claude/CLAUDE.md)?"

**If user chose option 4 (file-type specific rules)**:
- Recommend creating `./.claude/rules/[category].md`
- Explain: "We'll create a modular rule file that can be scoped to specific file types"
- Ask: "What would you like to name this rule file? (e.g., 'typescript-rules', 'python-style', 'api-conventions')"

**If user chose option 6 (custom slash commands)**:
- Recommend creating `./.claude/commands/[command-name].md`
- Explain: "We'll create a custom slash command that you can invoke with /command-name"
- Ask: "What would you like to name this command? (e.g., 'review', 'deploy', 'test-api')"
- Then proceed to Step 2b for commands

**If user chose option 7 (hooks)**:
- **Redirect to the Hooks-specific question flow**
- Load `resources/hooks/question-flow-hooks.md` for detailed guidance
- Explain: "Hooks are shell commands that run automatically at specific points in Claude's workflow"
- Common use cases to mention:
  - Auto-format code after edits (PostToolUse)
  - Block edits to sensitive files (PreToolUse)
  - Log all bash commands (PreToolUse)
  - Custom notifications (Notification)
- Proceed to Steps H1-H5 in the hooks question flow

**If user chose multiple options**:
- Suggest creating both CLAUDE.md for global rules and separate rule files for file-specific rules
- Guide them through creating each file separately

## Step 2b: Determine Command Type (For Custom Commands)

If the user is creating a custom command, ask about the command complexity:

```
What type of command would you like to create?

1. Simple command - A reusable prompt template (e.g., "review this code for bugs")
2. Command with arguments - Accepts parameters when invoked (e.g., "/fix-issue 123")
3. Command with bash execution - Runs shell commands and uses their output (e.g., git status, npm commands)
4. Advanced command - Includes hooks, specific model, or forked context

Please choose a number or describe what you need.
```

Also ask about the command scope:
```
Should this command be:

1. Project-specific (.claude/commands/) - Available only in this project, shared with team via git
2. Personal (~/.claude/commands/) - Available across all your projects, not shared

Which would you prefer?
```

## Step 3: Collect Specific Rules

Once the file type is determined, collect the actual rules from the user:

```
Please describe the specific rules or instructions you want Claude to follow.

You can provide them as:
- Natural language descriptions
- Bullet points
- Examples of what you want

For example:
- "Always use npm run build to build the project"
- "Use 2-space indentation for all TypeScript files"
- "Follow the repository pattern for database access"
- "Never commit .env files"

What rules would you like to add?
```

**Important**:
- Accept rules in any format the user provides
- You will format them properly when creating the file
- If rules are vague, ask clarifying questions
- Encourage users to be specific

## Step 3b: Collect Command Details (For Custom Commands)

If the user is creating a custom command, collect the following information:

**1. Command Description** (required):
```
Please provide a brief description of what this command does.
This will be shown when users type /help or autocomplete the command.

For example: "Review code for security vulnerabilities and best practices"
```

**2. Argument Hint** (if command uses arguments):
```
What arguments should users provide when invoking this command?
This hint will be shown during autocomplete.

For example:
- "[filename]" for a single file argument
- "[issue-number] [priority]" for multiple arguments
- "[message]" for a commit message

What argument hint would you like to use?
```

**3. Command Instructions** (required):
```
Now describe the actual instructions Claude should follow when this command is invoked.

You can include:
- Step-by-step instructions
- Specific behaviors or patterns to follow
- References to files using @filepath
- Bash commands to execute using !`command`

For example:
"Review the provided code for:
- Security vulnerabilities
- Performance issues
- Code style violations
Provide specific suggestions for each issue found."

What should Claude do when this command is invoked?
```

**4. Bash Commands** (if command type includes bash execution):
```
What bash commands should be executed? The output will be available to Claude.

For example:
- !`git status` - Show current git status
- !`git diff HEAD` - Show pending changes
- !`npm test` - Run tests

List the bash commands you want to include:
```

**5. Allowed Tools** (if command uses bash):
```
Which tools should this command be allowed to use?
This is required for commands that execute bash commands.

Common patterns:
- Bash(git add:*), Bash(git status:*), Bash(git commit:*) - For git operations
- Bash(npm:*) - For npm commands
- Bash(python:*) - For Python scripts

What tools should be allowed?
```

## Step 4: Path-Specific Rules (If Applicable)

If creating a file in `.claude/rules/`, ask whether the rules should apply to specific file types:

```
Should these rules apply to specific file types or paths?

- If YES: Please specify glob patterns (e.g., 'src/**/*.ts' for TypeScript files in src/, '**/*.py' for all Python files)
- If NO: The rules will apply globally when this rule file is loaded

What would you prefer?
```

If the user specifies paths, you'll add YAML frontmatter to the rule file.
