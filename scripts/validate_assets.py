#!/usr/bin/env python3
import os
import sys
from PIL import Image

def get_unique_tiles(image, tile_size=8):
    width, height = image.size
    tiles = set()
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            tile = image.crop((x, y, x + tile_size, y + tile_size))
            tiles.add(tile.tobytes())
    return len(tiles)

def validate_image(filepath, is_sprite):
    try:
        img = Image.open(filepath).convert('RGBA')
    except Exception as e:
        print(f"Error opening {filepath}: {e}")
        return False

    width, height = img.size

    # Check dimensions
    if width % 8 != 0 or height % 8 != 0:
        print(f"FAIL: {filepath} dimensions ({width}x{height}) are not multiples of 8.")
        return False

    # Get colors
    colors = img.getcolors(maxcolors=256)
    if colors is None:
        print(f"FAIL: {filepath} has too many colors.")
        return False

    if is_sprite:
        visible_colors = 0
        has_transparency = False
        for count, rgba in colors:
            r, g, b, a = rgba
            # Check for pure green mask or alpha 0
            if (r == 0 and g == 255 and b == 0) or a == 0:
                has_transparency = True
            else:
                visible_colors += 1

        if visible_colors > 3:
            print(f"FAIL: Sprite {filepath} uses {visible_colors} visible colors (Max 3).")
            return False
    else:
        # Backgrounds: check unique tiles
        unique_tiles = get_unique_tiles(img)
        if unique_tiles > 192:
            print(f"FAIL: Background {filepath} uses {unique_tiles} unique tiles (Max 192).")
            return False

    return True

def main():
    assets_dir = "BARRY-SHARP-PRO-MOVER-GBC/assets"
    sprites_dir = os.path.join(assets_dir, "sprites")
    bgs_dir = os.path.join(assets_dir, "backgrounds")

    failed = False

    # Check sprites
    if os.path.exists(sprites_dir):
        for f in os.listdir(sprites_dir):
            if f.endswith('.png'):
                if not validate_image(os.path.join(sprites_dir, f), is_sprite=True):
                    failed = True

    # Check backgrounds
    if os.path.exists(bgs_dir):
        for f in os.listdir(bgs_dir):
            if f.endswith('.png'):
                if not validate_image(os.path.join(bgs_dir, f), is_sprite=False):
                    failed = True

    if failed:
        sys.exit(1)
    else:
        print("Asset validation passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()
