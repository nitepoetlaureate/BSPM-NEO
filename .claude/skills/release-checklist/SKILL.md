---
name: release-checklist
description: "Generates a GBC-specific pre-release validation checklist covering ROM compilation, MBC bank switching, palette verification, and hardware compatibility."
argument-hint: "[version]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
---

When this skill is invoked:

1. **Read CLAUDE.md** for project context, version information, and GBC target.

2. **Scan the codebase** for outstanding issues:
   - Count `TODO` comments.
   - Count `FIXME` comments (blockers).
   - Check `.gbsproj` for missing references.

3. **Generate the GBC Release Checklist**:

```markdown
## GBC Release Checklist: [Version]
Generated: [Date]

### ROM Compilation & Build Verification
- [ ] Clean ROM build succeeds (.gbc)
- [ ] No compiler warnings (GBDK/GBVM)
- [ ] ROM size within budget (e.g., 1MB, 2MB, 4MB based on MBC)
- [ ] Bank switching (MBC5/MBC3) verified; no bank overflows
- [ ] Save data (SRAM) initialization and persistence tested
- [ ] Build version set in header and player-facing UI

### GBC Hardware Compliance
- [ ] Palette verification: All scenes use 8 or fewer background palettes
- [ ] Sprite limits: Max 40 sprites total, 10 per scanline (no flickering/crashes)
- [ ] Tile limits: Max 256 unique tiles per scene background
- [ ] Audio: 4-channel GBC hardware compatible (no illegal frequencies)
- [ ] Frame Rate: Consistent 60fps (16.6ms) on target hardware/emulators

### Quality Gates
- [ ] Zero Critical bugs (crashes on real hardware)
- [ ] Tested on at least one accurate emulator (BGB, SameBoy, or Emulicious)
- [ ] Tested on real hardware (EverDrive/Flash cart) if available
- [ ] Soak test: 2+ hours continuous play without memory corruption
- [ ] Credits complete and scrolling correctly

### Content & Assets
- [ ] All 4-color indexed PNGs verified for GBC color space
- [ ] No placeholder music or sound effects
- [ ] All player-facing text fits within 20x18 tile grid (or scrolling)
- [ ] All TODO/FIXME in scripts resolved

### Distribution Readiness
- [.] ROM Header: Correct title (15 chars max), Manufacturer code, CGB flag (0x80/0xC0)
- [ ] Manual/Instruction sheet (PDF/TXT) prepared
- [ ] Box art/Digital capsule (GBC style) finalized
- [ ] Legal notices and credits in-game

### Go / No-Go: [READY / NOT READY]
```

4. **Save the checklist** to `production/releases/release-checklist-[version].md`.

5. **Output a summary** to the user with the file path.
