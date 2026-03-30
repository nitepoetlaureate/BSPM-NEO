---
name: playtest-report
description: "Triggers the GB Studio playtest environment and coordinates human-in-the-loop playtest feedback."
argument-hint: "[new|analyze]"
user-invocable: true
allowed-tools: Bash, Read, Write
---
# GBC Playtest Coordinator

When this skill is invoked:

1. **Trigger the Playtest Build**:
   - Execute `./playtest.sh`. This will build and serve the project for the browser or emulator.

2. **Engage the Human Tester**:
   - Ask the user to play the build in their browser/emulator.
   - Request specific feedback on Game Boy hardware feel and ergonomics.

3. **Generate/Analyze the Report**:
   - Once the user reports back, summarize the findings into the following structure.

```markdown
# Playtest Report: [Build/Date]

## Playtest Execution
- **Command**: `./playtest.sh`
- **Platform**: [Browser / Emulator / Original Hardware]

## Human Feedback Summary
- **Visual Performance**: [Flicker/Corruption reported by user]
- **Gameplay Feel**: [Ergonomics and responsiveness feedback]

## Hardware Verification
- **Sprite Limits**: [Are more than 10 sprites on a row causing flicker?]
- **Tile Memory**: [Reported graphic glitches during transitions]

## Verdict
- **Ready for Release?** [YES / NO / NEEDS POLISH]
```

### Rules
- **Human-in-the-Loop**: Agents do not "play" the game; they trigger the build and ask the user for observations.
- **Hardware Focus**: Prioritize feedback related to GBC hardware constraints over general aesthetics.
