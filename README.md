# Claude Config Helper

A Claude Code Skill that helps users create and manage project-level configuration files through an interactive, question-based approach.

## Overview

Claude Config Helper guides users through creating CLAUDE.md, .claude/rules/, and .claude/commands/ configuration files without requiring them to understand the full complexity of Claude Code's memory system. Instead of reading documentation, users simply answer questions about what they want to configure, and the Skill creates the appropriate files automatically.

## Features

### Current Version (v1.1.0)

- **Interactive workflow**: Question-based approach to gather user requirements
- **Project-level rules**: Create CLAUDE.md files for global project configuration
- **Modular rules**: Create .claude/rules/ files for organized, topic-specific rules
- **Path-specific rules**: Scope rules to specific file types using glob patterns
- **Custom slash commands**: Create .claude/commands/ files for reusable prompts
- **Commands with bash execution**: Create commands that gather context from shell commands
- **Commands with arguments**: Create commands that accept parameters
- **Automatic file creation**: Generate properly formatted configuration files
- **Validation and confirmation**: Preview files before creation

### Planned Features

- Additional configuration types (hooks, plugins)
- Templates for common project types

## Installation

1. Download the `claude-config-helper.zip` file
2. In Claude Code, go to Settings > Capabilities
3. Click "Add Skill" and upload the ZIP file
4. Enable the "Claude Config Helper" skill

## Usage

### Triggering the Skill

The Skill activates when you ask Claude to help with project configuration:

- "I want to configure Claude for my project"
- "Help me create a CLAUDE.md file"
- "I need to set up project rules"
- "How do I configure Claude Code for this project?"
- "I want to create a custom slash command"
- "Help me create a /review command"

### Workflow

1. **Choose what to configure**: Select from build commands, code style, architecture patterns, file-specific rules, custom commands, or other instructions
2. **Specify file type and location**: Choose between CLAUDE.md, .claude/rules/, or .claude/commands/
3. **Provide your content**: Describe the specific rules or command instructions
4. **Configure options** (for commands): Add arguments, bash execution, or advanced features
5. **Confirm and create**: Review the file contents and confirm creation

### Example Interactions

#### Example 1: Simple Build Commands

```
You: "I want to configure Claude for my project"

Claude: "What would you like to configure? Choose one or more:
1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions
6. Custom slash commands"

You: "1"

Claude: "Would you like to create the file at the project root (./CLAUDE.md)
or in a .claude directory (./.claude/CLAUDE.md)?"

You: "project root"

Claude: "Please describe the specific build and test commands..."

You: "Use npm run build to build, npm test to test"

Claude: [Shows preview and creates ./CLAUDE.md]
```

#### Example 2: TypeScript-Specific Rules

```
You: "I need TypeScript rules"

Claude: "What would you like to configure? ..."

You: "4 - file-type specific"

Claude: "What would you like to name this rule file?"

You: "typescript-rules"

Claude: "Please describe the specific rules..."

You: "Use explicit return types, prefer interfaces, avoid any"

Claude: "Should these rules apply to specific paths?"

You: "Yes, src/**/*.ts and src/**/*.tsx"

Claude: [Shows preview and creates ./.claude/rules/typescript-rules.md with YAML frontmatter]
```

#### Example 3: Custom Slash Command

```
You: "I want to create a code review command"

Claude: "What would you like to configure? ..."

You: "6 - custom slash commands"

Claude: "What would you like to name this command?"

You: "review"

Claude: "What type of command?
1. Simple command
2. Command with arguments
3. Command with bash execution
4. Advanced command"

You: "1 - simple"

Claude: "Please provide a description..."

You: "Review code for bugs and security issues"

Claude: "What instructions should Claude follow?"

You: "Check for security vulnerabilities, performance issues, and code style"

Claude: [Shows preview and creates ./.claude/commands/review.md]
```

#### Example 4: Command with Bash Execution

```
You: "I need a commit command that shows git status first"

Claude: "What type of command?"

You: "3 - with bash"

Claude: "What bash commands should gather context?"

You: "git status, git diff HEAD, git log --oneline -5"

Claude: "What should Claude do after seeing the context?"

You: "Create a commit with a good message following conventional commits"

Claude: [Shows preview and creates ./.claude/commands/commit.md with allowed-tools]
```

## File Types Created

### CLAUDE.md (Global Rules)

Created at `./CLAUDE.md` or `./.claude/CLAUDE.md`

**Use for**:
- Build and test commands
- Code style preferences
- Architecture patterns
- General project instructions

**Example**:
```markdown
# Project Configuration for Claude

## Build Commands
- Use `npm run build` to build the project
- Use `npm test` to run tests
```

### .claude/rules/*.md (Modular Rules)

Created at `./.claude/rules/[name].md`

**Use for**:
- File-type specific rules
- Topic-specific conventions
- Path-scoped instructions

**Example**:
```markdown
---
paths:
  - "src/**/*.ts"
---

# TypeScript Standards
- Use explicit return types
- Prefer interfaces over type aliases
```

### .claude/commands/*.md (Custom Commands)

Created at `./.claude/commands/[name].md` or `~/.claude/commands/[name].md`

**Use for**:
- Reusable prompt templates
- Automated workflows
- Commands with bash context gathering

**Example (simple)**:
```markdown
---
description: Review code for bugs and security issues
---

Review the provided code for:
- Security vulnerabilities
- Performance issues
- Code style violations
```

**Example (with bash)**:
```markdown
---
description: Create a git commit with proper message
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
---

## Context
- Status: !`git status`
- Changes: !`git diff HEAD`

## Task
Create a well-formatted commit based on the changes.
```

## Command Features

### Arguments
Commands can accept arguments using `$ARGUMENTS` or `$1`, `$2`, etc.

```markdown
---
argument-hint: [issue-number]
---

Fix issue #$ARGUMENTS following our coding standards.
```

### Bash Execution
Use `!`command`` to execute bash commands and include output:

```markdown
- Current branch: !`git branch --show-current`
- Pending changes: !`git diff HEAD`
```

### Allowed Tools
Specify which tools the command can use:

```yaml
allowed-tools: Bash(git:*), Bash(npm:*), Read, Write
```

### Advanced Options
- `model`: Specify a model
- `context: fork`: Run in isolated context
- `hooks`: Add command-scoped hooks

## Verification

After creating configuration files, verify they're loaded:

```bash
# For rules and CLAUDE.md
/memory

# For commands
/help
```

## Project Structure

```
claude-config-helper/
├── Skill.md                          # Core skill instructions
└── resources/
    ├── rules/
    │   └── examples/
    │       ├── interaction-example-1.md              # Build commands example
    │       ├── interaction-example-2.md              # TypeScript rules example
    │       ├── generated-claude-md.md                # Example CLAUDE.md file
    │       └── generated-path-specific-rule.md       # Example path-specific rule
    └── commands/
        └── examples/
            ├── interaction-example-simple-command.md # Simple command example
            ├── interaction-example-bash-command.md   # Bash command example
            ├── generated-command-review.md           # Example review command
            ├── generated-command-commit.md           # Example commit command
            └── generated-command-deploy.md           # Example deploy command
```

## Best Practices

### For Rules
- **Be specific**: Provide clear, actionable rules
- **Use modular rules**: For large projects, create separate rule files for different topics
- **Use path-specific rules**: Scope rules to relevant file types
- **Review periodically**: Update rules as your project evolves

### For Commands
- **Start simple**: Begin with basic commands and add complexity as needed
- **Use descriptive names**: Command names should indicate their purpose
- **Add descriptions**: Always include a description for /help visibility
- **Be specific with tools**: Only allow the tools the command actually needs

## Troubleshooting

**Skill not activating?**
- Make sure it's enabled in Settings > Capabilities
- Try explicitly asking "use the Claude Config Helper skill"

**Files not loading?**
- For rules: Run `/memory` to verify files are loaded
- For commands: Run `/help` to see available commands
- Check file paths are correct
- Ensure YAML frontmatter is properly formatted

**Command not appearing in /help?**
- Ensure the command file has a `description` in frontmatter
- Check that the file is in `.claude/commands/` or `~/.claude/commands/`
- Verify the file has a `.md` extension

**Want to modify existing files?**
- Use `/memory` to open rule files in your editor
- Or ask Claude to help update specific rules or commands

## Contributing

This is an open-source Skill. Contributions are welcome!

## Version History

- **v1.1.0** (Current): Added custom slash commands configuration support
- **v1.0.0**: Initial release with project-level rules configuration

## License

MIT License

## Support

For issues or questions:
- Check the examples in `resources/rules/examples/` and `resources/commands/examples/`
- Review the Skill.md file for detailed instructions
- Ask Claude for help using the Skill

---

**Made for the Claude Code community**
