---
name: changelog
description: "Auto-generates a GBC-specific changelog from git commits and .gbsproj changes. Produces internal technical notes and player-facing ROM release notes."
argument-hint: "[version|sprint-number]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash
---

When this skill is invoked:

1. **Read the argument** for the target version or sprint number.

2. **Read the git log** since the last tag or release to identify changes in scripts and assets.

3. **Analyze `.gbsproj` changes** to detect:
   - New Scenes added.
   - New Sprites or Backgrounds imported.
   - Scripting logic changes (GBVM/GBS).
   - Music tracks added (.uge).

4. **Categorize changes** for GBC development:
   - **GBC Features**: New gameplay, scenes, or mechanics.
   - **Asset Updates**: New 4-color sprites, backgrounds, or music.
   - **Hardware Optimization**: Bank switching improvements, tile count reductions, palette fixes.
   - **Bug Fixes**: ROM crashes, sprite flickering, script logic errors.
   - **Balance Changes**: Enemy stats, item costs, player movement.

5. **Generate the INTERNAL technical changelog**:

```markdown
# GBC Internal Changelog: [Version]
Date: [Date]

## Hardware & Optimization
- **Bank Switching**: [e.g. Moved scripts to Bank 4 to avoid overflow]
- **Palettes**: [e.g. Fixed palette clash in Scene 'Forest']
- **Tile Counts**: [e.g. Reduced unique tiles in 'Castle' to 240]

## Scripting & GBVM
- [Feature/Fix] -- [Technical description of GBS/GBVM change]
  - Affected Scenes: [Scene Names]

## Assets
- **Sprites**: [Sprite names] added/updated
- **Music**: [Track names] added (.uge)

## Bug Fixes
- [Fixed ROM crash when...]
- [Fixed sprite flickering in...]
```

6. **Generate the PLAYER-FACING ROM notes** (GBC-style):

```markdown
# What's New in [Version] (.gbc)

## New Adventures
- **[Feature Name]**: [Player-friendly description of new content]

## Enhancements
- **Visuals**: [e.g. Improved colors in the Cave area]
- **Audio**: [e.g. New battle theme added]

## Bug Fixes
- Fixed a bug where the game would freeze when [symptom]
- Improved performance on real GBC hardware

---
Thank you for playing our GBC creation!
```

7. **Output both changelogs** to the user.
