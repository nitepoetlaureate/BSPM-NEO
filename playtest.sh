#!/bin/bash
# playtest.sh - Local developer bridge for OpenEmu and GBStudio CLI

# Load environment variables
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# We use npx to invoke the local gb-studio-cli
PROJECT="BARRY-SHARP-PRO-MOVER-GBC/project.gbsproj"
PROJECT_DIR="BARRY-SHARP-PRO-MOVER-GBC"
BUILD_DIR="BARRY-SHARP-PRO-MOVER-GBC/build"

echo "=== BARRY SHARP'S PRO MOVER: Build & Play ==="

# 1. Compile ROM
echo "Compiling ROM via npx gb-studio-cli..."
cd "$PROJECT_DIR"
npx gb-studio-cli make:rom -c "project.gbsproj" -o "build"
BUILD_STATUS=$?
cd ..

if [ $BUILD_STATUS -eq 0 ]; then
    ROM_FILE="$BUILD_DIR/rom/game.gbc"
    echo "Build Success: $ROM_FILE"
    
    # 2. Launch in OpenEmu
    echo "Launching OpenEmu..."
    open -a OpenEmu "$ROM_FILE"
else
    echo "Build Failed. Check logs."
    exit 1
fi
