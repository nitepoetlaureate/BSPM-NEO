---
name: asset-audit
description: "Audits GBC game assets (.png, .aseprite, .uge, .gbsproj) for compliance with GBC hardware limitations, naming conventions, and GB Studio requirements."
argument-hint: "[category|all]"
user-invocable: true
allowed-tools: Read, Glob, Grep
---

When this skill is invoked:

1. **Read the GBC asset standards** from `design/art-bible.md` and `CLAUDE.md`.

2. **Scan the target asset directories** using Glob for specific GBC formats:
   - `assets/backgrounds/**/*.png`
   - `assets/sprites/**/*.png`
   - `assets/music/**/*.uge`
   - `assets/data/**/*.gbsproj`
   - `**/*.aseprite` (Source files)

3. **Check naming conventions**:
   - Backgrounds: `bg_[name].png`
   - Sprites: `sprite_[name].png`
   - Music: `music_[name].uge`
   - All files must be lowercase with underscores.

4. **Check GBC Hardware Standards**:
   - **PNG (Backgrounds)**: Must be 160x144 or larger (multiples of 8). Max 256 unique tiles per scene.
   - **PNG (Sprites)**: Must follow GB Studio sprite sheet layouts (16x16 or 16x8 frames).
   - **Color Palette**: 4 colors per palette (indexed). Total 32,768 possible colors, but limited to 8 palettes per background/sprite.
   - **UGE (Audio)**: 4-channel GBC hardware compatible.

5. **Check for orphaned assets** by searching the `.gbsproj` file and scripts for references.

6. **Check for missing assets** by verifying all references in the `.gbsproj` exist in the filesystem.

7. **Output the audit**:

```markdown
# GBC Asset Audit Report -- [Category] -- [Date]

## Summary
- **Total assets scanned**: [N]
- **GBC hardware violations**: [N]
- **Naming violations**: [N]
- **Orphaned assets**: [N]
- **Missing assets**: [N]
- **Overall health**: [GBC COMPLIANT / ISSUES FOUND]

## Hardware Violations (Tile/Sprite/Palette Limits)
| File | Requirement | Actual | Issue |
|------|-------------|--------|-------|

## Naming Violations
| File | Expected Pattern | Issue |
|------|-----------------|-------|

## Format Violations (Only .png, .aseprite, .uge, .gbsproj allowed)
| File | Actual Format | Status |
|------|---------------|--------|

## Orphaned Assets (No .gbsproj references)
| File | Last Modified | Size |
|------|-------------|------|

## Missing Assets (Referenced in .gbsproj but missing)
| Reference Location | Expected Path |
|-------------------|---------------|
```
