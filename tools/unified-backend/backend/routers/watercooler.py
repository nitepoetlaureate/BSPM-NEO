from fastapi import APIRouter
from pydantic import BaseModel
from loguru import logger

router = APIRouter(prefix="/webhook/watercooler", tags=["watercooler"])

class ChatHistory(BaseModel):
    messages: list[str]
    context_topic: str = "general sprint discussion"

@router.post("/analyze")
async def eavesdrop_channel(history: ChatHistory):
    """Analyzes a block of chat messages to see if a specialist agent should intervene."""
    logger.info(f"Analyzing {len(history.messages)} recent messages for required interventions.")
    
    chat_log = "\n".join(history.messages)
    
    # Heuristic for the scaffold: classification based on keywords
    if "colors" in chat_log.lower() or "palette" in chat_log.lower():
        target = "art-director"
    elif "actors" in chat_log.lower() or "limit" in chat_log.lower():
        target = "engine-programmer"
    else:
        target = "NONE"

    logger.debug(f"Watercooler analysis result: Intervention by {target}")
    
    return {"intervention_required": target != "NONE", "agent_target": target}
