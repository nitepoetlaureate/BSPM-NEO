# BARRY SHARP'S PRO MOVER - Furniture Physics (GBVM)

## Overview
Because the Game Boy Color has no floating-point math, all "physics" are grid-based and integer-driven.

## Movement Rules (Fixed-Point Integer)
- **Barry Base Speed:** 2 pixels per frame (normal).
- **Encumbrance Formula:** Speed = BaseSpeed - (FurnitureWeight / 4).
- **Minimum Speed:** 1 pixel every 2 frames.

## The Push/Pull Logic
1. **Directional Locking:** Once Barry begins pushing an object along an axis (X or Y), he is locked to that axis until the D-pad is released.
2. **Corner Friction:** If Barry tries to pivot a 2x1 object around a 1x1 corner, the "Friction" variable must check for collision on the 45-degree tile.
3. **Momentum:** Heavy objects (Weight > 50) require a 15-frame "Wind-up" before they move at full encumbered speed.

## GBVM Injection Variables
- `VAR_BARRY_SPEED` (Local 0)
- `VAR_FURNITURE_WEIGHT` (Local 1)
- `VAR_COLLISION_TYPE` (Local 2)
