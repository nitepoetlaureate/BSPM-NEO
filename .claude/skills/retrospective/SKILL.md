---
name: retrospective
description: "Generates a GB Studio 3.x retrospective by analyzing 8-bit hardware limits, script complexity, and blockers. Produces 8-bit logic insights."
argument-hint: "[sprint-N|milestone-name]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
---

When this skill is invoked:

1. **Read the argument** to determine whether this is a sprint or milestone retrospective.

2. **Read the plan** (Sprint/Milestone). Extract: planned actors, scenes, and variables.

3. **Scan for completed tasks** in GB Studio:
   - ROM compile status.
   - Script trigger completion (On Init, On Interact).
   - Any hardware-related regressions (Sprite flicker, slowdown).

4. **Analyze performance and complexity**:

   **Hardware Metrics**:
   - Actor density per scene (Max 20).
   - Sprite per row (Max 10).
   - Global variable usage (Max 512).

   **Logic Metrics**:
   - **8-bit constraint adherence**: Any floating point math found?
   - Look-up table effectiveness.
   - Script optimization.

5. **Read previous retrospectives** for recurring 8-bit logic issues.

6. **Generate the retrospective**:

```markdown
## Retrospective: [Sprint N / Milestone Name] (GB Studio 3.x)

### 8-bit Metrics

| Metric | Planned | Actual | Hardware Limit |
|--------|---------|--------|----------------|
| Scenes | [X] | [Y] | -- |
| Actors/Scene | [Avg] | [Max] | 20 |
| Sprites/Row | [Avg] | [Max] | 10 |
| Variables | [X] | [Y] | 512 |

### Velocity (GB Studio scripts)

**Trend**: [Increasing / Stable / Decreasing]
[Analysis: Are we getting faster at script-writing or slowed by logic bugs?]

### 8-bit Blockers Encountered

| Blocker | Duration | Resolution | Prevention |
|---------|----------|------------|------------|
| Sprite Flicker | [X] | Actor reduction | Tile-based actors |
| Integer Overflow | [X] | Bitmasking | 8-bit range checks |

### What Went Well
- [Observation on 8-bit logic or aesthetic success]

### What Went Poorly
- [Any 3D/VFX or modern engine mentions (MAJOR REGRESSION)]
- [Floating point math logic errors]

### Action Items for Next Iteration

| # | Action | Owner | Priority |
|---|--------|-------|----------|
| 1 | Optimize math in [file] | **`systems-designer`** | High |
| 2 | Simplify Scene [name] | **`game-designer`** | High |

### Summary (GB Studio Context)
[Assessment: Did we respect the hardware while achieving the fun?]
```

7. **Guidelines**:
- Focus on systemic 8-bit causes.
- Delegate logic optimization to `systems-designer`.
- **FAIL** if any 3D, VFX, or non-8-bit logic is recommended.
