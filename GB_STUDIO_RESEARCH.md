# GB Studio 4.2.2 & GBVM Research Findings

This document summarizes the latest research on GB Studio 4.2.2 architecture, GBVM instructions, and community plugin standards to inform the next phase of development for **Barry Sharp's Pro Mover**.

---

## 1. GBVM (Game Boy Virtual Machine) Deep Dive

GBVM is the assembly-like bytecode interpreter powering GB Studio 3.0+. Research into the official `gbvm` repository and engine source reveals key mechanisms for high-performance logic.

### Core Instruction Set (vm.i)
The definitive list of macros is maintained in `chrismaltby/gbvm/include/vm.i`. Key instructions for furniture physics include:
- **`VM_ACTOR_GET_POS` / `VM_ACTOR_SET_POS`**: Essential for reading and snapping furniture to the grid.
- **`VM_ACTOR_GET_DIR`**: Used to identify player facing direction (1:R, 2:L, 4:U, 8:D).
- **`VM_RPN`**: The Reverse Polish Notation calculator. This is the most efficient way to perform multi-step math (like `pos + offset`) without wasting stack operations.
- **`VM_IF_CONST`**: The fastest way to branch logic based on direction or friction results.

### New in 4.2.2
- **Axis-Specific Movement**: New instructions like `VM_ACTOR_MOVE_TO_X` and `VM_ACTOR_MOVE_TO_Y` reduce CPU overhead by avoiding redundant calculations for the unchanged axis.
- **Rate Limiting**: `VM_RATE_LIMIT_CONST` can be used to throttle the "Push" check to every 5-10 frames, preventing logic lag during movement.
- **Bank 0 Optimizations**: Math functions (`isqrt`, `sin`, `cos`) have been moved to banked space, meaning our C engine plugins have more room in the critical Bank 0 for core physics overrides.

---

## 2. Plugin Architecture (GB Studio 4.2.2)

The 4.2.x series standardized the **Plugin Manager**, which strictly enforces folder structures.

### Standard Structure
```text
plugins/
└── [CategoryName]/
    ├── engine/
    │   ├── engine.json (Must specify "version": "4.2.2-e1")
    │   └── src/ (.c and .h files for engine overrides)
    └── events/
        └── event[Name].js (Script Event definitions)
```

### Community Standards (The "Pau-Tomas" Pattern)
Top-tier community plugins (like those from Pau-Tomas or Tomo666) utilize the following best practices:
- **Variable Aliasing**: Instead of hardcoding variable IDs, use `getVariableAlias` in the `.js` compiler to make the event user-friendly in the GUI.
- **Actor Activation**: Modern 4.2 plugins always call `actorSetActive(input.actorId)` before movement helpers to avoid the `eval.js` crash.
- **GDK Compatibility**: C plugins should include `collision.h` and use `tile_at_2(tx, ty)` for background checks, as it is the most CPU-efficient way to prevent objects from clipping through walls.

---

## 3. RetroDiffusion API (Art Generation)

Research indicates that **astropulse/RetroDiffusion** is a paid, private service.

### Integration Path
- **Official API**: Hosted at `retrodiffusion.ai`. Access requires a personal API key and use of their specific Gradio endpoints.
- **Standalone Client**: The Python script `hf_client.py` is the correct approach, but it must be configured with the **exact endpoint URL** found in the "Developer Tools" section of the user's logged-in RetroDiffusion account.
- **Fallback**: For testing without an active RetroDiffusion subscription, `anzorq/finetuned_diffusion` or `nerijs/pixelcascade128-v0.1` on Hugging Face are viable community alternatives for generating "retro-style" art.

---

## 4. Agentic Workflow Improvements

GB Studio projects are highly "agent-friendly" because they are collections of small JSON files (`.gbsres`).

### Recommended Agent Directives
1. **JSON Surgery via `jq`**: Agents should use `jq` for surgical edits to `scene.gbsres` instead of rewriting the whole file, reducing the risk of UUID corruption.
2. **One-Shot Scene Generation**: The `gbstudio-claude-mcp` tool is the preferred method for creating new scenes, as it handles the "distributed" folder creation automatically.
3. **Automated Quantization**: The `quantize_gbc.py` script should be part of the `art-director`'s core toolset, automatically triggered whenever a new image is added to the `assets/` folder.
