---
name: Claude Config Helper
description: Guide users through creating project-level CLAUDE.md and .claude/rules/ files by asking questions about their needs and generating appropriate configuration files
version: 1.0.0
---

# Claude Config Helper

## Overview

This Skill helps users create and manage project-level configuration files for Claude Code through an interactive, question-based approach. Instead of requiring users to understand the full complexity of Claude Code's memory system, this Skill guides them through a conversation to understand their needs and automatically creates the appropriate configuration files.

**Current Features (v1.0.0)**:
- Project-level rules configuration (CLAUDE.md and .claude/rules/)
- Interactive question-based workflow
- Automatic file creation based on user needs

**Planned Features**:
- Custom commands configuration
- Other configuration types

## When to Use This Skill

Invoke this Skill when users:
- Want to create CLAUDE.md files
- Ask about configuring Claude for their project
- Need to set up project-specific rules or preferences
- Want to create file-type specific rules
- Ask "how do I configure Claude for my project?"

## How This Skill Works

This Skill follows a 4-step interactive workflow:

1. **Ask about configuration scope**: Understand what the user wants to configure
2. **Determine file type**: Based on their needs, decide whether to create CLAUDE.md or .claude/rules/ files
3. **Collect specific rules**: Guide the user to provide the actual rules and instructions
4. **Create files**: Generate the appropriate configuration files with proper structure

## Question Flow

### Step 1: Determine Configuration Scope

Start by asking the user what they want to configure. Present clear options:

```
What would you like to configure for this project? You can choose one or more:

1. Build and test commands (e.g., "always use npm run build")
2. Code style and formatting preferences (e.g., "use 2-space indentation")
3. Architecture patterns and conventions (e.g., "follow repository pattern")
4. File-type specific rules (e.g., rules only for TypeScript files)
5. Other project-specific instructions

Please tell me the number(s) or describe what you'd like to configure.
```

### Step 2: Determine File Type

Based on the user's answer from Step 1, decide which file type to create:

**If user chose options 1, 2, 3, or 5 (global rules)**:
- Recommend creating `./CLAUDE.md` or `./.claude/CLAUDE.md`
- Explain: "These rules will apply to the entire project"
- Ask: "Would you like to create the file at the project root (./CLAUDE.md) or in a .claude directory (./.claude/CLAUDE.md)?"

**If user chose option 4 (file-type specific rules)**:
- Recommend creating `./.claude/rules/[category].md`
- Explain: "We'll create a modular rule file that can be scoped to specific file types"
- Ask: "What would you like to name this rule file? (e.g., 'typescript-rules', 'python-style', 'api-conventions')"

**If user chose multiple options**:
- Suggest creating both CLAUDE.md for global rules and separate rule files for file-specific rules
- Guide them through creating each file separately

### Step 3: Collect Specific Rules

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

### Step 4: Path-Specific Rules (If Applicable)

If creating a file in `.claude/rules/`, ask whether the rules should apply to specific file types:

```
Should these rules apply to specific file types or paths?

- If YES: Please specify glob patterns (e.g., 'src/**/*.ts' for TypeScript files in src/, '**/*.py' for all Python files)
- If NO: The rules will apply globally when this rule file is loaded

What would you prefer?
```

If the user specifies paths, you'll add YAML frontmatter to the rule file.

## Creating Files

### Scenario A: Global Project Rules (CLAUDE.md)

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

### Scenario B: Modular Rules (.claude/rules/)

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

### Scenario C: Multiple Files

If the user wants to configure multiple categories:

1. Create CLAUDE.md for global rules
2. Create separate files in `.claude/rules/` for specific categories
3. Explain the structure to the user after creation

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

## Best Practices for Asking Questions

When interacting with users:

1. **One question at a time**: Don't overwhelm users with multiple questions
2. **Provide clear options**: Give numbered choices when possible
3. **Include examples**: Show examples for each option
4. **Confirm understanding**: Repeat back what you understood before creating files
5. **Be patient**: Users may not know exactly what they want - help them discover it
6. **Explain as you go**: Briefly explain why you're asking each question

## Example Interactions

### Example 1: Simple Build Commands

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

### Example 2: TypeScript-Specific Rules

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

## Technical Notes

### Directory Creation

- Always check if `.claude/rules/` directory exists before creating rule files
- Create directories using: `mkdir -p .claude/rules`
- Handle both Windows and Unix-style paths

### YAML Frontmatter Format

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

### Glob Patterns

Common patterns to suggest:
- `**/*.ts` - All TypeScript files
- `src/**/*.ts` - TypeScript files in src/
- `*.{ts,tsx}` - TypeScript and TSX files
- `{src,lib}/**/*.ts` - TypeScript files in src/ or lib/

### File Locations

Project-level configuration files:
- `./CLAUDE.md` - Root level (visible, good for small projects)
- `./.claude/CLAUDE.md` - Hidden directory (cleaner, good for larger projects)
- `./.claude/rules/*.md` - Modular rules (best for complex projects)
- `./CLAUDE.local.md` - Personal, not committed to git (mention if user asks about personal preferences)

## Error Handling

If issues occur:

1. **Directory doesn't exist**: Create it first with `mkdir -p`
2. **File already exists**: Ask user if they want to overwrite or append
3. **Invalid glob pattern**: Explain the issue and ask for correction
4. **Unclear rules**: Ask clarifying questions before creating files

## After File Creation

Always:
1. Confirm the file was created successfully
2. Explain how to verify it's loaded (`/memory` command)
3. Ask if they want to add more configuration
4. Remind them they can edit the file directly anytime

## Resources

For more examples and templates, see:
- `resources/rules/examples/` - Example interactions and generated files
