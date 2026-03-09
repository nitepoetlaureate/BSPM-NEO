# GBVM Technical Reference (SM83 / GBC)

## Overview
GBVM (Game Boy Virtual Machine) is a stack-based instruction set powering GB Studio 3.x logic.

## Core Operations (Stack-Based)
All operations follow a Push -> Op -> Pop cycle.

- `VM_PUSH_CONST <val>`: Pushes a 16-bit constant onto the stack.
- `VM_POP <count>`: Pops N values from the stack to prevent overflow.
- `VM_IF <op> <var_a> <var_b> <label>`: Jumps to label if condition is met.
- `VM_JUMP <label>`: Unconditional jump.
- `VM_SET_CONST <var> <val>`: Directly sets a variable to a constant.

## Memory & Variable Scoping
- **Global Variables:** Prefixed with `VAR_`. Limit is 512.
- **Local Variables:** Prefixed with `L0`, `L1`... `L7`. Use these for all math to save RAM.
- **Integers Only:** No floating point. Range is 0-65535 (unsigned) or -32768 to 32767 (signed).

## Movement & Physics
- `VM_ACTOR_MOVE_TO <actor_id> <x> <y>`: Grid-aligned movement.
- `VM_ACTOR_SET_POS <actor_id> <x> <y>`: Instant teleport.
- `VM_ACTOR_GET_POS <actor_id> <var_x> <var_y>`: Store actor position in variables.

## Hardware Constraints
- **Screen:** 160x144 px (20x18 tiles).
- **Actors:** 10 max per scene + player.
- **Background Tiles:** 192 unique tiles max.
- **Sprites:** 40 max on screen, 10 max per scanline.
