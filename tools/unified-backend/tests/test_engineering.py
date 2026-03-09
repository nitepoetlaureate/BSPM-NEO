from unittest.mock import patch, MagicMock
from backend.engineering.build_runner import GBStudioBuildRunner

@patch("subprocess.run")
def test_compile_rom_command_construction(mock_run, tmp_path):
    # Mock successful run
    mock_run.return_value = MagicMock(stdout="Success", returncode=0)
    
    project_path = tmp_path / "project.gbsproj"
    build_dir = tmp_path / "build"
    
    runner = GBStudioBuildRunner(str(project_path), str(build_dir))
    runner.compile_rom()
    
    # Assert the command was built correctly using npx
    args = mock_run.call_args[0][0]
    assert args[0] == "npx"
    assert args[1] == "gb-studio-cli"
    assert args[2] == "make:rom"
    assert "-c" in args
    assert str(project_path) in args
