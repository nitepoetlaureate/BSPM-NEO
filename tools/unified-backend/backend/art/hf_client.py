import argparse
import sys
import os
from typing import Optional
from gradio_client import Client
from loguru import logger
from PIL import Image

# Add the project root to sys.path to allow importing from scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../")))
from scripts.validate_assets import validate_image

class HFArtClient:
    """
    Client for interacting with RetroDiffusion on Hugging Face via Gradio.
    """
    
    def __init__(self, space_id: str = None):
        # Load from env if not provided
        self.space_id = space_id or os.getenv("RD_SPACE_ID", "anzorq/finetuned_diffusion")
        try:
            # We must pass the HF token if accessing a private space
            hf_token = os.getenv("HUGGINGFACE_API_KEY")
            self.client = Client(self.space_id, hf_token=hf_token)
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
            # RetroDiffusion prediction call
            result = self.client.predict(
                prompt,
                negative_prompt,
                steps,
                guidance_scale,
                seed,
                fn_index=0
            )
            
            if isinstance(result, tuple):
                image_path = result[0]
            else:
                image_path = result
                
            logger.info(f"Successfully generated image: {image_path}")
            return image_path
            
        except Exception as e:
            logger.error(f"Error during image generation: {e}")
            return None

def main():
    parser = argparse.ArgumentParser(description="Generate art using Hugging Face RetroDiffusion.")
    parser.add_argument("--prompt", type=str, required=True, help="The positive prompt for generation.")
    parser.add_argument("--negative_prompt", type=str, default="blurry, gradient, shadow, 3d, anti-aliased, complex texture, modern", help="The negative prompt.")
    parser.add_argument("--steps", type=int, default=20, help="Number of inference steps.")
    parser.add_argument("--guidance", type=float, default=7.0, help="Guidance scale (CFG).")
    parser.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random).")
    parser.add_argument("--output", type=str, help="Path to save the generated image.")
    parser.add_argument("--validate", action="store_true", help="Validate the generated image for GBC compatibility.")
    parser.add_argument("--is_sprite", action="store_true", help="Whether the generated image is a sprite (used for validation).")

    args = parser.parse_args()

    client = HFArtClient()
    image_path = client.generate_image(
        prompt=args.prompt,
        negative_prompt=args.negative_prompt,
        steps=args.steps,
        guidance_scale=args.guidance,
        seed=args.seed
    )

    if image_path:
        if args.output:
            import shutil
            shutil.copy(image_path, args.output)
            logger.info(f"Saved image to {args.output}")
            final_path = args.output
        else:
            final_path = image_path

        if args.validate:
            logger.info(f"Validating {final_path}...")
            is_valid = validate_image(final_path, is_sprite=args.is_sprite)
            if is_valid:
                logger.info("Validation PASSED.")
            else:
                logger.error("Validation FAILED.")
                sys.exit(1)
    else:
        logger.error("Image generation failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
