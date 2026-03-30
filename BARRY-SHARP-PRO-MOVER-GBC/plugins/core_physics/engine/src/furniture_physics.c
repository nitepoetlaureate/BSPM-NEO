#pragma bank 255

#include <gb/gb.h>
#include "gbs_types.h"
#include "vm.h"
#include "collision.h"

extern UBYTE barry_grip_strength;
extern UBYTE global_gravity;

UBYTE is_solid_at(UBYTE x, UBYTE y) {
    return tile_at_2(x, y);
}

void apply_furniture_friction(SCRIPT_CTX * THIS) __banked {
    // Basic math: if grip > gravity, return 1 (success), else 0 (fail)
    UBYTE can_push = 0;
    if (barry_grip_strength > global_gravity) {
        can_push = 1;
    }
    
    // Push the result back to the VM stack so GBVM can read it
    *(THIS->stack_ptr) = can_push;
}
