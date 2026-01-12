# Example Interaction 1: Configuring Build Commands

This example shows a complete interaction where a user wants to configure build and test commands for their project.

---

## Conversation Flow

**User**: "I want to configure Claude for my project"

**Claude (using Claude Config Helper Skill)**:

"I'll help you set up project configuration. What would you like to configure for this project? You can choose one or more:

1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions

Please tell me the number(s) or describe what you'd like to configure."

---

**User**: "1"

**Claude**:

"Great! I'll help you configure build and test commands. These rules will apply to the entire project. Would you like to create the file at the project root (./CLAUDE.md) or in a .claude directory (./.claude/CLAUDE.md)?"

---

**User**: "project root"

**Claude**:

"Perfect. Please describe the specific build and test commands you want Claude to follow. For example:
- 'Always use npm run build to build the project'
- 'Run tests with npm test before committing'

What commands would you like to add?"

---

**User**: "Use npm run build to build, npm test to test, and npm run lint before committing"

**Claude**:

"Got it! I'll create the following file:

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

---

**User**: "yes"

**Claude**:

[Uses Write tool to create ./CLAUDE.md]

"✓ Created ./CLAUDE.md

You can verify it was loaded by running `/memory` in Claude Code. Would you like to add any other configuration?"

---

**User**: "no, that's all"

**Claude**:

"Perfect! Your project is now configured. Claude will now:
- Use `npm run build` when building the project
- Use `npm test` when running tests
- Remind you to run `npm run lint` before committing

You can edit ./CLAUDE.md anytime to update these rules."

---

## Result

**File Created**: `./CLAUDE.md`

**File Contents**:
```markdown
# Project Configuration for Claude

## Build and Test Commands

- Use `npm run build` to build the project
- Use `npm test` to run tests
- Always run `npm run lint` before committing changes
```

## Key Takeaways

1. **Simple workflow**: User answered 3 questions and got a configured project
2. **Clear options**: Numbered choices made it easy to select
3. **Confirmation**: User saw the file contents before creation
4. **Verification**: User was told how to verify the configuration loaded
5. **Global rules**: CLAUDE.md at root applies to entire project
