import subprocess
import pathlib
from loguru import logger

class GBStudioBuildRunner:
    """Wrapper for the GBStudio CLI to compile ROMs programmatically."""
    
    def __init__(self, project_path: str, build_dir: str):
        self.project_path = pathlib.Path(project_path)
        self.build_dir = pathlib.Path(build_dir)
        self.build_dir.mkdir(parents=True, exist_ok=True)

    def compile_rom(self) -> str:
        """Runs the gb-studio-cli make:rom command via npx."""
        logger.info(f"Starting ROM compilation for {self.project_path}...")
        
        # Use npx to invoke the local gb-studio-cli installation
        command = [
            "npx", "gb-studio-cli",
            "make:rom",
            "-c", str(self.project_path),
            "-o", str(self.build_dir)
        ]
        
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                cwd=self.project_path.parent # Run from the project directory where node_modules lives
            )
            logger.info("ROM compilation successful.")
            logger.debug(f"Compiler output: {result.stdout}")
            
            # The CLI usually outputs to build/rom/game.gbc
            rom_path = self.build_dir / "rom" / "game.gbc"
            return str(rom_path)
            
        except subprocess.CalledProcessError as e:
            logger.error(f"ROM compilation failed with exit code {e.returncode}")
            logger.error(f"Error output: {e.stderr}")
            raise RuntimeError(f"Build failed: {e.stderr}")
        except FileNotFoundError:
            logger.error("npx or gb-studio-cli not found. Ensure Node.js is installed.")
            raise
