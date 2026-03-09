---
name: estimate
description: "Estimates GB Studio task effort by analyzing 8-bit complexity, scripting limits, and historical velocity. Produces a structured 8-bit estimate."
argument-hint: "[task-description]"
user-invocable: true
allowed-tools: Read, Glob, Grep
---

When this skill is invoked:

1. **Read the task description**.

2. **Read CLAUDE.md** for GB Studio 3.x context.

3. **Read relevant design documents** from `design/gdd/`.

4. **Scan the codebase** for GB Studio script complexity:
   - Identify files/scripts that would need to change.
   - Assess actor/sprite counts per scene affected.
   - Identify 8-bit variable usage.

5. **Analyze the following factors (8-bit Context)**:

   **8-bit Complexity**:
   - Number of variables (global vs local).
   - Use of look-up tables vs real-time math.
   - Script trigger complexity (On Init, On Update loops).

   **Hardware Scope**:
   - Scene count, Actor count per scene (max 20).
   - Sprite density (max 10 sprites per row).
   - Palette/Art asset constraints.

   **Risk**:
   - Complex GBVM hacking needed?
   - Any mentions of 3D, high-res VFX, or floating point math (MAJOR RISK/FAIL).

6. **Generate the estimate**:

```markdown
## Task Estimate: [Task Name] (GB Studio 3.x)

### Complexity Assessment (8-bit)

| Factor | Assessment | Notes |
|--------|-----------|-------|
| Variables touched | [Count] | [Global/Local/8-bit range] |
| Scripts modified | [Count] | [On Init, Triggers, etc.] |
| Math complexity | [Low/Med/High] | [Integer-based look-ups needed?] |
| Integration points | [Count] | [Global flag dependencies] |

**Key GB Studio assets affected:**
- `[path/to/scene]` -- [Actor/Trigger changes]
- `[path/to/sprite]` -- [Art/Palette changes]

### Effort Estimate

| Scenario | Days | Assumption |
|----------|------|------------|
| Optimistic | [X] | Standard script events, no GBVM needed |
| Pessimistic | [Z] | Complex variable logic or hardware bottlenecks |

**Recommended budget: [Y days]**

### Confidence: [High / Medium / Low]

**High** -- Standard GB Studio events, within 8-bit limits.
**Low** -- Requires custom GBVM, complex math, or risk of sprite flicker/slowdown.

### Risk Factors (Hardware)

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Sprite Flicker | [High/Med/Low] | Performance | Reduce actor density |
| Variable Overflow | [High/Med/Low] | Logic Crash | 8-bit bitmasking |

### Suggested Breakdown

| # | Sub-task | Estimate | Notes |
|---|----------|----------|-------|
| 1 | Logic Design | [X days] | **Delegate to `systems-designer`** |
| 2 | Script Implementation | [X days] | **Delegate to `game-designer`** |
```

7. **Guidelines**:
- Always assume 8-bit integer logic.
- Round to half-day increments.
- If task mentions 3D or VFX, fail the estimate and flag for scope-check.
