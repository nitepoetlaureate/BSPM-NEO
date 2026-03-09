---
name: architecture-decision
description: "Creates an Architecture Decision Record (ADR) for GB Studio technical choices. Documents context, 8-bit alternatives, and hardware consequences."
argument-hint: "[title]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
---

When this skill is invoked:

1. **Next ADR number**: Scan `docs/architecture/` for existing ADRs.

2. **Gather context**: Read related scripts and existing ADRs.

3. **Guide the user through the decision**: Ask clarifying questions focused on GB Studio 3.x and 8-bit hardware.

4. **Generate the ADR** following this format:

```markdown
# ADR-[NNNN]: [Title] (GB Studio 3.x)

## Status
[Proposed | Accepted | Deprecated]

## Context

### Problem Statement
[What problem are we solving within GB Studio logic/scripting?]

### Hardware Constraints (8-bit)
- Max 20 actors per scene.
- Max 10 sprites per row.
- 8-bit integer variables (0-255 range).
- 4-color palettes per tile.
- **NO 3D, NO VFX, NO FLOATS.**

### Requirements
- [Must support X in the GB emulator]
- [Must fit within variable limits]

## Decision

[The specific technical decision made for GB Studio, including script trigger logic and variable mapping.]

### Logic Diagram
[ASCII flow for GB Studio script events]

### 8-bit Variable Usage
[Mapping of bits/variables created by this decision]

## Alternatives Considered (8-bit)

### Alternative 1: [Name]
- **Pros**: Low actor overhead.
- **Cons**: High variable usage.
- **Rejection Reason**: [Hardware limit violation?]

## Consequences

### Positive
- [Better performance / lower flicker]

### Negative
- [8-bit complexity increase]

## Performance Implications (8-bit)
- **Actor Density**: [Expected impact]
- **CPU/VBlank**: [Expected impact, e.g. sprite flicker]
- **Memory/Variables**: [Number of 8-bit global variables used]

## Validation Criteria
- ROM compiles cleanly.
- Logic passes 8-bit range testing (no overflow).

## Related Decisions
- [Links to related ADRs]
```

5. **Guidelines**:
- **Delegate to `systems-designer`** for 8-bit math validation.
- **Delegate to `game-designer`** for scripting feasibility check.
- **FAIL** if mentions 3D, VFX, or non-8-bit logic.
