# BARRY SHARP'S PRO MOVER - Master Art Bible

## Core Aesthetic: 8-Bit Retro GBC / DMG
This game must adhere to the hard physical limits of the Game Boy Color and original Game Boy hardware.

### 1. The Color Palettes
#### GBC Master Palette (Barry Sharp Default)
- **Black:** `#000000` (Outline / Deep Shadow)
- **Dark Gray:** `#555555` (Furniture Detail)
- **Light Gray:** `#AAAAAA` (Highlights)
- **White:** `#FFFFFF` (Barry / Bright UI)

#### DMG Classic Palette (Pea Soup)
- Shade 1 (Off): `#9BBC0F`
- Shade 2 (Light): `#8BAC0F`
- Shade 3 (Dark): `#306230`
- Shade 4 (On): `#0F380F`

### 2. Hardware Constraints (MANDATORY)
- **Backgrounds (BG):** Max 8 palettes of 4 colors each. Single 8x8 tile can only use ONE palette.
- **Background Complexity:** Max 192 unique 8x8 tiles per screen. Reuse tiles for floors and walls.
- **Sprites (OBJ):** Max 8 palettes. **COLOR 0 IS TRANSPARENT.**
- **Sprite Limit:** A single 8x8 or 16x16 sprite can only show **3 visible colors**.
- **Resolution:** 160x144 pixels (20x18 tiles).

### 3. Visual Standard of Success
- **Success:** Pixel-perfect edges, high-contrast silhouettes, and orthographic isometric perspective.
- **Failure:** Gradients, alpha transparency, anti-aliasing, or using more than 3 colors on a sprite.
- **YAGNI:** 3D blockouts, dynamic lighting, or modern VFX particles.
