from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from loguru import logger
import httpx
import os

router = APIRouter(prefix="/webhook/watercooler", tags=["watercooler"])

class ChatHistory(BaseModel):
    messages: list[str]
    context_topic: str = "general sprint discussion"

@router.post("/analyze")
async def eavesdrop_channel(history: ChatHistory):
    """Analyzes a block of chat messages using HF Inference to see if a specialist agent should intervene."""
    logger.info(f"Analyzing {len(history.messages)} recent messages for required interventions.")
    
    # We load settings directly or via env to avoid circular imports for now
    hf_url = os.getenv("HF_INFERENCE_URL")
    hf_token = os.getenv("HUGGINGFACE_API_KEY")
    
    if not hf_url or not hf_token:
        logger.error("HuggingFace credentials missing. Cannot eavesdrop.")
        raise HTTPException(status_code=500, detail="Inference credentials not configured.")

    chat_log = "\n".join(history.messages)
    
    prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are the Watercooler Bouncer. Read the following chat log. Does this conversation require a technical or artistic constraint to be mentioned?
Return ONLY the exact name of the agent who should intervene from this list: [art-director, engine-programmer, qa-lead].
If no intervention is needed, return 'NONE'.<|eot_id|><|start_header_id|>user<|end_header_id|>
CHAT LOG:
{chat_log}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 10, "temperature": 0.1}
    }
    
    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(hf_url, headers=headers, json=payload, timeout=10.0)
            response.raise_for_status()
            result = response.json()
            
            # Parse the generated text
            if isinstance(result, list) and "generated_text" in result[0]:
                raw_output = result[0]["generated_text"].replace(prompt, "").strip()
            else:
                raw_output = str(result)
                
            # Clean up the output to match our exact expected strings
            target = "NONE"
            for agent in ["art-director", "engine-programmer", "qa-lead"]:
                if agent in raw_output.lower():
                    target = agent
                    break

            logger.debug(f"Watercooler analysis result: Intervention by {target}")
            return {"intervention_required": target != "NONE", "agent_target": target}
            
    except Exception as e:
        logger.error(f"HF Inference failed: {e}")
        return {"intervention_required": False, "agent_target": "NONE", "error": str(e)}
