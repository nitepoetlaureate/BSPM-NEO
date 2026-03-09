---
name: tech-debt
description: "Track and prioritize technical debt in GB Studio projects. Focuses on unoptimized tilesets, redundant GBVM scripts, and bank overflows."
argument-hint: "[scan|add|prioritize|report]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
---
# Code/Quality Purifier: GB Studio Tech Debt Register

When this skill is invoked:

1. **Scan Subcommand**:
   - **TODO/FIXME**: Scan scripts and project JSON for developer notes.
   - **Tile Duplication**: Identify backgrounds with similar tilesets that could be merged.
   - **Variable Bloat**: Find global variables that aren't used or could be local.
   - **Instruction Depth**: Detect scripts nearing the 255-instruction limit.
   - **Bank Overflows**: Find large scripts that could be broken up.

2. **Categorize findings**:
   - **Hardware Debt**: Violates GB Studio limits (tiles, sprites, actors).
   - **Logic Debt**: Complex/redundant GBVM scripts.
   - **Asset Debt**: Non-optimized images (non-2-bit, non-tileset-friendly).
   - **Variable Debt**: Wasteful usage of the 512-variable global limit.

3. **Report Status**:
```markdown
## GB Studio Tech Debt Register
Total items: [N] | Debt Status: [HEALTHY/WARNING/CRITICAL]

| ID | Category | Description | Effort | Impact |
|----|----------|-------------|--------|--------|
| TD-001 | Hardware | 200+ unique tiles in Scene A | S | High |
| TD-002 | Variable | 50 unused global variables | M | Low |
```

### Rules
- Hardware Debt is always prioritized over Logic Debt.
- Any scene with > 192 background tiles is a "Critical" debt item.
- Any script with > 255 instructions without a `Wait` is a "Critical" debt item.
