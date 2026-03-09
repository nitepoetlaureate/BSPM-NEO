import json
import uuid
import pathlib
from filelock import FileLock
from loguru import logger
from .gbsproj_validator import GBProjValidator

class GBProjInjector:
    """Safely injects new entities into the GBStudio project file using file locking."""
    
    def __init__(self, project_path: str):
        self.project_path = pathlib.Path(project_path)
        self.lock_path = self.project_path.with_suffix(".lock")
        self.lock = FileLock(self.lock_path, timeout=10)

    def inject_scene(self, name: str, background_id: str, width: int = 20, height: int = 18):
        """Programmatically adds a new scene to the project."""
        with self.lock:
            logger.info(f"Acquired lock for {self.project_path}. Injecting scene: {name}")
            
            with open(self.project_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            new_scene = {
                "id": str(uuid.uuid4()),
                "name": name,
                "backgroundId": background_id,
                "x": 0,
                "y": 0,
                "width": width,
                "height": height,
                "type": "TOPDOWN",
                "actors": [],
                "triggers": [],
                "script": []
            }
            
            data["scenes"].append(new_scene)
            
            # Save and validate
            with open(self.project_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            
            if not GBProjValidator.validate_file(str(self.project_path)):
                logger.error("Injection corrupted the project file! Rolling back is not implemented yet.")
                raise RuntimeError("Injection failed validation.")
                
            logger.info(f"Successfully injected scene '{name}' with ID {new_scene['id']}")
            return new_scene["id"]

    def inject_actor(self, scene_id: str, name: str, sprite_id: str, x: int, y: int):
        """Adds a new actor to a specific scene."""
        with self.lock:
            with open(self.project_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            target_scene = next((s for s in data["scenes"] if s["id"] == scene_id), None)
            if not target_scene:
                raise ValueError(f"Scene ID {scene_id} not found.")
            
            new_actor = {
                "id": str(uuid.uuid4()),
                "name": name,
                "spriteSheetId": sprite_id,
                "x": x,
                "y": y,
                "frame": 0,
                "animate": False,
                "direction": "down",
                "script": []
            }
            
            target_scene["actors"].append(new_actor)
            
            with open(self.project_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                
            logger.info(f"Injected actor '{name}' into scene {scene_id}")
            return new_actor["id"]
