#!/bin/bash
# playtest.sh - Local developer bridge for GBStudio CLI

# Load environment variables
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

echo "=== BARRY SHARP'S PRO MOVER: Gatekeeper & Build ==="

# 1. Asset Validation
echo "Running Asset Gatekeeper..."
python3 scripts/validate_assets.py
if [ $? -ne 0 ]; then
    echo "Asset validation failed. Fix the errors and try again."
    exit 1
fi

PROJECT="BARRY-SHARP-PRO-MOVER-GBC/project.gbsproj"
PROJECT_DIR="BARRY-SHARP-PRO-MOVER-GBC"
BUILD_DIR="BARRY-SHARP-PRO-MOVER-GBC/build"

# Check for argument
if [ "$1" == "--rom" ]; then
    echo "Compiling ROM via npx gb-studio-cli..."
    cd "$PROJECT_DIR"
    npx gb-studio-cli make:rom -c "project.gbsproj" -o "build"
    BUILD_STATUS=$?
    cd ..

    if [ $BUILD_STATUS -eq 0 ]; then
        ROM_FILE="$BUILD_DIR/rom/game.gbc"
        echo "Build Success: $ROM_FILE"
        echo "Launching OpenEmu..."
        open -a OpenEmu "$ROM_FILE"
    else
        echo "Build Failed. Check logs."
        exit 1
    fi
else
    echo "Compiling Web Build via npx gb-studio-cli..."
    cd "$PROJECT_DIR"
    npx gb-studio-cli make:web -c "project.gbsproj" -o "build"
    BUILD_STATUS=$?
    cd ..

    if [ $BUILD_STATUS -eq 0 ]; then
        echo "Web Build Success."
        echo "Starting local server on http://localhost:8080..."
        cd "$BUILD_DIR/web"
        python3 -m http.server 8080
    else
        echo "Web Build Failed. Check logs."
        exit 1
    fi
fi
