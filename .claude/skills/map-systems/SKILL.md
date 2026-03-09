---
name: map-systems
description: "Decompose a GB Studio game concept into individual systems, map dependencies, prioritize 8-bit design order, and create the systems index."
argument-hint: "[optional: 'next' to pick highest-priority undesigned system]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, AskUserQuestion, TodoWrite
---

When this skill is invoked:

## 1. Phase 1: Read Concept (GB Studio Context)

Read the game concept. **Required**: `design/gdd/game-concept.md`.

## 2. Phase 2: Systems Enumeration (Collaborative)

Identify systems relevant to GB Studio 3.x.

### Step 2a: Extract Explicit Systems (8-bit)

Scan for mechanics mentioned:
- Dialogue system (Flags, Text boxes)
- Combat (HP variables, Palette swaps)
- RPG stats (8-bit integer variables)

### Step 2b: Identify Implicit Systems

For each system, identify the **8-bit hidden systems** it implies:

- "Inventory" implies: Variable-based slots (0-255), Item database (Scene-less logic), Menu UI (Overlay scenes).
- "Combat" implies: 8-bit damage formulas, Actor health bars (Sprite-based UI), Scene transitions, Turn-based scripts.
- "World map" implies: Scene triggers, Variable-based coordinates, Palette-based weather/time.

Explain how these systems must fit within GB Studio script/actor limits.

---

## 3. Phase 3: Dependency Mapping

Map how systems depend on each other for GB Studio.

### Step 3a: Map Dependencies (8-bit)

Heuristics:
- **Global Variable dependencies**: System B uses variables initialized by System A.
- **Scene-to-Scene dependencies**: Transitions between Scenes.
- **Script-based dependencies**: Scripts calling other scripts (Custom events).

### Step 3b: Sort by Dependency Order (GB Studio layers)

1. **Global Vars**: Zero dependencies (Designed first).
2. **Foundation**: Input/Movement.
3. **Core**: Scene logic.
4. **Meta**: Save/Load, Menus.

---

## 4. Phase 4: Priority Assignment

Prioritize based on MVP functionality (the first 1-2 scenes).

---

## 5. Phase 5: Create Systems Index (Write)

Create `design/gdd/systems-index.md` with:
- System enumeration table.
- 8-bit logic complexity estimates.
- GB Studio actor/scene counts where applicable.

---

## 6. Phase 6: Hand Off to /design-system

Invoke `/design-system [system-name]` for the next system.

**Delegate to `game-designer` and `systems-designer`** to validate system boundaries against 8-bit memory limits and GB Studio scripting performance before final index creation.

---

## Collaborative Protocol

1. **8-bit Filtering**: Always screen systems for feasibility in GB Studio 3.x.
2. **Incremental Writing**: Update the index as systems are designed.
3. **Hardware-First Mapping**: Priorities based on what can be prototyped in the emulator.
