# Example Interaction: Creating a Simple Custom Command

This example shows a complete conversation flow for creating a simple code review command.

---

## Conversation Flow

**User**: "I want to create a custom command for reviewing code"

**Claude**: "I'll help you create a custom slash command. What would you like to configure for this project? You can choose one or more:

1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions
6. Custom slash commands (reusable prompts you can invoke with /command-name)

Please tell me the number(s) or describe what you'd like to configure."

**User**: "6"

**Claude**: "Great! We'll create a custom slash command. What would you like to name this command? (e.g., 'review', 'check', 'audit')

The command name will be used to invoke it, like `/review`."

**User**: "review"

**Claude**: "What type of command would you like to create?

1. Simple command - A reusable prompt template
2. Command with arguments - Accepts parameters when invoked
3. Command with bash execution - Runs shell commands and uses their output
4. Advanced command - Includes hooks, specific model, or forked context

Please choose a number or describe what you need."

**User**: "1"

**Claude**: "Should this command be:

1. Project-specific (.claude/commands/) - Available only in this project, shared with team via git
2. Personal (~/.claude/commands/) - Available across all your projects, not shared

Which would you prefer?"

**User**: "1 - project specific"

**Claude**: "Please provide a brief description of what this command does. This will be shown when users type /help or autocomplete the command."

**User**: "Review code for bugs, security issues, and best practices"

**Claude**: "Now describe the actual instructions Claude should follow when /review is invoked. What specific things should be checked?"

**User**: "Check for security vulnerabilities like injection and XSS, look for performance issues, check code style, and find potential bugs. Give specific suggestions with examples."

**Claude**: "I'll create the following file:

**File**: ./.claude/commands/review.md

**Contents**:
```markdown
---
description: Review code for bugs, security issues, and best practices
---

Review the provided code thoroughly for the following:

## Security Vulnerabilities
- SQL injection risks
- XSS (Cross-Site Scripting) vulnerabilities
- CSRF (Cross-Site Request Forgery) issues
- Authentication and authorization flaws
- Sensitive data exposure

## Performance Issues
- Inefficient algorithms or data structures
- Unnecessary database queries
- Memory leaks or excessive memory usage
- Blocking operations that could be async

## Code Style & Quality
- Adherence to project coding standards
- Code readability and maintainability
- Proper error handling
- Appropriate use of comments

## Potential Bugs
- Edge cases not handled
- Race conditions
- Null/undefined reference errors
- Logic errors

For each issue found, provide:
1. The specific location in the code
2. Why it's a problem
3. A concrete suggestion or code example to fix it
```

Does this look good? Should I create this file?"

**User**: "yes"

**Claude**: [Creates directory if needed, then creates file]

"✓ Created ./.claude/commands/review.md

You can now use this command by typing `/review` in Claude Code. It will appear in /help as 'review (project)'.

To use it, simply type `/review` when you want Claude to review some code. Would you like to create any other commands?"

---

## Generated File

See `generated-command-review.md` for the complete generated command file.
