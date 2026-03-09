from loguru import logger
import httpx

class CriticLoopEngine:
    """Orchestrates an adversarial debate between two agents until consensus is reached."""
    
    def __init__(self, api_url: str, api_token: str):
        self.api_url = api_url
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    async def run_loop(self, actor_prompt: str, critic_prompt: str, task: str, max_retries: int = 3):
        """Alternates between Actor and Critic until 'Approved.' is found or retries exhausted."""
        current_draft = ""
        last_critique = ""
        
        async with httpx.AsyncClient() as client:
            for i in range(max_retries):
                # 1. Actor Drafts (or revises)
                actor_payload = f"TASK: {task}\n\nPREVIOUS CRITIQUE: {last_critique}\n\nDRAFT YOUR SOLUTION:"
                current_draft = await self._call_llm(client, actor_prompt, actor_payload)
                
                logger.info(f"Actor-Critic Round {i+1}: Draft generated.")

                # 2. Critic Interrogates
                critic_payload = f"TASK: {task}\n\nDRAFT TO REVIEW: {current_draft}\n\nCRITIQUE THIS DRAFT (Type 'Approved.' if perfect):"
                last_critique = await self._call_llm(client, critic_prompt, critic_payload)
                
                if "Approved." in last_critique:
                    logger.info(f"Consensus reached in {i+1} rounds!")
                    return current_draft, last_critique
                
                logger.warning(f"Draft rejected by critic. Feedback: {last_critique[:100]}...")

        logger.error("Failed to reach consensus within max retries.")
        return current_draft, f"FAILED TO REACH CONSENSUS: {last_critique}"

    async def _call_llm(self, client: httpx.AsyncClient, system_prompt: str, user_payload: str) -> str:
        """Sends the HTTP request to the LLM Gateway."""
        data = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_payload}
            ],
            "max_tokens": 1500,
            "temperature": 0.2
        }
        
        try:
            response = await client.post(self.api_url, headers=self.headers, json=data, timeout=60.0)
            response.raise_for_status()
            
            # Assumes an OpenAI-compatible JSON schema response
            result = response.json()
            return result["choices"][0]["message"]["content"]
            
        except Exception as e:
            logger.error(f"LLM API Call failed: {e}")
            return "API_ERROR: Unable to communicate with LLM."
