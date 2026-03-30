---
name: asset-audit
description: "Strictly audits GBC game assets using the automated validation script to ensure compliance with hardware limits."
argument-hint: "[category|all]"
user-invocable: true
allowed-tools: Bash, Read
---

# GBC Asset Audit (Automated)

When this skill is invoked:

1. **Execute the validation script**:
   - Run `python3 scripts/validate_assets.py`.
   - This script checks for GBC hardware limitations, naming conventions, and GB Studio requirements.

2. **Analyze the output**:
   - Capture all output from the script, especially warnings and errors.
   - Do NOT perform manual visual checks or manual file scanning.

3. **Output the audit report**:

```markdown
# GBC Asset Audit Report -- [Date]

## Summary
- **Validation Status**: [PASSED / FAILED / WARNINGS]
- **Command Executed**: `python3 scripts/validate_assets.py`

## Validation Output
[Insert the full output from the script here]

## Required Actions
- [List specific assets that failed validation and why, based on script output]
```

### Rules
- **No Manual Audits**: Always rely on `python3 scripts/validate_assets.py`.
- **Hard Block**: Any asset failure reported by the script is a blocker for production.
