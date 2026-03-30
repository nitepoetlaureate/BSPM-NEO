---
name: architecture-decision
description: "Documents hardware-strict decisions and ensures they are logged into the Mycelium state engine."
argument-hint: "[title]"
user-invocable: true
allowed-tools: Read, Write, Bash
---

# ADR: GBC Hardware Decision

When this skill is invoked:

1. **Guide the Decision**:
   - Focus exclusively on GB Studio 3.x and GBC hardware.
   - Every decision MUST respect 8-bit architecture and memory limits.

2. **Generate the ADR Document**:
   - Save to `docs/architecture/ADR-[NNNN].md`.

3. **Log into Mycelium (MANDATORY)**:
   - Every architectural decision MUST be logged into the Mycelium state engine.
   - Either trigger a Mycelium sync command OR write the decision details to `production/session-state/active.md`.

```markdown
# ADR-[NNNN]: [Title] (GBC Architecture)

## Status
[Proposed | Accepted | Deprecated]

## GBC Hardware Constraints
- Max 10 actors per scene.
- 8-bit integer variables (0-255).
- Balanced GBVM stack.
- **NO 3D, NO FLOATS.**

## Decision
[The specific technical decision made]

## Mycelium Sync Status
- **Logged to Mycelium**: [YES/NO]
- **Session File Update**: [Updated `production/session-state/active.md`]

## Consequences
- **Positive**: [Better performance / lower flicker]
- **Negative**: [Increased 8-bit complexity]
```

### Rules
- **Mycelium Integration**: A decision is NOT complete until it is logged to `production/session-state/active.md`.
- **Fail on Modernity**: Reject any mention of 3D, VFX, or floats.
- **Strictly 8-bit**: Prioritize GBC architecture above all else.
