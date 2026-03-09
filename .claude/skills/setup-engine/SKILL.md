---
name: setup-engine
description: "Configure the project for Game Boy Color (GBC) development. Pins the GB Studio version and GBC architecture in CLAUDE.md, and populates engine reference docs for GBVM/GBS."
argument-hint: "[GB Studio version] or no args for latest"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, WebSearch, WebFetch, Task
---

When this skill is invoked:

## 1. Parse Arguments

- **Version provided**: `/setup-engine 3.1.0` — pins specific GB Studio version.
- **No args**: `/setup-engine` — defaults to latest stable GB Studio (3.x).

---

## 2. GBC Architecture Enforcement

This project is strictly for **Game Boy Color (GBC)**. All engine configurations must support:
- **CPU**: LR35902 (Z80-hybrid) @ 4.19/8.38 MHz.
- **Memory**: 32KB System RAM, 32KB Video RAM.
- **Display**: 160x144 pixels, 56 simultaneous colors from a palette of 32,768.
- **Audio**: 4-channel stereo (2 pulse, 1 wave, 1 noise).

---

## 3. Look Up GB Studio Version

- Use WebSearch to find the latest stable GB Studio release if not provided.
- Confirm with the user: "The latest stable GB Studio is [version]. Setting up for GBC ROM compilation."

---

## 4. Update CLAUDE.md Technology Stack

Read `CLAUDE.md` and update the Technology Stack section for GBC/GB Studio:

```markdown
- **Engine**: GB Studio [version]
- **Architecture**: Game Boy Color (GBC)
- **Language**: GBVM (Game Boy Virtual Machine), GBS Script, C (via GBDK-2020 for plugins)
- **Build System**: GB Studio Compiler (ROM Compilation)
- **Primary Target**: .gbc ROM file
- **Asset Pipeline**: 4-color Indexed PNGs (Backgrounds/Sprites), .uge (Music), .aseprite (Source)
```

---

## 5. Populate Technical Preferences

Update `.claude/docs/technical-preferences.md` with GBC-specific constraints:

### Naming Conventions
- Sprites: `sprite_[name].png`
- Backgrounds: `bg_[name].png`
- Scripts: `script_[name].gbs`
- Music: `music_[name].uge`

### Performance Budgets
- Frame Budget: 16.6ms (60fps target).
- Sprite Limit: 40 total, 10 per scanline.
- Memory: Respect bank switching (MBC5 preferred).

---

## 6. Populate Engine Reference Docs

Create or update `docs/engine-reference/gbstudio/VERSION.md`:

```markdown
# GB Studio — GBC Reference

| Field | Value |
|-------|-------|
| **Engine Version** | [version] |
| **Architecture** | Game Boy Color |
| **Primary Target** | ROM (.gbc) |
| **Build System** | GBS Compiler |
```

---

## 7. Output Summary

After setup is complete, output:

```
GBC Engine Setup Complete
=========================
Engine:          GB Studio [version]
Architecture:    Game Boy Color (GBC)
Build Target:    ROM Compilation (.gbc)
CLAUDE.md:       [updated]
Tech Prefs:      [GBC Optimized]

Next Steps:
1. Ensure assets are in 4-color indexed PNG format.
2. Run /asset-audit to verify GBC compatibility.
3. Use /prototype to script GBVM events.
```

---

## Guardrails

- NEVER suggest modern engines (Unity, Godot, Unreal).
- NEVER suggest non-ROM targets (Steam, Web-only, Mobile-native).
- Ensure all build instructions focus on ROM compilation for GBC hardware/emulators.
