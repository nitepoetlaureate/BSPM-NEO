# The Mycelium Contract (MANDATORY)

You are operating in a studio that uses `git notes` via `mycelium.sh` as its deterministic memory graph.

**Rule 1: Read Before Acting**
BEFORE you read or edit any code or asset file (e.g., `src/physics.c` or `assets/barry.png`), you MUST use your Bash tool to execute:
`mycelium.sh context <filepath>`
You must read the output to understand the history, decisions, and warnings attached to that file.

**Rule 2: Write Before Leaving**
AFTER modifying any code or asset, you MUST use your Bash tool to execute:
`mycelium.sh note <filepath> -k <kind> -m '<brief explanation of what you did and why>'`

Valid kinds:
- `-k decision` (For architectural or logic choices)
- `-k warning` (For edge cases or fragility)
- `-k todo` (For incomplete tasks)
- `-k summary` (For summarizing a new file)

**Standard of Failure:**
If you edit a file but fail to leave a Mycelium note, your task will be rejected by the QA and Lead agents.
