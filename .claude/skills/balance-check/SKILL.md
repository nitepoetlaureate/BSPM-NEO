---
name: balance-check
description: "Analyzes game balance for GB Studio projects. Focuses on 8-bit math constraints, variable limits, and Game Boy progression curves."
argument-hint: "[system-name|path-to-data-file]"
user-invocable: true
allowed-tools: Read, Glob, Grep
---
# Code/Quality Purifier: GB Studio Balance Check

When this skill is invoked:

1. **Identify Balance Domain**: Combat, Economy, or Progression.

2. **Read GB Studio Data**: Project JSON, variables, and design docs.

3. **Check 8-bit/16-bit Constraints**:
   - **Math Overflow**: Identify variables that might exceed 255 (8-bit) or 65,535 (16-bit).
   - **Precision**: Flag calculations that require floating-point (not natively supported).
   - **Variable Efficiency**: Check if the 512-variable limit is being approached.

4. **Perform Analysis**:
   - **Combat**: Analyze enemy HP vs player Damage at different levels.
   - **Economy**: Map item costs vs player gold accumulation (8-bit limit).
   - **Progression**: Plot XP curve vs. variable capacity.

5. **Output Balance Report**:
```markdown
## Balance Check: [System Name]

### Hardware Constraints Analyzed
- 8-bit Variable Limit: [Check]
- 16-bit Variable Limit: [Check]
- Script Math Complexity: [Check]

### Outliers Found
| Item | Issue | Suggested Adjustment |
|------|-------|----------------------|
| Sword | Damage 256 | Reduce to 255 or use 16-bit |

### Progression Analysis
[Graph description showing XP curve health within variable bounds]

### Verdict: [BALANCED / OVERFLOW RISK / CRITICAL IMBALANCE]
```

### Rules
- If a value exceeds 255, **must** recommend 16-bit variable handling.
- Reject balance designs that require floating-point math without a lookup table (LUT) implementation.
- Any mechanic that requires more than 50 global variables for a single system is "Poor Architecture".
