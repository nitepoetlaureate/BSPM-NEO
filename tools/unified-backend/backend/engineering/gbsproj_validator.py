import json
import pathlib
import sys
from loguru import logger

class GBProjValidator:
    """Ensures the project.gbsproj JSON matches the minimum required GBStudio 3.x schema."""
    
    REQUIRED_KEYS = ["_resourceType", "scenes", "backgrounds", "sprites", "settings"]

    @staticmethod
    def validate_file(file_path: str) -> bool:
        path = pathlib.Path(file_path)
        if not path.exists():
            logger.error(f"Validation failed: File {file_path} does not exist.")
            return False
            
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Validation failed: Malformed JSON in {file_path}. Error: {e}")
            return False
            
        # Check for top-level keys
        for key in GBProjValidator.REQUIRED_KEYS:
            if key not in data:
                logger.error(f"Validation failed: Missing required key '{key}' in {file_path}.")
                return False
        
        # Verify Scenes structure
        if not isinstance(data.get("scenes"), list):
            logger.error("Validation failed: 'scenes' must be an array.")
            return False
            
        logger.info(f"Validation successful: {file_path} is a valid GBStudio project.")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: uv run python gbsproj_validator.py <path_to_gbsproj>")
        sys.exit(1)
        
    success = GBProjValidator.validate_file(sys.argv[1])
    sys.exit(0 if success else 1)
