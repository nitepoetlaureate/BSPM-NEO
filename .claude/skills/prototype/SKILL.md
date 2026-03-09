---
name: prototype
description: "Rapid prototyping workflow for GB Studio. Produces throwaway logic/assets to test a Game Boy mechanic and builds a ROM for validation."
argument-hint: "[concept-description]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
---
# Code/Quality Purifier: GB Studio Prototyper

When this skill is invoked:

1. **Define Core Question**: What mechanic or constraint is being tested (e.g., "Can we handle 8 active actors in a 320x320 scene?")?

2. **Setup Isolation**: Create a prototype directory in `prototypes/[concept-name]/`.

3. **Implement Minimum Viable Logic**:
   - Use placeholder tilesets/sprites.
   - Focus on GBVM script efficiency.
   - **No Production Imports**: Keep prototype code separate.

4. **Build the ROM**:
   **Mandatory Command**: `npx gb-studio-cli build BARRY-SHARP-PRO-MOVER-GBC build --type rom`
   (If this fails, analyze the GBVM output for errors).

5. **Test and Observe**:
   - Playtest using `./playtest.sh`.
   - Monitor for tile flicker or input lag on the prototype ROM.

6. **Generate the Prototype Report**:
```markdown
## Prototype Report: [Concept]

### Question
[Hypothesis]

### Results
- Build Status: [Succeeds/Fails]
- Build Command: `npx gb-studio-cli build BARRY-SHARP-PRO-MOVER-GBC build --type rom`
- Observed Performance: [Flicker/Depth/Lag]

### Recommendation: [PROCEED / PIVOT / KILL]
[Reasoning based on ROM performance]
```

### Rules
- If the build takes more than 5 minutes, the prototype is too complex.
- **Never** refactor prototype code into production. Rewrite it according to `code-review` standards if the concept proceeds.
- Mandatory use of `gb-studio-cli` for all ROM builds.
