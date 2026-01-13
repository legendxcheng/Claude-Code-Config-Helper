# Generated Command: Code Review

This is an example of a simple custom command for code review.

---

## File Location

`.claude/commands/review.md`

---

## File Contents

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

---

## Usage

```bash
# Invoke the command
/review

# The command will review whatever code is in context
```

---

## Behavior

When `/review` is invoked:
1. Claude receives the instructions from this file
2. Claude applies the review criteria to the code in context
3. Claude provides detailed feedback for each issue found

---

## Customization Ideas

- Add project-specific coding standards
- Include framework-specific checks (React, Vue, etc.)
- Add performance benchmarks
- Include accessibility checks for frontend code
