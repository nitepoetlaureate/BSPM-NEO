<p align="center">
  <h1 align="center">BARRY SHARP'S PRO MOVER</h1>
  <p align="center">
    A Retro-Inspired GBC Puzzle-RPG developed by an Atomic AI Game Studio.
    <br />
    48 Agents. 8 Departments. 1 Legendary Mover.
  </p>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href=".claude/agents"><img src="https://img.shields.io/badge/agents-48-blueviolet" alt="48 Agents"></a>
  <a href=".claude/skills"><img src="https://img.shields.io/badge/skills-37-green" alt="37 Skills"></a>
  <a href="https://huggingface.co/"><img src="https://img.shields.io/badge/compute-HuggingFace%20PRO-ffad15?logo=huggingface" alt="HuggingFace PRO"></a>
  <a href="https://www.gbstudio.dev/"><img src="https://img.shields.io/badge/engine-GB%20Studio%203.x-red" alt="GB Studio"></a>
</p>

---

## The Vision

**BARRY SHARP'S PRO MOVER** is a unique, pixel-art, retro-inspired RPG/puzzle/open-world game about the high-stakes world of professional furniture moving. Developed for the original Game Boy Color hardware, the game challenges players to master the "Pivot" physics, manage stamina, and navigate narrow Victorian hallways without breaking the client's glass vases.

## The Studio OS (GBC Edition)

This project is built using a custom **Atomic AI Studio Architecture**. Instead of a single chatbot, development is managed by 48 specialized AI agents organized into 8 functional departments. Every line of code, every sprite, and every dialogue box is vetted through a rigorous **Actor-Critic** loop.

### Departmental Hierarchy

- **Executive Suite**: Vision, Production, and DevOps orchestration.
- **Design Pit**: Mechanical loops, 8-bit integer math, and RPG systems.
- **Engineering Bay**: GBVM Assembly, JSON Injection, and Core Engine Plugins.
- **Art Forge**: RetroDiffusion (ZeroGPU) asset generation and Aseprite formatting.
- **Narrative Wing**: GBC-constrained dialogue and world-building.
- **Level Lab**: 160x144 scene layouts and tile budget management.
- **Audio Studio**: 4-channel SFX and hUGETracker music integration.
- **QA Testing**: Edge-case discovery and ROM validation.

---

## Technology Stack

- **Engine**: [GB Studio 3.x](https://www.gbstudio.dev/)
- **Core Logic**: GBVM (Game Boy Virtual Machine) & SM83 Assembly
- **Plugins**: C (GBDK-2020) for hardware-level optimizations
- **Asset Generation**: RetroDiffusion Pro via Private HuggingFace ZeroGPU Spaces
- **Asset Editing**: [Aseprite](https://www.aseprite.org/) (CLI-automated & GUI-manual)
- **Memory Core**: [Mycelium](mycelium/README.md) (Deterministic Git-notes based agent memory)
- **Backend**: FastAPI / Pydantic v2 (Python 3.11+)
- **Network**: Tailscale-secured Docker sandboxes (Oracle Cloud & Mac Mini)

---

## Project Structure

```text
/
├── BARRY-SHARP-PRO-MOVER-GBC/    # Core GB Studio Project
│   ├── assets/                   # Palettes, Sprites, Backgrounds, Music
│   ├── plugins/                  # Custom C/Assembly Engine Plugins
│   └── project.gbsproj           # Master JSON Game Data
├── tools/
│   └── unified-backend/          # The FastAPI Brain & Agent Router
├── design/                       # GDDs, Art Bible, and GBVM Technical References
├── .claude/                      # Studio Configuration (Agents, Skills, Hooks)
├── production/                   # Sprints, Milestones, and Risk Registers
├── mycelium/                     # Agent Collaboration Runtime
├── playtest.sh                   # One-click GBC Build & Play (OpenEmu)
└── docker-compose-*.yml          # Tailscale Deployment Blueprints
```

---

## The Mycelium Contract

To eliminate technical debt, all agents adhere to the **Mycelium Contract**:
1. **Read Before Acting**: Agents query `mycelium.sh context` to understand a file's history.
2. **Document Decisions**: Every change is logged as a Git note (`kind decision`) explaining the *why* behind the logic.
3. **No Bullshit**: No placeholders, no mocks, and no stubs are allowed in production logic.

---

## Getting Started

### Local Setup (Human Director)

1. **Environment**: Install [Astral uv](https://docs.astral.sh/uv/), [Node.js](https://nodejs.org/), and [Aseprite](https://www.aseprite.org/).
2. **Secrets**: Copy `.env.template` to `.env` and fill in your Discord, HuggingFace, and Tailscale credentials.
3. **Mycelium**: Run `curl -fsSL https://raw.githubusercontent.com/openprose/mycelium/main/install.sh | bash` to install the memory runtime.
4. **Compile & Play**:
   ```bash
   ./playtest.sh
   ```

### AI Studio Activation

The studio is operated via **Discord/PicoClaw**. Messages in `#engineering`, `#art-department`, and `#design-pit` are automatically routed to the corresponding department sandboxes.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
