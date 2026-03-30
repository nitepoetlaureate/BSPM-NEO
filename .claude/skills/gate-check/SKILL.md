---
name: gate-check
description: "Hardware-strict phase gate validation for GBC development. Hard-blocks on any asset validation warnings."
argument-hint: "[target-phase]"
user-invocable: true
allowed-tools: Read, Bash, Write
---

# GBC Phase Gate Validation

This skill validates readiness to advance through GBC development using GB Studio 3.x.

## 1. Automated Validation (MANDATORY)

- **Execute**: `python3 scripts/validate_assets.py`.
- **Hard Block**: If the script returns ANY warnings or errors, the phase gate MUST fail.

## 2. Hardware Checks

- [ ] **Scene Limits**: Max 10 actors per scene.
- [ ] **Variable Range**: 8-bit integer (0-255).
- [ ] **Stack Balance**: Verified balanced GBVM stack.

## 3. Verdict Output

```markdown
## Gate Check: [Current Phase] → [Target Phase]

### Automated Validation: [PASSED / FAILED]
- **Script Status**: [No Warnings / WARNINGS DETECTED]
- **Blockers**: [List warnings from `scripts/validate_assets.py`]

### Hardware Readiness: [X/3 present]
- [ ] Actors (Max 10 respected)
- [ ] Variables (All 8-bit)
- [ ] Stack (Balanced)

### Verdict: [PASS / FAIL]
```

### Rules
- **Asset Compliance First**: The `scripts/validate_assets.py` script is the final authority. Any warning is a `FAIL`.
- **Zero Tolerance for Modernity**: Block any reference to 3D, VFX, or floats.
- **Mycelium Integration**: Every gate check must be recorded in the Mycelium session state.
