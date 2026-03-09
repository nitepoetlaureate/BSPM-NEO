---
name: project-stage-detect
description: "Automatically analyzes GB Studio project state, detects development stage, and identifies gaps in design, assets, and ROM build readiness."
argument-hint: "[no arguments]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash
---
# Code/Quality Purifier: GB Studio Stage Detect

When this skill is invoked:

1. **Scan GB Studio Project Structure**:
   - **Project File**: Search for `*.gbsproj` at root or in subdirectories.
   - **Assets**: Count backgrounds in `assets/backgrounds/`, sprites in `assets/sprites/`, and music in `assets/music/`.
   - **Scripts**: Scan for custom scripts and GBVM files in `scripts/` or project JSON.
   - **Design Docs**: Check for `design/gdd/game-concept.md`.

2. **Classify Project Stage**:
| Stage | Indicators |
|-------|------------|
| **Concept** | No `game-concept.md`, no `.gbsproj` |
| **Asset Dev** | `.gbsproj` exists, < 5 backgrounds, < 5 sprites |
| **Logic/Scripting** | 5+ backgrounds, scripts in progress, no ROM build |
| **Beta/ROM** | 10+ scenes, ROM builds successfully via `gb-studio-cli` |
| **Release Ready** | Full `localize` coverage, passed `perf-profile` |

3. **Identify Gaps**:
   - "I found a `.gbsproj` but no `assets/backgrounds/`. Have you imported your tilesets?"
   - "You have 20 scenes but no `perf-profile` run. We should check GBVM instruction depth."
   - "No `assets/music/` found. Is the soundtrack planned?"

4. **Generate Stage Report**:
```markdown
# GB Studio Project Stage Analysis

**Date**: [date]
**Stage**: [Concept/Asset Dev/Logic/Beta/Release Ready]

## Asset Inventory
- Backgrounds: [N]
- Sprites: [N]
- Music Tracks: [N]
- Custom Scripts: [N]

## Build Status
- ROM Build: [Succeeds/Fails/Untested]
- `gb-studio-cli` readiness: [OK/Missing]

## Gaps Identified
1. [Gap Description]

## Recommended Next Steps
[Priority-ordered list]
```

### Rules
- If no `.gbsproj` is found, default recommendation is to initialize the project via GB Studio.
- Prioritize asset organization (naming conventions) as a "Quality Purifier" check.
