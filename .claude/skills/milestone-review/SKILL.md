---
name: milestone-review
description: "Evaluates GBC development milestone progress. Hard-blocks on any asset validation warnings."
argument-hint: "[milestone-name|current]"
user-invocable: true
allowed-tools: Read, Bash, Write
---

# GBC Milestone Review

When this skill is invoked:

1. **Automated Asset Check**:
   - Execute `python3 scripts/validate_assets.py`.
   - **Hard Block**: If ANY warnings or errors are returned, the milestone MUST NOT pass.

2. **Quality Metrics (8-bit Hardware Focus)**:
   - Verify scene actor counts (max 10).
   - Verify global variables (max 512).
   - Ensure GBVM stack is balanced.

3. **Generate the Review**:

```markdown
# Milestone Review: [Milestone Name]

## GBC Hardware Readiness: [PASSED / FAILED]
- **Asset Validator**: [No Warnings / WARNINGS DETECTED]
- **Actor Limits**: [Max 10 per scene / VIOLATION FOUND]
- **Variable Usage**: [Count / Over 512]

## Quality Metrics
- **Stack Integrity**: [Balanced / Leaks Found]
- **Math Integrity**: [All 8-bit / FLOATS DETECTED]

## Risk Assessment
- **Hardware Bottlenecks**: [List any scenes near actor limits]

## Go/No-Go Assessment
**Recommendation**: [GO / NO-GO]

**Rationale**: [Every asset warning must be resolved for a GO.]
```

### Rules
- **Asset Validation is King**: `python3 scripts/validate_assets.py` output is the primary arbiter of quality.
- **Hardware-Strict**: Any 3D, VFX, or non-8-bit logic is a failure.
- **Record in Mycelium**: Save the review outcome to the Mycelium state.
