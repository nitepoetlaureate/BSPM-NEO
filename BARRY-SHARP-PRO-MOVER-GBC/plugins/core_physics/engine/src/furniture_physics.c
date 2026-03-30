#pragma bank 255

#include <gb/gb.h>
#include "gbs_types.h"
#include "vm.h"
#include "collision.h"

// Define the global engine fields exposed in engine.json
UBYTE barry_grip_strength = 10;
UBYTE global_gravity = 1;

// Function to check if a tile is solid at pixel coordinates
UBYTE is_solid_at(UBYTE x, UBYTE y) {
    // Use the engine's built-in collision detection
    return tile_at_2(x, y);
}

void apply_furniture_friction(void) __banked {
    // This C function can be called via VM_CALL_NATIVE.
    // Logic to calculate if Barry has enough grip to push the furniture.
    // Placeholder for real friction math.
}
