---
name: scope-check
description: "Analyze a GB Studio feature or sprint for scope creep. Flags 8-bit hardware violations, 3D/VFX bloat, and recommends cuts."
argument-hint: "[feature-name or sprint-N]"
user-invocable: true
allowed-tools: Read, Glob, Grep
---

When this skill is invoked:

1. **Read the original plan** — Find the relevant document (GDD or Sprint plan).

2. **Read the current state** — Check implementaton in GB Studio:
   - Scan `src/` (or script files) for new triggers/actors.
   - Read for "vague" additions that exceed 8-bit limits.

3. **Compare original vs current scope**:

   ```markdown
   ## Scope Check: [Feature/Sprint Name] (GB Studio 3.x)

   ### Original Scope
   [List of items]

   ### Current Scope
   [List of current items]

   ### Scope Additions (not in original plan)
   | Addition | 8-bit Feasibility | Effort |
   |----------|-------------------|--------|
   | [item]   | [Yes/No]          | [S/M/L] |

   ### Violations Found (Scope Creep)
   - **FAIL**: Mentions of modern VFX or 3D rendering.
   - **FAIL**: Floating point math or 16/32-bit complex logic.
   - **FAIL**: High actor density beyond scene limits.

   ### Bloat Score
   - Original items: [N]
   - Current items: [N]
   - Items added: [N] (+[X]%)

   ### Risk Assessment
   - **Performance Risk**: [Low/Medium/High] — (e.g. Sprite flicker, slowdown)
   - **Memory Risk**: [Low/Medium/High] — (e.g. Variable count overflow)

   ### Recommendations
   1. **Cut**: Any 3D/VFX or non-8-bit logic additions.
   2. **Simplify**: Move complex math to 8-bit integer look-up tables.
   3. **Consult `systems-designer`**: For 8-bit logic optimization.
   ```

4. **Output the verdict**:
   - **On Track**: Scope within limits.
   - **Out of Control**: >25% scope increase or any non-8-bit hardware additions.
