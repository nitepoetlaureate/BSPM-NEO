from typing import Optional
from gradio_client import Client
from loguru import logger

class HFArtClient:
    """
    Client for interacting with RetroDiffusion on Hugging Face via Gradio.
    """
    
    def __init__(self, space_id: str = "astropulse/RetroDiffusion"):
        self.space_id = space_id
        try:
            self.client = Client(self.space_id)
            logger.info(f"Connected to Hugging Face space: {self.space_id}")
        except Exception as e:
            logger.error(f"Failed to connect to Hugging Face space {self.space_id}: {e}")
            self.client = None

    def generate_image(
        self, 
        prompt: str, 
        negative_prompt: str = "blurry, gradient, shadow, 3d, anti-aliased, complex texture, modern",
        steps: int = 20,
        guidance_scale: float = 7.0,
        seed: int = -1
    ) -> Optional[str]:
        """
        Generates an image using RetroDiffusion.
        
        Args:
            prompt: The positive prompt for generation.
            negative_prompt: The negative prompt to avoid unwanted features.
            steps: Number of inference steps.
            guidance_scale: CFG scale.
            seed: Random seed for generation (-1 for random).
            
        Returns:
            The path to the generated image file, or None if failed.
        """
        if not self.client:
            logger.error("HF Client not initialized.")
            return None
            
        try:
            # Note: RetroDiffusion API parameters might vary. 
            # This is a standard prediction call for many Gradio SD spaces.
            # Using keyword arguments if the API supports it, or positional.
            # Most RetroDiffusion spaces use 'predict' with specific indices.
            result = self.client.predict(
                prompt,
                negative_prompt,
                steps,
                guidance_scale,
                seed,
                fn_index=0 # Defaulting to the first function
            )
            
            # Gradio usually returns a tuple or a single string (path)
            if isinstance(result, tuple):
                image_path = result[0]
            else:
                image_path = result
                
            logger.info(f"Successfully generated image: {image_path}")
            return image_path
            
        except Exception as e:
            logger.error(f"Error during image generation: {e}")
            return None

if __name__ == "__main__":
    # Quick manual test
    client = HFArtClient()
    res = client.generate_image("pixel art, barry sharp, game boy color style")
    print(f"Result: {res}")
