# Example Interaction 2: TypeScript-Specific Rules

This example shows a complete interaction where a user wants to create TypeScript-specific coding rules that only apply to TypeScript files.

---

## Conversation Flow

**User**: "I need to set up TypeScript rules"

**Claude (using Claude Config Helper Skill)**:

"I'll help you set up TypeScript-specific rules. What would you like to configure for this project? You can choose one or more:

1. Build and test commands
2. Code style and formatting preferences
3. Architecture patterns and conventions
4. File-type specific rules
5. Other project-specific instructions

Please tell me the number(s) or describe what you'd like to configure."

---

**User**: "4 - TypeScript specific"

**Claude**:

"Perfect! We'll create a modular rule file that can be scoped to TypeScript files. What would you like to name this rule file? (e.g., 'typescript-rules', 'typescript-style', 'ts-conventions')"

---

**User**: "typescript-rules"

**Claude**:

"Great! Please describe the specific rules you want Claude to follow for TypeScript files. For example:
- 'Use explicit return types for all functions'
- 'Prefer interfaces over type aliases'
- 'Avoid using any type'

What TypeScript rules would you like to add?"

---

**User**: "Always use explicit return types, prefer interfaces, avoid any, use strict null checks"

**Claude**:

"Excellent! Should these rules apply to specific file types or paths?

- If YES: Please specify glob patterns (e.g., 'src/**/*.ts' for TypeScript files in src/)
- If NO: The rules will apply globally when this rule file is loaded

What would you prefer?"

---

**User**: "Yes, src/**/*.ts and src/**/*.tsx"

**Claude**:

"Perfect! I'll create the following file:

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

---

**User**: "yes"

**Claude**:

[Uses Bash to create .claude/rules/ directory if needed]
[Uses Write tool to create ./.claude/rules/typescript-rules.md]

"✓ Created ./.claude/rules/typescript-rules.md

This rule file will only apply when working with TypeScript files in the src/ directory. You can verify it was loaded by running `/memory` in Claude Code. Would you like to add any other configuration?"

---

**User**: "no thanks"

**Claude**:

"Perfect! Your TypeScript rules are now configured. Claude will now:
- Use explicit return types for all functions in src/**/*.ts and src/**/*.tsx files
- Prefer interfaces over type aliases
- Avoid using `any` type
- Use strict null checks

These rules only apply to TypeScript files in the src/ directory. You can edit ./.claude/rules/typescript-rules.md anytime to update these rules."

---

## Result

**File Created**: `./.claude/rules/typescript-rules.md`

**File Contents**:
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

## Key Takeaways

1. **Modular rules**: Used .claude/rules/ for file-type specific rules
2. **Path-specific**: YAML frontmatter with `paths` field limits scope
3. **Glob patterns**: Used `src/**/*.ts` and `src/**/*.tsx` to target specific files
4. **Clear naming**: File named `typescript-rules.md` makes purpose obvious
5. **Scoped application**: Rules only apply when working with matching files

## Technical Details

**YAML Frontmatter**:
- Three dashes before and after (`---`)
- `paths:` field with array of glob patterns
- Each pattern on new line with `  - ` prefix
- Patterns in double quotes

**Glob Patterns Used**:
- `src/**/*.ts` - All TypeScript files in src/ and subdirectories
- `src/**/*.tsx` - All TSX files in src/ and subdirectories

**Directory Structure Created**:
```
project-root/
└── .claude/
    └── rules/
        └── typescript-rules.md
```
