import pytest
import json
import pathlib
import shutil
from backend.engineering.injector import GBProjInjector
from backend.engineering.gbsproj_validator import GBProjValidator

@pytest.fixture
def mock_project(tmp_path):
    project_path = tmp_path / "test_project.gbsproj"
    with open(project_path, "w", encoding="utf-8") as f:
        json.dump({
            "_resourceType": "project",
            "scenes": [],
            "backgrounds": [],
            "sprites": [],
            "settings": {}
        }, f)
    return project_path

def test_inject_scene_success(mock_project):
    injector = GBProjInjector(str(mock_project))
    scene_id = injector.inject_scene("Test Scene", "bg_id")
    
    assert scene_id is not None
    with open(mock_project, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data["scenes"]) == 1
        assert data["scenes"][0]["name"] == "Test Scene"

def test_inject_scene_rollback_on_validation_failure(mock_project, monkeypatch):
    injector = GBProjInjector(str(mock_project))
    
    # Inject one good scene first
    injector.inject_scene("Good Scene", "bg_id")
    
    # Mock validation failure
    monkeypatch.setattr(GBProjValidator, "validate_file", lambda path: False)
    
    with pytest.raises(RuntimeError, match="Injection failed validation"):
        injector.inject_scene("Failing Scene", "bg_id")
        
    # Verify rollback
    with open(mock_project, "r", encoding="utf-8") as f:
        data = json.load(f)
        scene_names = [s["name"] for s in data["scenes"]]
        assert "Good Scene" in scene_names
        assert "Failing Scene" not in scene_names

def test_inject_actor_rollback_on_validation_failure(mock_project, monkeypatch):
    injector = GBProjInjector(str(mock_project))
    
    # Inject a scene first
    scene_id = injector.inject_scene("Scene", "bg_id")
    
    # Mock validation failure for actor injection
    monkeypatch.setattr(GBProjValidator, "validate_file", lambda path: False)
    
    with pytest.raises(RuntimeError, match="Actor injection failed validation"):
        injector.inject_actor(scene_id, "Failing Actor", "sprite_id", 0, 0)
        
    # Verify rollback
    with open(mock_project, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data["scenes"][0]["actors"]) == 0
