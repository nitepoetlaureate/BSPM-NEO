---
name: reverse-document
description: "Generates design or architecture documents from existing GB Studio scripts, project JSON, and GBVM files. Works backwards to create missing documentation."
argument-hint: "<type> <path> (e.g., 'design scripts/' or 'architecture project.gbsproj')"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
---
# Code/Quality Purifier: GB Studio Reverse Documentation

When this skill is invoked:

1. **Analyze GB Studio Implementation**:
   - **GDD (Design)**: Extract mechanics, state machines, and event flows from project JSON/scripts.
   - **Architecture**: Map out global variables, custom script usage, and scene transitions.
   - **Concept**: Analyze a prototype's implementation to extract the "why" and "how".

2. **Extract Key Values**:
   - Locate variable assignments (e.g., `$Global_PlayerHP = 10`).
   - Identify branching logic complexity (GBVM instruction depth).
   - Trace event triggers (Actor interact, Trigger enter, Scene init).

3. **Ask Intent Questions**:
   - "I see a loop that checks `$Var_Energy` every frame. Was this for a cooldown or a UI update?"
   - "You used a custom script for NPC dialogue. Is this the standard for all NPCs?"

4. **Draft Document using GB Studio context**:
```markdown
# [System Name] Design Doc

> **Note**: This document was reverse-engineered from the GB Studio implementation.

### Mechanics (Scripts)
[Extracted logic: e.g., "3-hit combo implemented via variable switch"]

### Variables & State
[List key globals/locals used]

### Constraints & Performance
- GBVM Depth: [estimate]
- Scene Actors: [count]
```

### Rules
- Never just list scripts; explain the **mechanic** they implement.
- Flag "magic numbers" found in scripts for documentation.
- **Strictly for GB Studio**: Do not generate documentation for non-GBS codebases.
