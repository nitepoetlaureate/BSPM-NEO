#pragma bank 255

#include <gb/gb.h>
#include "gbs_types.h"
#include "vm.h"

// Define the global engine fields exposed in engine.json
UBYTE barry_grip_strength = 10;
UBYTE global_gravity = 1;

void apply_furniture_friction(void) __banked {
    // This C function will be callable via GBVM assembly using VM_CALL_NATIVE.
}
