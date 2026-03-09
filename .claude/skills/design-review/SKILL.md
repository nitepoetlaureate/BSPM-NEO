---
name: design-review
description: "Reviews a GB Studio design document for 8-bit feasibility, internal consistency, and implementability within GB Studio 3.x hardware limits."
argument-hint: "[path-to-design-doc]"
user-invocable: true
allowed-tools: Read, Glob, Grep
---

When this skill is invoked:

1. **Read the target design document** in full.

2. **Read the master CLAUDE.md** to understand project context (GB Studio 3.x).

3. **Read related design documents** from `design/gdd/`.

4. **Evaluate against the 8-bit Design Document Standard checklist**:
   - [ ] Has Overview section (GB Studio context)
   - [ ] Has Player Fantasy section (8-bit aesthetic)
   - [ ] Has Detailed Rules section (GBVM / Scripting logic)
   - [ ] Has Variable Mapping (8-bit integers 0-255)
   - [ ] Has Formulas section (No floats, only integer math)
   - [ ] Has Edge Cases section (Handling overflow/underflow)
   - [ ] Has Tuning Knobs section (Variable-based tuning)
   - [ ] Has Acceptance Criteria section (Testable in emulator)

5. **Check for 8-bit Internal Consistency**:
   - Do formulas work within the 0-255 range?
   - Is logic based on scripting triggers (On Init, On Interact, On Update)?
   - Are actor/sprite limits per scene respected (max 10 sprites per row, 20 actors per scene)?

6. **Check for Implementability in GB Studio 3.x**:
   - Are rules precise enough to implement with GB Studio script events?
   - Are there "vague" mechanics that would require complex GBVM hacking?
   - Are performance implications (sprite flicker, slowdown) considered?

7. **Check for modernisms (VIOLATIONS)**:
   - **FAIL** if mentions modern 3D rendering, shaders, or VFX.
   - **FAIL** if mentions floating point math.
   - **FAIL** if mentions high-resolution assets or high frame-rate dependencies.

8. **Output the review** in this format:

```
## Design Review: [Document Title] (GB Studio 3.x)

### 8-bit Feasibility: [PASS/FAIL]
[List any hardware constraint violations]

### Completeness: [X/8 sections present]
[List missing sections]

### Logic Issues (8-bit Integer Math)
[List any math or overflow concerns]

### Implementability Concerns
[List any scripting complexity issues]

### Recommendations
[Prioritized list of improvements for GB Studio]

### Verdict: [APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED]
```

9. **Contextual next steps**:
   - If verdict is APPROVED, suggest `/map-systems next` or `/gate-check`.
   - If verdict is NEEDS REVISION, delegate the revision to `systems-designer` for 8-bit math correction or `game-designer` for mechanical simplification.
