---
name: perf-profile
description: "Uses automated MCP tools to profile GB Studio projects against hardware-strict actor and variable limits."
argument-hint: "[scene-name|full]"
user-invocable: true
allowed-tools: Bash, Read
---
# GBC Resource Profiler (Automated)

When this skill is invoked:

1. **Query the project via `gbstudio-claude-mcp`**:
   - Query `project.gbsproj` for all scene actor counts and global variables.

2. **Audit Actor Counts**:
   - **Limit**: Max 10 actors per scene.
   - Any scene exceeding 10 actors is a `CRITICAL` failure.

3. **Audit Global Variables**:
   - **Limit**: Max 512 global variables.
   - Any project exceeding 512 global variables is an `OVER BUDGET` failure.

4. **Generate the Report**:

```markdown
## GBC Performance Profile: [Date]

### Resource Overview (Automated)
| Metric | Limit | Current | Status |
|--------|-------|---------|--------|
| Actors per Scene | 10 | [Max Found] | [OK/CRITICAL] |
| Global Variables | 512 | [Total Count] | [OK/OVER] |

### Scene-by-Scene Actor Audit
| Scene | Actor Count | Status |
|-------|-------------|--------|
| [Scene Name] | [N] | [PASS/FAIL] |

### Global Variable Status
- **Current Total**: [N]
- **Remaining Capacity**: [512 - N]
```

### Rules
- **Data Source**: Always use `gbstudio-claude-mcp` for accurate counts.
- **Strict Budgeting**: Any violation of the actor or variable limit is a blocker.
- **No Speculative Optimization**: Only report on the hard numbers from the project file.
