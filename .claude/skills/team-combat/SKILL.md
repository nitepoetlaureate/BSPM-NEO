---
name: team-combat
description: "Orchestrate combat systems team: game-designer + gameplay-programmer + engine-programmer for GBC-optimized physics and mechanics."
argument-hint: "[combat mechanic to design, e.g. 'couch pushing']"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, Bash, Task, AskUserQuestion
---

When this skill is invoked:

1. **Gather context**:
   - Read `design/gdd/game-concept.md`
   - Read `design/gbvm-reference.md`

2. **Orchestrate the Engineering Sandbox**:

### Step 1: Mechanical Design (game-designer)
- Define the puzzle/combat verb.
- Must resolve to 8-bit integer math (0-255).

### Step 2: Assembly Drafting (gameplay-programmer)
- Write raw GBVM assembly commands (`VM_PUSH_CONST`, `VM_IF`).
- Use Local Variables (L0-L7) to save RAM.

### Step 3: Hardware Audit (engine-programmer)
- **CRITIC:** Interrogate the assembly. Reject if it uses floats or excessive global vars.

### Step 4: Integration (tools-programmer)
- Inject logic into `EVENT_GBVM_SCRIPT` blocks in `project.gbsproj`.
