# BARRY SHARP'S PRO MOVER -- Studio OS (GBC Edition)

Indie game development managed through 48 coordinated AI agents, hyper-specialized for Game Boy Color hardware constraints.

## Technology Stack

- **Engine**: GB Studio 3.x
- **Architecture**: Game Boy Color (GBC) / DMG
- **Language**: GBVM (Game Boy Virtual Machine), SM83 Assembly, C (GBDK-2020)
- **Primary Target**: .gbc ROM
- **Asset Pipeline**: 4-color Indexed PNGs, .aseprite source files, .uge music
- **Automation**: FastAPI Backend (Oracle VPS), npx gb-studio-cli (Mac Mini)

## Collaboration Protocol

**USER-DRIVEN COLLABORATION (CRITICAL)**
Every task MUST follow the Actor-Critic loop:
1. **Request**: User provides goal in Discord/Terminal.
2. **Draft**: Specialist agent (Actor) creates logic/asset.
3. **Audit**: Lead agent (Critic) enforces GBC hardware limits.
4. **Approval**: User approves final draft.
5. **Execution**: Logic injected into `project.gbsproj` via Python tools.

## The Mycelium Contract

**MANDATORY FOR ALL AGENTS:**
- **Arrival**: Run `mycelium.sh context <file>` before reading/editing.
- **Departure**: Run `mycelium.sh note <file> -k decision -m "..."` after work.

## Project Structure

- `BARRY-SHARP-PRO-MOVER-GBC/`: Core Game Boy project.
- `tools/unified-backend/`: FastAPI brain, agent logic, and hardware-specific validators.
- `design/`: Master GDD, Art Bible, and GBVM technical references.
- `.claude/`: Studio configuration (Agents, Skills, Hooks, Rules).

## Available Command Hooks

- `playtest.sh`: Compiles ROM and launches OpenEmu (Local Mac only).
- `.claude/hooks/validate-assets.sh`: Mathematically enforces GBC color/tile limits.
- `.claude/hooks/validate-commit.sh`: Verifies `.gbsproj` JSON integrity.
