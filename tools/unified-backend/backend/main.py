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

from typing import Optional

class Settings(BaseSettings):
    """Pydantic v2 Settings for the Studio Backend with Graceful Degradation"""
    discord_token: Optional[str] = Field(None, repr=False, description="Discord Bot Token (Optional for local dev)")
    huggingface_api_key: Optional[str] = Field(None, repr=False, description="HF PRO Token (Optional for local dev)")
    hf_inference_url: Optional[str] = Field(None, repr=False, description="URL for Llama-3 or chosen chat model")
    rd_endpoint_url: Optional[str] = Field(None, repr=False, description="URL for the Private RetroDiffusion Space")
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
