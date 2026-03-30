---
name: export-optimize
description: "Handles GBVM assembly export and stack optimization for Game Boy hardware efficiency."
argument-hint: "[export|optimize]"
user-invocable: true
allowed-tools: Bash, Read, Write, Glob
---
# GBVM: Export & Optimize

When this skill is invoked:

1. **Request Data Export**:
   - Ask the user to manually trigger 'Export Project Data' within GB Studio.
   - This ensures the latest `.s` GBVM assembly files are generated.

2. **Read Assembly Files**:
   - Navigate to `build/src/src/data/` and read the `.s` files.
   - Use Glob to find relevant script data files.

3. **Perform Stack Optimization**:
   - Analyze `VM_PUSH` and `VM_POP` instructions.
   - Ensure the stack is perfectly balanced within each script block.
   - Identify redundant push/pop pairs and propose removals.

4. **Return Optimized Code**:
   - Provide the user with the optimized GBVM assembly snippets.
   - Explain why the optimization is hardware-strict (e.g., saving stack space, cycles).

```markdown
# GBVM Optimization Report -- [File Name]

## Stack Health
- **Total Pushes**: [N]
- **Total Pops**: [N]
- **Stack Balance**: [BALANCED / LEAK DETECTED]

## Optimization Opportunities
| Original Code | Optimized Code | Impact |
|---------------|----------------|--------|
| `VM_PUSH 1` | (removed redundant) | Saved cycles |

## Final Optimized Snippet
[Optimized Assembly Code]
```

### Rules
- **Stack Balance**: Every `VM_PUSH` must have a corresponding `VM_POP`.
- **Target Files**: Only analyze files within `build/src/src/data/`.
- **No Manual Edits**: Present optimized code back to the user for implementation.
