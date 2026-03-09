#!/bin/bash
# .claude/hooks/validate-commit.sh - Verifies GBC Project Integrity before Commit

PROJECT_FILE="BARRY-SHARP-PRO-MOVER-GBC/project.gbsproj"

# 1. Check if the project file is being committed
if [[ ! -f "$PROJECT_FILE" ]]; then
    echo "Notice: $PROJECT_FILE not found, skipping JSON validation."
    exit 0
fi

# 2. Verify JSON validity using jq
if ! command -v jq &> /dev/null; then
    echo "Warning: jq not found. Skipping strict JSON validation."
    exit 0
fi

if ! jq empty "$PROJECT_FILE" > /dev/null 2>&1; then
    echo "Error: $PROJECT_FILE contains malformed JSON!"
    exit 1
fi

# 3. Check for GBC specific hardware limits in the JSON
# (e.g., Ensuring the version is compatible with GBS 3.x)
VERSION=$(jq -r '._version' "$PROJECT_FILE")
if [[ "$VERSION" != 3* ]]; then
    echo "Error: Project version $VERSION is not compatible with GBS 3.x automated pipeline."
    exit 1
fi

echo "GBC Project Validation successful."
exit 0
