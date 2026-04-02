
import subprocess
import os
import sys
import time
import argparse
import socket
from loguru import logger

RD_PATH = "/Users/michaelraftery/Library/Application Support/Aseprite/extensions/RetroDiffusion/"
PYTHON_EXEC = os.path.join(RD_PATH, "stable-diffusion-aseprite/venv/bin/python3")
SERVER_SCRIPT = os.path.join(RD_PATH, "stable-diffusion-aseprite/main.py")
ASEPRITE_EXEC = "/usr/local/bin/aseprite"
BRIDGE_SCRIPT = "tools/rd_headless_bridge.lua"

def is_server_running(port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0

def start_server():
    if is_server_running():
        logger.info("RD Server already running.")
        return None
    
    logger.info("Starting RetroDiffusion Server (CPU mode)...")
    # We run it in the background
    process = subprocess.Popen(
        [PYTHON_EXEC, SERVER_SCRIPT],
        cwd=os.path.dirname(SERVER_SCRIPT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # Wait for server to wake up
    max_wait = 60
    for i in range(max_wait):
        if is_server_running():
            logger.info("RD Server is UP.")
            return process
        time.sleep(1)
    
    logger.error("Failed to start RD Server within 60s")
    return None

def main():
    parser = argparse.ArgumentParser(description="Art Forge: Automated RetroDiffusion CLI")
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--width", type=int, default=16)
    parser.add_argument("--height", type=int, default=16)
    args = parser.parse_args()

    # 1. Ensure Server is running
    server_process = start_server()

    # 2. Run Aseprite Bridge
    logger.info(f"Triggering Aseprite for: {args.prompt}")
    command = [
        ASEPRITE_EXEC,
        "-b",
        "--script-param", f"prompt={args.prompt}",
        "--script-param", f"output={args.output}",
        "--script-param", f"width={args.width}",
        "--script-param", f"height={args.height}",
        "--script", BRIDGE_SCRIPT
    ]
    
    try:
        # High timeout for CPU generation
        result = subprocess.run(command, capture_output=True, text=True, timeout=600)
        print(result.stdout)
        if result.returncode != 0:
            logger.error(f"Aseprite failed: {result.stderr}")
            sys.exit(1)
    except subprocess.TimeoutExpired:
        logger.error("Generation timed out.")
        sys.exit(1)

    # 3. Post-Process (Quantization)
    if os.path.exists(args.output):
        logger.info("Running GBC Quantization...")
        quant_cmd = ["python3", "tools/unified-backend/backend/art/scripts/quantize_gbc.py", args.output, args.output]
        subprocess.run(quant_cmd)
        
        logger.info("Running Asset Validation...")
        val_cmd = ["python3", "scripts/validate_assets.py"]
        subprocess.run(val_cmd)
        
        logger.info(f"SUCCESS: Art Forge completed. Asset ready at {args.output}")
    else:
        logger.error("Output file not found after generation.")
        sys.exit(1)

    # We leave the server running for subsequent calls

if __name__ == "__main__":
    main()
