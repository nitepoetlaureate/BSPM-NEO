---
name: code-review
description: "Performs a hardware-strict quality and architectural review focusing on GBVM stack balancing and 8-bit constraints."
argument-hint: "[path-to-script-or-scene]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash
---

# GBVM Code Review: GBC Hardware Compliance

When this skill is invoked:

1. **Focus on GBVM Stack Balancing**:
   - Every `VM_PUSH` MUST have a matching `VM_POP`.
   - Any stack leak is an immediate failure.

2. **Strict 8-bit Enforcement**:
   - Verify all variables are 8-bit integers (0-255).
   - Check all C-engine overrides for compliance with the GBC's 8-bit architecture.

3. **Reject Floating Point Math**:
   - **FAIL** any script or override that includes floating point operations (`float`, `double`).
   - Formulas must be converted to 8-bit integer look-up tables or scaled integer math.

4. **Output the Review**:

```markdown
## Code Review: [Script/Override Name]

### GBVM Stack Balancing: [BALANCED / LEAK]
[Detail any mismatched PUSH/POP pairs]

### Hardware Constraints (8-bit): [PASSED / FAILED]
- **Variable Range**: [All are 0-255 / Out of range found]
- **C-Engine Overrides**: [Strictly 8-bit / Modern artifacts found]

### Mathematical Integrity: [NO FLOATS / FLOAT DETECTED]
- **Floating Point Math**: [None / FOUND - MUST REWRITE]

### Required Changes
[List specific lines for stack repair or float removal]

### Verdict: [PURIFIED / REJECTED]
```

### Rules
- **Stack Integrity is First**: Never approve a script with an unbalanced stack.
- **Hardware-Strict**: Prioritize Game Boy (LR35902) limitations over any modern clean-code convention.
- **Float-Free Zone**: Any mention of floating point is an automatic `REJECTED` verdict.
