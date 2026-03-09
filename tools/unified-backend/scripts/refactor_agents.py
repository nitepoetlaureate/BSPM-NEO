import re
from pathlib import Path

AGENTS_DIR = Path(".claude/agents")

# The text to append to the bottom of every agent to ensure GBC constraints
GBC_MANDATE = """
### UNIVERSAL GBC CONSTRAINTS (MANDATORY)
1. You are developing 'BARRY SHARP PRO MOVER' for GB Studio 3.x.
2. DO NOT reference Unity, Godot, Unreal, 3D, C#, or modern shaders.
3. The hardware is the Game Boy Color (8-bit CPU, 160x144 resolution, 4-color palettes, 10 actors per scene max).
4. If your task violates these limits, you must explicitly REJECT the design.
"""

def purify_agents():
    for filepath in AGENTS_DIR.glob("*.md"):
        content = filepath.read_text(encoding="utf-8")
        
        # Strip modern 3D engine references
        content = re.sub(r'(?i)(unity|godot|unreal engine|ue4|ue5|c\#|c\+\+|blueprints|gdscript|3d model|pbr shader)', '[REDACTED 3D TECH]', content)
        
        # Inject the universal mandate if not present
        if "UNIVERSAL GBC CONSTRAINTS" not in content:
            content += f"\n{GBC_MANDATE}\n"
            
        filepath.write_text(content, encoding="utf-8")
        print(f"Purified: {filepath.name}")

if __name__ == "__main__":
    purify_agents()
