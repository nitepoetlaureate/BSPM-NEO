from PIL import Image
import sys
import os

def quantize_to_gbc(image_path, output_path):
    """
    Forces an image into a 3-color GBC palette with a green transparency mask.
    Target Palette: Black (0,0,0), Dark Grey (100,100,100), Light Grey (200,200,200).
    Transparency: Green (0,255,0).
    """
    try:
        img = Image.open(image_path).convert('RGBA')
        # Snap to 16x16 or 8x8 if requested, but for now we assume input is correct size
        # Target GBC Palette (3 colors + transparency)
        palette = [(0, 0, 0), (100, 100, 100), (200, 200, 200)]
        
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                r, g, b, a = pixels[x, y]
                # Use green (0, 255, 0) as the transparency mask if alpha is low or already green
                if a < 128 or (r == 0 and g == 255 and b == 0):
                    pixels[x, y] = (0, 255, 0, 255)
                else:
                    # Map to closest grey color
                    closest = min(palette, key=lambda c: (c[0]-r)**2 + (c[1]-g)**2 + (c[2]-b)**2)
                    pixels[x, y] = (*closest, 255)
        
        img.save(output_path)
        print(f"Success: Quantized image saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error during quantization: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 quantize_gbc.py <input_path> <output_path>")
        sys.exit(1)
    quantize_to_gbc(sys.argv[1], sys.argv[2])
