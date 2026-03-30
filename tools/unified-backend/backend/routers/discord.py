import subprocess
import asyncio
from fastapi import APIRouter, BackgroundTasks, Request
from loguru import logger
from pydantic import BaseModel
from backend.agents.config import AGENT_DEPARTMENT_MAP, Department

router = APIRouter(prefix="/webhook/discord", tags=["discord"])

class DiscordMessage(BaseModel):
    channel_id: str  # Channel name or ID
    username: str
    content: str
    attachments: list[str] = []

def run_agent_task(agent_name: str, content: str):
    logger.info(f"Triggering Gemini CLI agent: {agent_name}")
    try:
        # NATIVE CLI TRIGGER:
        # Command: gemini chat --agent <agent_name> -m "<content>"
        subprocess.run(["gemini", "chat", "--agent", agent_name, "-m", content], check=False)
    except Exception as e:
        logger.error(f"Failed to spawn agent CLI: {e}")

@router.post("")
async def handle_discord_webhook(msg: DiscordMessage, background_tasks: BackgroundTasks):
    """
    Entry point for Discord messages.
    Payload Format (JSON):
    {
        "channel_id": "string",
        "username": "string",
        "content": "string",
        "attachments": ["url1", "url2"]
    }
    """
    logger.info(f"Discord Message Received from {msg.username} in {msg.channel_id}")
    
    # Map Channel to Agent
    target_agent = "generalist"
    for agent_name in AGENT_DEPARTMENT_MAP.keys():
        if agent_name in msg.channel_id.lower():
            target_agent = agent_name
            break
    
    background_tasks.add_task(run_agent_task, target_agent, msg.content)
    
    return {"status": "accepted", "agent": target_agent}
