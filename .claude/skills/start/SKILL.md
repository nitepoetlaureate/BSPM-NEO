---
name: start
description: "First-time onboarding for GB Studio development. Asks for project status and guides you to the correct workflow."
argument-hint: "[no arguments]"
user-invocable: true
allowed-tools: Read, Glob, Grep, AskUserQuestion
---
# Code/Quality Purifier: GB Studio Onboarding

When this skill is invoked:

1. **Silent Detection**:
   - **Project File**: Search for `.gbsproj`.
   - **ROM Check**: Check for ROMs in `build/`.
   - **Documentation**: Count Markdown files in `design/gdd/`.

2. **User Inquiry**:
   > **Welcome to the GB Studio Code/Quality Purifier!**
   > How can I help you build your Game Boy game today?
   >
   > **A) No idea yet**: Explore concepting and GB Studio basics.
   > **B) Clear concept**: Jump to engine setup and asset planning.
   > **C) Existing work**: Analyze my current `.gbsproj` for performance and gaps.
   > **D) Prototype**: Test a specific mechanic with `gb-studio-cli`.

3. **Routing based on selection**:

| Choice | Path |
|--------|------|
| **A** | Run `/brainstorm open` |
| **B** | Run `/project-stage-detect` then `/setup-engine` |
| **C** | Run `/project-stage-detect` then `/perf-profile` |
| **D** | Run `/prototype` |

### Rules
- If no `.gbsproj` exists, emphasize that GB Studio is the primary engine.
- Always recommend `/project-stage-detect` for first-time onboarding with existing work.
- Keep output concise and focused on GB Studio hardware constraints.
