# GEMINI CLI STUDIO CONFIGURATION

This file is automatically loaded by Gemini CLI to provide project-specific context and tool instructions.

## Project State: Phase 2 (Network Deployment)

We have successfully "Purified" the studio. All 48 agents and 37 skills are configured for Game Boy Color. The FastAPI backend is strictly typed and wired to Discord/PicoClaw.

## Immediate Next Steps for Next Instance

1. **Verify Backend Connectivity**: Start the FastAPI server (`cd tools/unified-backend && uv run python -m uvicorn backend.main:app`) and check `/health`.
2. **Environment Check**: Ensure `.env` exists with real keys (not placeholders).
3. **MCP Tool Use**: You have native access to `huggingface` and `chrome-devtools` MCPs. 
   - Use `mcp_huggingface_...` tools for any ZeroGPU or Space interaction.
   - Do NOT use the deprecated `hf_client.py` for image generation; use the MCP instead.
4. **Mycelium Sync**: Run `mycelium.sh sync-init` to ensure notes are connected to the remote.

## Active MCP Tools

- **huggingface**: Use for searching models, datasets, and running inference on your private spaces.
- **chrome-devtools**: Use for any browser-based debugging or automation tasks.

## Constraints Reference

- **Resolution**: 160x144 pixels.
- **Tiles**: Max 192 unique 8x8 tiles for backgrounds.
- **Sprites**: Max 3 visible colors per sprite (Color 0 is transparent).
- **Math**: 8-bit integers only. No floating point.
