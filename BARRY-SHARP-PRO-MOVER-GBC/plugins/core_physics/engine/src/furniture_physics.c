#pragma bank 255

#include <gb/gb.h>
#include "gbs_types.h"
#include "vm.h"

// Define the global engine fields exposed in engine.json
extern UBYTE barry_grip_strength;
extern UBYTE global_gravity;

void apply_furniture_friction() __banked {
    // This C function will be callable via GBVM assembly using VM_CALL_NATIVE.
    // It handles the complex math of checking grid collision before allowing Barry to pivot a 2x1 couch.
    // A stub for the AI Engine Programmer to expand upon.
}