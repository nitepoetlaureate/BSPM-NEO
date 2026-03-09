import pytest
from unittest.mock import MagicMock, patch
import os
from backend.art.hf_client import HFArtClient
from backend.art.aseprite_cli import AsepriteCLI

@pytest.fixture
def mock_gradio_client():
    with patch("backend.art.hf_client.Client") as mock_client:
        yield mock_client

def test_hf_client_initialization(mock_gradio_client):
    """
    Test that HFArtClient initializes correctly.
    """
    client = HFArtClient(space_id="test/space")
    mock_gradio_client.assert_called_once_with("test/space")
    assert client.space_id == "test/space"

def test_hf_client_generate_image(mock_gradio_client):
    """
    Test image generation with HFArtClient.
    """
    # Mock the Client instance and its predict method
    mock_instance = MagicMock()
    mock_gradio_client.return_value = mock_instance
    mock_instance.predict.return_value = "path/to/generated/image.png"
    
    client = HFArtClient(space_id="test/space")
    result = client.generate_image("pixel art, barry sharp")
    
    # Check if predict was called with correct arguments
    mock_instance.predict.assert_called_once()
    assert result == "path/to/generated/image.png"

def test_hf_client_failed_initialization():
    """
    Test HFArtClient behavior when Gradio Client fails to initialize.
    """
    with patch("backend.art.hf_client.Client", side_effect=Exception("Connection failed")):
        client = HFArtClient(space_id="test/space")
        assert client.client is None
        
        result = client.generate_image("test prompt")
        assert result is None

@pytest.fixture
def mock_subprocess_run():
    with patch("subprocess.run") as mock_run:
        yield mock_run

def test_aseprite_cli_process_image(mock_subprocess_run):
    """
    Test image processing with AsepriteCLI.
    """
    # Create a temporary input file to satisfy os.path.exists check
    input_path = "test_input.png"
    output_path = "test_output.png"
    
    with open(input_path, "w") as f:
        f.write("dummy content")
    
    try:
        cli = AsepriteCLI(aseprite_path="dummy_aseprite")
        
        # Mock subprocess.run success
        mock_subprocess_run.return_value = MagicMock(returncode=0)
        
        # Mock output file creation
        with patch("os.path.exists", side_effect=lambda p: True if p in [input_path, output_path] else os.path.exists(p)):
            # We need to create the output file so the existence check passes
            with open(output_path, "w") as f:
                f.write("dummy output")
                
            success = cli.process_image(input_path, output_path)
            
            assert success is True
            mock_subprocess_run.assert_called_once()
            args = mock_subprocess_run.call_args[0][0]
            assert "dummy_aseprite" in args
            assert "--palette" in args
            assert "--resize" in args
            assert "160,144" in args
            
    finally:
        # Cleanup
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)

def test_aseprite_cli_file_not_found():
    """
    Test AsepriteCLI error handling when input file doesn't exist.
    """
    cli = AsepriteCLI()
    success = cli.process_image("non_existent.png", "output.png")
    assert success is False
