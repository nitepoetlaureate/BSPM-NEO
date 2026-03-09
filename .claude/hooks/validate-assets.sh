#!/bin/bash
# .claude/hooks/validate-assets.sh - Enforces strict GBC Hardware Limits

FILE_PATH=$1

if [[ ! -f "$FILE_PATH" ]]; then
    exit 0
fi

# Check for ImageMagick 'identify'
if ! command -v identify &> /dev/null; then
    echo "Warning: ImageMagick not found. Skipping validation."
    exit 0
fi

# Identify if file is a Sprite or Background based on path
IS_SPRITE=false
if [[ "$FILE_PATH" == *"sprites"* ]]; then
    IS_SPRITE=true
fi

# Count unique colors
COLOR_COUNT=$(identify -format "%k" "$FILE_PATH")

if [ "$IS_SPRITE" = true ]; then
    # GBC Sprites: 4 colors total, but Color 0 is Transparent = 3 visible colors.
    # Note: If the file has a transparency layer, identify treats it as a color.
    if [ "$COLOR_COUNT" -gt 4 ]; then
        echo "Error: Sprite $FILE_PATH has $COLOR_COUNT colors. Max visible is 3 (+ transparent)."
        exit 1
    fi
else
    # GBC Backgrounds: Max 4 colors per 8x8 tile. 
    if [ "$COLOR_COUNT" -gt 4 ]; then
        echo "Error: Background $FILE_PATH has $COLOR_COUNT colors. Max allowed is 4."
        exit 1
    fi
fi

# Verify Dimensions (Must be multiples of 8)
WIDTH=$(identify -format "%w" "$FILE_PATH")
HEIGHT=$(identify -format "%h" "$FILE_PATH")

if (( WIDTH % 8 != 0 )) || (( HEIGHT % 8 != 0 )); then
    echo "Error: $FILE_PATH dimensions (${WIDTH}x${HEIGHT}) are not multiples of 8px (Game Boy Tiles)."
    exit 1
fi

echo "GBC Asset Validation passed: $FILE_PATH"
exit 0
