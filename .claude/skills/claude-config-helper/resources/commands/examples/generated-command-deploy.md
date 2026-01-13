# Generated Command: Deploy with Validation

This is an example of an advanced command with hooks and forked context.

---

## File Location

`.claude/commands/deploy.md`

---

## File Contents

```markdown
---
description: Deploy to staging with pre-flight validation
allowed-tools: Bash(npm:*), Bash(git:*), Bash(docker:*)
context: fork
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-deploy.sh"
          once: true
---

## Pre-deployment Checks

Before deploying, verify the following:

- **Current Branch**: !`git branch --show-current`
- **Uncommitted Changes**: !`git status --porcelain`
- **Test Results**: !`npm test -- --reporter=summary 2>&1 || echo "Tests need attention"`
- **Build Status**: !`npm run build --if-present 2>&1 | tail -5`

## Deployment Process

### 1. Validation
- Ensure you're on an appropriate branch (main, staging, or release/*)
- Confirm no uncommitted changes exist
- Verify all tests pass
- Check that the build succeeds

### 2. Build
```bash
npm run build
```

### 3. Deploy
```bash
docker build -t app:staging .
docker push registry.example.com/app:staging
kubectl apply -f k8s/staging/
```

### 4. Verification
After deployment:
- Check pod status: `kubectl get pods -n staging`
- Verify health endpoint responds
- Run smoke tests if available

## Safety Rules

- **NEVER** deploy to production from this command
- Always verify the deployment target before proceeding
- If any pre-flight check fails, stop and report the issue
- Log all deployment actions for audit purposes

## Rollback Instructions

If deployment fails:
```bash
kubectl rollout undo deployment/app -n staging
```
```

---

## Usage

```bash
# Deploy to staging
/deploy

# The command runs in a forked context and validates before deployment
```

---

## Key Features

### Forked Context
```yaml
context: fork
```
Runs the command in an isolated sub-agent context. This means:
- Separate conversation history
- Doesn't affect the main conversation
- Ideal for complex, multi-step operations

### Command-Scoped Hooks
```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-deploy.sh"
          once: true
```
- Runs `validate-deploy.sh` before any Bash command
- `once: true` means it only runs once per session
- Hooks are cleaned up when the command finishes

### Multiple Allowed Tools
```yaml
allowed-tools: Bash(npm:*), Bash(git:*), Bash(docker:*)
```
Allows npm, git, and docker commands for the deployment workflow.

---

## Validation Script Example

Create `.scripts/validate-deploy.sh`:

```bash
#!/bin/bash

# Check if on allowed branch
BRANCH=$(git branch --show-current)
if [[ ! "$BRANCH" =~ ^(main|staging|release/).*$ ]]; then
    echo "ERROR: Cannot deploy from branch: $BRANCH"
    exit 1
fi

# Check for uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
    echo "ERROR: Uncommitted changes detected"
    exit 1
fi

echo "Validation passed"
exit 0
```

---

## Customization Ideas

- Add environment selection (staging/production)
- Include Slack notifications
- Add deployment approval workflow
- Include automatic rollback on failure
- Add performance baseline checks
