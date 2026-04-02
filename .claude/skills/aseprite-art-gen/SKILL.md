---
name: aseprite-art-gen
description: Automated art generation using local Aseprite and RetroDiffusion. Use when the user needs to generate pixel art sprites or backgrounds for the Game Boy project.
---

# Aseprite RetroDiffusion Art Generation

This skill teaches you how to use the local "Art Forge" to generate hardware-compliant assets.

## The Workflow

1. **Formulate the Prompt**: Write a specific prompt including "pixel art" and "game boy style".
2. **Execute the Command**: Use the `art_forge.py` tool.
   ```bash
   python3 tools/art_forge.py --prompt "your prompt" --output "BARRY-SHARP-PRO-MOVER-GBC/assets/sprites/name.png" --width 16 --height 16
   ```
3. **Verify Compliance**: The tool automatically runs `validate_assets.py` and `quantize_gbc.py`. 
4. **Import to Project**: Once saved, use the `gbstudio-claude-mcp` to register the asset in the `.gbsres` files if necessary.

## Constraints
- **Sprites**: 16x16 or 16x32.
- **Backgrounds**: 160x144.
- **Device**: Generation is currently forced to CPU mode. Expect execution times of 2-5 minutes.
