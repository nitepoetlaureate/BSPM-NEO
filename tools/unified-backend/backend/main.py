from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger
import sys

from backend.routers import discord
from backend.routers import watercooler

# Configure loguru
logger.remove()
logger.add(sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")

class Settings(BaseSettings):
    """Pydantic v2 Settings for the Studio Backend"""
    discord_token: str = "placeholder"
    huggingface_api_key: str = "placeholder"
    tailscale_ip: str = "127.0.0.1"

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

settings = Settings()

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
    logger.info(f"Routers mapped. Environment: Tailscale IP {settings.tailscale_ip}")

@app.get("/health")
async def health_check():
    return {"status": "online", "version": "0.1.0"}
