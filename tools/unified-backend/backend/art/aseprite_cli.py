import subprocess
import os
import tempfile
from loguru import logger

class AsepriteCLI:
    """
    Wrapper for Aseprite CLI ('aseprite -b') to process images.
    """
    
    GBC_PALETTE_GPL = """GIMP Palette
Name: GBC
Columns: 1
#
0 0 0
85 85 85
170 170 170
255 255 255
"""

    def __init__(self, aseprite_path: str = "aseprite"):
        self.aseprite_path = aseprite_path

    def _ensure_palette_file(self) -> str:
        """
        Creates a temporary GBC palette file.
        
        Returns:
            The path to the temporary palette file.
        """
        palette_path = os.path.join(tempfile.gettempdir(), "gbc_palette.gpl")
        with open(palette_path, "w") as f:
            f.write(self.GBC_PALETTE_GPL)
        return palette_path

    def process_image(
        self, 
        input_path: str, 
        output_path: str, 
        width: int = 160, 
        height: int = 144
    ) -> bool:
        """
        Resizes and applies a 4-color indexed palette using Aseprite.
        
        Args:
            input_path: Path to the input image file.
            output_path: Path where the processed image will be saved.
            width: Target width in pixels.
            height: Target height in pixels.
            
        Returns:
            True if successful, False otherwise.
        """
        if not os.path.exists(input_path):
            logger.error(f"Input file does not exist: {input_path}")
            return False

        palette_path = self._ensure_palette_file()
        
        try:
            # Aseprite command:
            # -b: run in background (CLI mode)
            # --load-palette: load the GBC palette
            # --scale: resize (this is tricky with absolute dimensions, better use --resize)
            # --color-mode indexed: convert to indexed colors
            # --save-as: specify output file
            
            # Note: For exact resizing, --resize WxH is often used.
            command = [
                self.aseprite_path,
                "-b",
                input_path,
                "--palette", palette_path,
                "--resize", f"{width},{height}",
                "--color-mode", "indexed",
                "--save-as", output_path
            ]
            
            logger.info(f"Running Aseprite command: {' '.join(command)}")
            subprocess.run(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True,
                check=True
            )
            
            if os.path.exists(output_path):
                logger.info(f"Successfully processed image: {output_path}")
                return True
            else:
                logger.error(f"Aseprite finished but output file not found: {output_path}")
                return False
                
        except subprocess.CalledProcessError as e:
            logger.error(f"Aseprite command failed with error: {e.stderr}")
            return False
        except Exception as e:
            logger.error(f"Error during Aseprite processing: {e}")
            return False

if __name__ == "__main__":
    # Quick manual test
    cli = AsepriteCLI()
    # Assume we have a test.png
    # res = cli.process_image("test.png", "test_gbc.png")
    # print(f"Result: {res}")
