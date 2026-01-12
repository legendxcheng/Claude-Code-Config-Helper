---
name: Claude Config Helper
description: Guide users through creating project-level CLAUDE.md, .claude/rules/, and .claude/commands/ files by asking questions about their needs and generating appropriate configuration files
version: 2.0.0
---

# Claude Config Helper

## Overview

This Skill helps users create and manage project-level configuration files for Claude Code through an interactive, question-based approach. Instead of requiring users to understand the full complexity of Claude Code's memory system, this Skill guides them through a conversation to understand their needs and automatically creates the appropriate configuration files.

**Current Features (v2.0.0)**:
- Project-level rules configuration (CLAUDE.md and .claude/rules/)
- Custom slash commands configuration (.claude/commands/)
- Interactive question-based workflow
- Automatic file creation based on user needs

## When to Use This Skill

Invoke this Skill when users:
- Want to create CLAUDE.md files
- Ask about configuring Claude for their project
- Need to set up project-specific rules or preferences
- Want to create file-type specific rules
- Want to create custom slash commands
- Ask "how do I configure Claude for my project?"
- Ask "how do I create a slash command?"
- Ask "how do I create a custom command?"

## How This Skill Works

This Skill follows a 4-step interactive workflow:

1. **Ask about configuration scope**: Understand what the user wants to configure (rules or commands)
2. **Determine file type**: Based on their needs, decide whether to create CLAUDE.md, .claude/rules/, or .claude/commands/ files
3. **Collect specific content**: Guide the user to provide the actual rules or command instructions
4. **Create files**: Generate the appropriate configuration files with proper structure

## Resources

This Skill uses modular resources for detailed guidance. Access these when needed:

### `resources/question-flow.md`
**Use when**: Starting the configuration process or guiding user through questions.
Contains the complete question flow for Steps 1-4, including:
- Step 1: Determine Configuration Scope (6 options)
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
- File Creation Process and Validation

### `resources/examples.md`
**Use when**: Needing reference for interaction patterns or showing users examples.
Contains 5 complete example interactions:
- Example 1: Simple Build Commands
- Example 2: TypeScript-Specific Rules
- Example 3: Simple Custom Command
- Example 4: Command with Bash Execution
- Example 5: Command with Arguments

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

## Quick Reference

### Configuration Types

| Type | File Location | Use Case |
|------|---------------|----------|
| Global Rules | `./CLAUDE.md` | Build commands, code style, general preferences |
| Modular Rules | `./.claude/rules/*.md` | File-type specific rules with glob patterns |
| Commands | `./.claude/commands/*.md` | Reusable slash commands |

### Command Types

| Type | Features |
|------|----------|
| Simple | Basic prompt template |
| With Arguments | Uses $ARGUMENTS or $1, $2, etc. |
| With Bash | Executes shell commands with !`command` |
| Advanced | Hooks, specific model, forked context |

## Error Handling

1. **Directory doesn't exist**: Create with `mkdir -p`
2. **File already exists**: Ask user to overwrite or append
3. **Invalid patterns**: Explain and ask for correction
4. **Unclear requirements**: Ask clarifying questions

## After File Creation

Always:
1. Confirm the file was created
2. Explain verification method (`/memory` for rules, `/help` for commands)
3. Ask if they want to add more configuration
