---
name: gate-check
description: "Validate GB Studio readiness to advance between development phases. Produces a verdict based on 8-bit hardware limits and 3.x standards."
argument-hint: "[target-phase: systems-design | technical-setup | pre-production | production | polish | release]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash, Write
---

# GB Studio Phase Gate Validation

This skill validates readiness to advance through GB Studio 3.x development. It checks for 8-bit constraints, actor limits, and 3.x scripting artifacts.

## Production Stages (7)

1. **Concept** — 8-bit concept doc
2. **Systems Design** — 8-bit variable mapping, scene flow
3. **Technical Setup** — GB Studio 3.x config
4. **Pre-Production** — Emulator-based core loop prototyping
5. **Production** — Feature development (Actors, Scenes, Scripts)
6. **Polish** — Performance (Sprite flicker removal), Playtesting
7. **Release** — ROM export, GB/GBC certification

---

## 1. Phase Gate Definitions

### Gate: Concept → Systems Design
- [ ] `design/gdd/game-concept.md` exists and defines GB Studio 3.x as engine.
- [ ] Pillars respect 8-bit limitations.

### Gate: Systems Design → Technical Setup
- [ ] `design/gdd/systems-index.md` exists with 8-bit variable tracking.
- [ ] At least 1 GDD in `design/gdd/` with **8-bit integer formulas**.

### Gate: Technical Setup → Pre-Production
- [ ] GB Studio 3.x project initialized.
- [ ] Asset directories (`assets/sprites`, `assets/backgrounds`) exist with 4-color palettes.
- [ ] **FAIL** if any 3D, VFX, or modern engine references found.

### Gate: Pre-Production → Production
- [ ] Prototype scenes validate core loop in GB emulator.
- [ ] **Delegate to `game-designer` and `systems-designer`** for logic/loop validation.
- [ ] Scene/Actor counts are within hardware limits (20 Actors/Scene, 10 Sprites/Row).

### Gate: Production → Polish
- [ ] All scripts implemented (On Init, On Interact, On Update).
- [ ] ROM compiles cleanly in GB Studio.
- [ ] No 16/32-bit floating point math used in any script logic.

---

## 2. Run the Gate Check

- **Artifacts**: Verify `.gbsproj` and asset palettes.
- **8-bit Logic**: Grep for any non-integer math.
- **Hardware**: Check scene actor counts.

---

## 3. Verdict Output

```
## Gate Check: [Current Phase] → [Target Phase] (GB Studio 3.x)

### 8-bit Hardware Readiness: [X/Y present]
- [x] Backgrounds (4-color palettes)
- [x] Actors (Scene limits respected)
- [ ] Logic (8-bit Integer formulas missing in [file])

### Blockers
1. **Modern VFX detected** — Remove references to shaders/3D.
2. **Floating point math** — Rewrite formulas to use 8-bit integer look-ups.

### Verdict: [PASS / CONCERNS / FAIL]
```

---

## Collaborative Protocol

1. **8-bit Priority**: Hardware limits are the ultimate arbiter.
2. **"May I write this report?"** before final write.
3. **Delegate complex logic reviews to Sandbox 2 agents.**
