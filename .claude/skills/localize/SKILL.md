---
name: localize
description: "Handles localization for GB Studio projects. Extracts strings from project JSON/scripts and validates character limits for Game Boy screens."
argument-hint: "[scan|extract|status]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Bash
---
# Code/Quality Purifier: GB Studio Localizer

When this skill is invoked:

1. **Scan Subcommand**:
   - **Hardcoded Text**: Find text strings in project JSON/scripts.
   - **Character Limits**: Identify strings exceeding 18-20 characters per line (GB screen width).
   - **Variable Injection**: Check for `$Variable` usage in dialogue.

2. **Extract Subcommand**:
   - Generate a list of all dialogue and menu strings.
   - Group by scene or script category.
   - Output string table for translation (e.g., CSV or JSON format compatible with GB Studio assets).

3. **Status Report**:
```markdown
## GB Studio Localization Status
Generated: [Date]

| Locale | Strings | Coverage |
|--------|---------|----------|
| en (source) | [N] | 100% |
| [lang] | [N] | [X]% |

### Hardware Compatibility Issues
- [N] strings exceed 20 characters per line.
- [N] strings used without a "Wait" or "Clear" window.
```

### Rules
- All text must fit within the Game Boy's 160x144 resolution constraints.
- Prioritize **8-bit character sets**; warn if special characters are used that aren't in the project font.
- Every localized string must have a corresponding "Wait" command for player readability.
