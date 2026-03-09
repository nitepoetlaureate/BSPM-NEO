---
name: code-review
description: "Performs a rigorous quality and architectural review of GB Studio scripts (GBVM/GBScript) and project structure. Checks for script depth, variable efficiency, and bank optimization."
argument-hint: "[path-to-script-or-scene]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash
---

# Code/Quality Purifier: GB Studio Review

When this skill is invoked:

1. **Read the target file(s)** (GBS scripts, GBVM files, or .gbsproj JSON fragments).

2. **Read CLAUDE.md** for project-specific naming conventions and variable ranges.

3. **Evaluate against GB Studio Standards**:
   - [ ] **Script Depth**: Ensure no script exceeds safe GBVM stack limits (instruction depth).
   - [ ] **Variable Usage**: Verify variables are scoped correctly (Local vs Global) and reused where possible to save the 512-variable limit.
   - [ ] **Actor/Trigger Limits**: Confirm scene does not exceed 20 actors or 30 triggers.
   - [ ] **Bank Optimization**: Check that large scripts or data aren't causing bank overflows.
   - [ ] **Logic Verification**: Replace unit test checks with "Logic Injection" readiness (can this script be triggered/tested in isolation via `gb-studio-cli`?).

4. **Check Architectural Compliance**:
   - [ ] **Modular Scripts**: Are common logic blocks extracted into "Custom Scripts"?
   - [ ] **Event Flow**: No deep nesting of "If" statements (prefer early exits or state machine switches).
   - [ ] **Hardware Compatibility**: No 16-bit operations where 8-bit suffices.

5. **Output the review** in this format:

```markdown
## Code Review: [Script/Scene Name]

### GB Studio Compliance: [X/5 passing]
[List violations: e.g., "Script depth exceeds 255 instructions", "Global variable leak"]

### Architecture: [CLEAN / BLOATED / DEBT FOUND]
[Analyze use of Custom Scripts and event flow]

### Resource Efficiency
[VRAM, Variable, and Actor usage analysis]

### Logic Verification Readiness
[Can this be verified via `gb-studio-cli` injection? Yes/No]

### Required Changes
[Must-fix items: e.g., "Flatten nested conditionals in Actor 3"]

### Suggestions
[Optimization tips]

### Verdict: [PURIFIED / NEEDS CLEANUP / REJECTED]
```

### Rules
- Prioritize **hardware limitations** over "clean code" abstractions if they conflict.
- Reject any script that uses "Wait" commands in global/persistent loops without clear exit conditions.
- Flags "On Update" scripts that perform complex math every frame.
