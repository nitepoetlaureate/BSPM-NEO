---
name: playtest-report
description: "Generates a structured playtest report for GB Studio projects. Analyzes playtest notes, focusing on hardware-accurate behavior and Game Boy ergonomics."
argument-hint: "[new|analyze path-to-notes]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
---
# Code/Quality Purifier: GB Studio Playtest Report

When this skill is invoked with `new`, generate this GB Studio specific template:

```markdown
# Playtest Report: [Build Name]

## Session Info
- **Date**: [Date]
- **ROM Build**: [Version/Commit]
- **Platform**: [Original Hardware / Analogue Pocket / Emulator]
- **Tester**: [Name/ID]
- **Input Method**: [Original GB / SNES Controller / Keyboard]

## Hardware Verification
- **Visual Artifacts?** [Yes/No] (Flicker, tile corruption)
- **Audio Lag?** [Yes/No]
- **Input Responsiveness?** [Yes/No/Sluggish]

## First Impressions (3-5 mins)
- **Goal Clear?** [Yes/No]
- **Text Readability?** [Good/Bad] (Small screen check)
- **Emotional Response**: [Engaged/Confused/Frustrated]

## Gameplay Flow
### What worked
- [Observation]

### GB Specific Pain Points
- **Flicker on too many sprites**: [Yes/No]
- **Navigation in small spaces**: [Issue]
- **Menu navigation speed**: [Issue]

## Bugs (Hardware vs Emulator)
| # | Bug | Severity | Found on Hardware? |
|---|-----|----------|-------------------|
| 1 | Tile corruption on screen transition | High | Yes |

## Overall Assessment
- **Difficulty**: [Too Easy / Just Right / Too Hard]
- **Pacing**: [Good / Laggy / Too Fast]
- **Verdict**: [READY FOR RELEASE / NEEDS POLISH / UNSTABLE]

## Top 3 Priorities
1. [Highest priority]
```

When invoked with `analyze`, process raw notes into this format, prioritizing hardware-specific observations over general gameplay feedback.
