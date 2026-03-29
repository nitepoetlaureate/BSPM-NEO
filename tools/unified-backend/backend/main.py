from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from loguru import logger
import sys

from backend.routers import discord
from backend.routers import watercooler

# Configure loguru
logger.remove()
logger.add(sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")

class Settings(BaseSettings):
    """Pydantic v2 Settings for the Studio Backend with Strict Vault Enforcement"""
    discord_token: str = Field(..., min_length=20, repr=False, description="Must be a valid Discord Bot Token")
    huggingface_api_key: str = Field(..., min_length=10, repr=False, description="Must be a valid HF PRO Token")
    hf_inference_url: str = Field(..., repr=False, description="URL for Llama-3 or chosen chat model")
    rd_endpoint_url: str = Field(..., repr=False, description="URL for the Private RetroDiffusion Space")
    tailscale_ip: str = Field("127.0.0.1", description="Local or Tailscale IP")

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

settings = Settings()  # type: ignore

# Initialize FastAPI
app = FastAPI(
    title="CCGS Studio Backend",
    description="The routing brain for the Atomic AI Studio",
    version="0.1.0"
)

# Mount the Routers
app.include_router(discord.router)
app.include_router(watercooler.router)

@app.on_event("startup")
async def startup_event():
    logger.info("CCGS Backend is waking up...")
    logger.info("Vault unlocked. Secrets loaded securely.")
    logger.info(f"Routers mapped. Environment: Tailscale IP {settings.tailscale_ip}")

@app.get("/health")
async def health_check():
    return {"status": "online", "version": "0.1.0"}
