---
name: team-level
description: "Orchestrate level design team: level-designer + narrative-director + art-director + engine-programmer + qa-tester for complete GBC scene creation."
argument-hint: "[level name or area to design]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, Bash, Task, AskUserQuestion
---

When this skill is invoked:

1. **Gather context**:
   - Read `design/gdd/game-concept.md`
   - Read `design/art-bible.md`
   - Read `design/gbvm-reference.md`

2. **Orchestrate the level design team** in the Engineering Sandbox:

### Step 1: Narrative & World (narrative-director)
- Define the GBC scene purpose (what happens in this 160x144 space?)
- Write dialogue (Max 18 chars x 3 lines).

### Step 2: Layout & Constraints (level-designer + engine-programmer)
- Design the 8x8 tile grid layout.
- **Engine Audit:** Verify unique tile count is < 192.
- Ensure actor count is < 10.

### Step 3: Visuals (art-director + technical-artist)
- Call HuggingFace for RetroDiffusion background.
- **Aseprite CLI:** Index to 4-color palette and save to `assets/backgrounds/`.

### Step 4: Logic Injection (tools-programmer)
- Inject the scene JSON into `project.gbsproj` using Python tools.

### Step 5: QA (qa-tester)
- Compile ROM via `gbstudio build` and launch OpenEmu.
