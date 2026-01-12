# Claude Config Helper

A Claude Code Skill that helps users create and manage project-level configuration files through an interactive, question-based approach.

## Overview

Claude Config Helper guides users through creating CLAUDE.md and .claude/rules/ configuration files without requiring them to understand the full complexity of Claude Code's memory system. Instead of reading documentation, users simply answer questions about what they want to configure, and the Skill creates the appropriate files automatically.

## Features

### Current Version (v1.0.0)

- **Interactive workflow**: Question-based approach to gather user requirements
- **Project-level rules**: Create CLAUDE.md files for global project configuration
- **Modular rules**: Create .claude/rules/ files for organized, topic-specific rules
- **Path-specific rules**: Scope rules to specific file types using glob patterns
- **Automatic file creation**: Generate properly formatted configuration files
- **Validation and confirmation**: Preview files before creation

### Planned Features

- Custom commands configuration
- Additional configuration types
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

### Workflow

1. **Choose what to configure**: Select from build commands, code style, architecture patterns, file-specific rules, or other instructions
2. **Specify file location**: Choose between root-level CLAUDE.md or modular .claude/rules/ files
3. **Provide your rules**: Describe the specific rules you want Claude to follow
4. **Add path restrictions** (optional): Limit rules to specific file types using glob patterns
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
5. Other project-specific instructions"

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

## Verification

After creating configuration files, verify they're loaded:

```bash
/memory
```

This command shows all loaded memory files and their contents.

## Editing Configuration

To edit configuration files later:

```bash
/memory
```

This opens the memory files in your system editor for quick updates.

## Project Structure

```
claude-config-helper/
├── Skill.md                          # Core skill instructions
└── resources/
    └── rules/
        └── examples/
            ├── interaction-example-1.md              # Build commands example
            ├── interaction-example-2.md              # TypeScript rules example
            ├── generated-claude-md.md                # Example CLAUDE.md file
            └── generated-path-specific-rule.md       # Example path-specific rule
```

## How It Works

The Skill uses a progressive disclosure approach:

1. **Metadata**: Claude reads the Skill description to know when to invoke it
2. **Question flow**: Guides users through a series of questions
3. **File generation**: Creates appropriate files based on user responses
4. **Validation**: Shows preview and gets confirmation before creating files

## Best Practices

- **Be specific**: Provide clear, actionable rules
- **Use modular rules**: For large projects, create separate rule files for different topics
- **Use path-specific rules**: Scope rules to relevant file types
- **Review periodically**: Update rules as your project evolves
- **Start simple**: Begin with basic rules and expand as needed

## Troubleshooting

**Skill not activating?**
- Make sure it's enabled in Settings > Capabilities
- Try explicitly asking "use the Claude Config Helper skill"

**Files not loading?**
- Run `/memory` to verify files are loaded
- Check file paths are correct
- Ensure YAML frontmatter is properly formatted (for path-specific rules)

**Want to modify existing files?**
- Use `/memory` to open files in your editor
- Or ask Claude to help update specific rules

## Contributing

This is an open-source Skill. Contributions are welcome!

## Version History

- **v1.0.0** (Current): Initial release with project-level rules configuration

## License

MIT License

## Support

For issues or questions:
- Check the examples in `resources/rules/examples/`
- Review the Skill.md file for detailed instructions
- Ask Claude for help using the Skill

---

**Made with ❤️ for the Claude Code community**
