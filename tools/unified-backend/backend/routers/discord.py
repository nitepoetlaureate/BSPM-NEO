from fastapi import APIRouter
from loguru import logger
from pydantic import BaseModel
from backend.agents.config import AGENT_DEPARTMENT_MAP, Department

router = APIRouter(prefix="/webhook/discord", tags=["discord"])

class DiscordMessage(BaseModel):
    channel_id: str  # Channel name or ID
    username: str
    content: str
    attachments: list[str] = []

@router.post("")
async def handle_discord_webhook(msg: DiscordMessage):
    """Entry point for PicoClaw messages from Discord."""
    logger.info(f"Discord Message Received from {msg.username} in {msg.channel_id}")
    
    # 1. Map Channel ID/Name to Department
    # Mapping logic: check if channel name contains department name
    target_dept = None
    for dept in Department:
        if dept.value.lower() in msg.channel_id.lower():
            target_dept = dept
            break
            
    if not target_dept:
        logger.warning(f"No department found for channel {msg.channel_id}. Defaulting to EXECUTIVE.")
        target_dept = Department.EXECUTIVE
    
    # 2. Trigger the appropriate Agentic workflow
    # This will later call the CriticLoopEngine with the correct department context
    return {
        "status": "accepted",
        "department": target_dept.value,
        "agent_roster_count": len([a for a, d in AGENT_DEPARTMENT_MAP.items() if d == target_dept])
    }
