---
name: perf-profile
description: "Structured performance profiling for GB Studio projects. Measures GBVM instruction depth, VRAM/Tile usage, and engine constraints."
argument-hint: "[scene-name or 'full']"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash
---
# Code/Quality Purifier: GB Studio Perf Profiler

When this skill is invoked:

1. **Determine scope** from the argument:
   - If a scene name: profile that specific scene.
   - If `full`: run a comprehensive scan of the entire project.

2. **Read project budgets** (from CLAUDE.md or design/engine-constraints.md):
   - **GBVM Instruction Depth**: (Max: 255-512 per script segment).
   - **VRAM/Tile Limits**: (Max: 192 tiles for background, 64-96 for sprites).
   - **Bank Limits**: (Max: 16KB per bank, monitoring script overflows).
   - **Sprite Counts**: (Max: 10 sprites per scanline).

3. **Analyze Implementation**:

   **GBVM Analysis**:
   - Count instructions in scripts (GBScript/GBVM).
   - Flag deep nesting of branching logic.
   - Detect redundant math in `On Update` loops.

   **Graphics/VRAM Analysis**:
   - Analyze background tilesets in `assets/backgrounds/`.
   - Calculate tile usage vs. limit (192 unique tiles).
   - Check sprite sheets in `assets/sprites/` for excessive frame counts.

   **Resource/Bank Analysis**:
   - Check script size in `scripts/GBVM/`.
   - Estimate bank pressure based on script/scene counts.

4. **Generate the profiling report**:

```markdown
## Performance Profile: [Scene/Project]
Generated: [Date]

### Hardware Constraints
| Metric | Budget | Estimated Current | Status |
|--------|--------|-------------------|--------|
| GBVM Depth | [255] | [estimate] | [OK/CRITICAL] |
| Background Tiles | [192] | [count] | [OK/OVER] |
| Sprite VRAM | [96] | [count] | [OK/WARNING] |
| Bank Usage | [16KB] | [estimate] | [OK/FULL] |

### Bottlenecks Identified
| # | Location | Issue | Estimated Impact | Fix Effort |
|---|----------|-------|------------------|------------|
| 1 | [scene:actor] | Deep GBVM Nesting | Lag on trigger | [S/M/L] |
| 2 | [background] | Unique tile overflow | Graphic glitching | [S] |

### Optimization Recommendations
1. **[Title]** — [Optimization]
   - Approach: [Reuse tiles/Extract to custom script/8-bit only math]
   - Impact: [High/Med/Low]

### Quick Wins (< 10 mins)
- [Simple optimization]
```

### Rules
- **No speculative optimization**: Only recommend changes that directly address a budget violation.
- **Hardware First**: Focus exclusively on Game Boy (LR35902) hardware limits.
- **VRAM is King**: Prioritize tile reduction above all visual flourishes.
- **Instruction Depth**: Warn when scripts approach the 255-instruction limit before a mandatory wait/yield.
