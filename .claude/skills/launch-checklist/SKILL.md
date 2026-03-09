---
name: launch-checklist
description: "GBC-specific launch readiness validation covering ROM header, hardware compatibility, manual/box art, and final ROM sign-off."
argument-hint: "[launch-date or 'dry-run']"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
---

When this skill is invoked:

1. **Read CLAUDE.md** for GBC tech stack and version.

2. **Scan codebase health**:
   - Count `TODO`, `FIXME`, `HACK` comments.
   - Check for placeholder assets (.png, .aseprite, .uge).
   - Verify `.gbsproj` for final scenes and scripts.

3. **Generate the GBC Launch Checklist**:

```markdown
# GBC Launch Checklist: [Game Title]
Target Launch: [Date or DRY RUN]
Generated: [Date]

---

## 1. ROM & Technical Readiness

### ROM Build Health
- [ ] Clean GBC ROM build succeeds (.gbc)
- [ ] Zero compiler warnings (GBVM/GBDK)
- [ ] ROM size within target MBC limits (e.g., 2MB MBC5)
- [ ] ROM Header: 15-char Title, Manufacturer Code, CGB Flag, Licensee Code
- [ ] Global Checksum: Correctly calculated in ROM header
- [ ] Save Data (SRAM): Tested for persistence across power cycles

### Hardware Compatibility
- [ ] Verified on accurate emulators (BGB, SameBoy, Emulicious)
- [ ] Verified on real GBC hardware (via flash cart)
- [ ] Verified on Game Boy Advance (backwards compatibility mode)
- [ ] No illegal opcodes or memory access violations

---

## 2. GBC Content & Quality

### Assets & Hardware Limits
- [ ] All 4-color indexed PNGs finalized (no placeholders)
- [ ] Palette limits: Max 8 BG palettes, 8 Sprite palettes per scene
- [ ] Tile limits: Max 256 unique background tiles per scene
- [ ] Sprite limits: Max 40 total, 10 per scanline (no excessive flickering)
- [ ] Audio: 4-channel GBC hardware compatible music (.uge) and SFX

### Quality Assurance
- [ ] Full playthrough from start to finish (no softlocks)
- [ ] All TODO/FIXME comments resolved or documented
- [ ] Performance: Stable 60fps (16.6ms) in all gameplay scenes
- [ ] Credits: All contributors listed and legible on 160x144 screen

---

## 3. Distribution & Legal

### Metadata & Physicals
- [ ] Instruction Manual (PDF/TXT) prepared for players
- [ ] Digital Box Art (GBC style) finalized
- [ ] Store page (e.g. Itch.io) copy finalized and proofread
- [ ] Pricing/Distribution plan confirmed

### Legal
- [ ] Credits and copyright notice in ROM header/title screen
- [ ] Third-party tools (GB Studio, GBDK, UGE) attributed
- [ ] No unlicensed IP or assets in the final ROM

---

## 4. Operations

### Post-Launch & Support
- [ ] Bug tracking system ready for player reports
- [ ] Known issues list prepared
- [ ] Patching pipeline tested (can rebuild and re-distribute ROM)

---

## Go / No-Go Decision

**Overall Status**: [READY / NOT READY]

### Sign-Offs Required
- [ ] Creative Director (Experience)
- [ ] Technical Lead (ROM Integrity)
- [ ] QA Lead (Hardware Compatibility)
```

4. **Save the checklist** to `production/releases/launch-checklist-[date].md`.

5. **Output a summary** to the user.
