---
name: design-system
description: "Guided, section-by-section GDD authoring for a single GB Studio system. Gathers context, walks through 8-bit constraints, cross-references dependencies, and writes incrementally."
argument-hint: "<system-name> (e.g., 'combat-system', 'inventory', 'dialogue')"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, Task, AskUserQuestion, TodoWrite
---

When this skill is invoked:

## 1. Parse Arguments & Validate

A system name argument is **required**. If missing, fail with:
> "Usage: `/design-system <system-name>` — e.g., `/design-system combat-system`
> Run `/map-systems` first to create the systems index."

Normalize the system name to kebab-case for the filename.

---

## 2. Gather Context (Read Phase)

Read all relevant context **before** asking the user anything.

### 2a: Required Reads

- **Game concept**: Read `design/gdd/game-concept.md`.
- **Systems index**: Read `design/gdd/systems-index.md`.
- **Target system**: Find the system in the index.

### 2b: Dependency Reads

From the systems index, identify Upstream and Downstream dependencies. Extract:
- Key interfaces (Variable ranges 0-255)
- Formulas (8-bit integer math)
- GB Studio scripting constraints (Triggers, Actor limits)

### 2c: Present Context Summary

> **Designing: [System Name] (GB Studio 3.x)**
> - Priority: [from index] | Layer: [from index]
> - Depends on: [list]
> - Variable Constraints: 8-bit Integers (0-255)
> - Hardware Limits: Sprite/Actor density constraints to respect

---

## 3. Create File Skeleton

Immediately create the GDD file with empty section headers using the GB Studio optimized template.

```markdown
# [System Name]

> **Status**: In Design
> **Engine**: GB Studio 3.x
> **Implements Pillar**: [from context]

## Overview

[To be designed]

## Player Fantasy (8-bit Aesthetic)

[To be designed]

## Detailed Design (GBVM / Scripting)

### Core Rules

[To be designed]

### Variable Mapping (8-bit)

[To be designed]

### Interactions (Triggers & Scenes)

[To be designed]

## Formulas (8-bit Integer Math)

[To be designed]

## Edge Cases (Overflow/Underflow)

[To be designed]

## Dependencies

[To be designed]

## Tuning Knobs (Variable Ranges)

[To be designed]

## Visual/Audio Requirements (Palettes/SFX)

[To be designed]

## Acceptance Criteria

[To be designed]
```

---

## 4. Section-by-Section Design

Walk through each section in order.

### Section C: Detailed Design (GBVM / Scripting)

**Goal**: Unambiguous specification for GB Studio scripting.

**Questions to ask**:
- How does this script trigger? (On Init, On Interact, On Update)
- What actors/sprites are involved? (Keep under hardware limits)
- Which global/local variables are used?

**Agent delegation**: Delegate to `game-designer` for mechanical loops and `systems-designer` for variable tracking and 8-bit logic optimization.

---

### Section D: Formulas (8-bit Integer Math)

**Goal**: Every calculation must work within the 0-255 range (or 16-bit where supported by GBVM, but default to 8-bit for simplicity).

**Constraints**:
- No floating point math.
- Use look-up tables or stepped values for curves.
- Handle overflow and underflow explicitly.

**Agent delegation**: Delegate to `systems-designer` to model formulas using only integer arithmetic and bitwise operations.

---

### Section G: Tuning Knobs (Variable Ranges)

**Goal**: Define values that can be changed in the GB Studio UI.

**Questions to ask**:
- Which variables should be "exposed" for tuning?
- What is the max value (0-255)?

---

## 5. Post-Design Validation

### 5a: 8-bit Hardware Check

Verify:
- No mentions of 3D, VFX, or modern shaders.
- Actor counts per scene are reasonable.
- All math is integer-based.

### 5b: Offer Design Review

Use `AskUserQuestion`:
- "Run `/design-review` now to validate the 8-bit logic?"

---

## 6. Specialist Agent Routing

| System Category | Primary Agent | Supporting Agent(s) |
|----------------|---------------|---------------------|
| Combat, health | `game-designer` | `systems-designer` (8-bit formulas) |
| Inventory, items | `systems-designer` | `game-designer` (usage) |
| Dialogue, flags | `game-designer` | `narrative-director` |
| UI (Palettes/Overlays) | `game-designer` | `ux-designer` |

**Agent Directive**: Always assume GB Studio 3.x constraints. No modern vfx.

---

## Collaborative Protocol

1. **Question -> Options -> Decision -> Draft -> Approval** for every section.
2. **Incremental writing**: Each section is written to file immediately.
3. **Hardware Awareness**: Constant checking against 8-bit limits.
