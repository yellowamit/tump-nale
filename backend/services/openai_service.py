import base64
from typing import Any, cast

from openai import AsyncOpenAI
from config import OPEN_AI_API_KEY

client = AsyncOpenAI(api_key=OPEN_AI_API_KEY)


async def generate_image(prompt: str, style_prompt: str, headshot_url: str) -> bytes:
    """use the responses api from image-gpt2 as a built in image generation tool.
    pass the headshot url directly as an input image
    return raw png bytes"""
    full_prompt = f" {style_prompt}\n\n"
    f"user_request: {prompt}\n\n"

    response = await client.responses.create(
        model="gpt-5.5",
        input=cast(
            Any,
            [{"role": "user", "content": [{"type": "text", "text": full_prompt}]}],
        ),
        tools=cast(
            Any,
            [{
                "type": "image_generation",
                "model": "image-gpt2",
                "size": "1536x1024",
                "quality": "medium",
                "output_format": "png",
            }],
        ),
    )
    for item in response.output:
        if item.type == "image_generation_call" and item.result:
            return base64.b64decode(item.result)

    raise RuntimeError("No image generated in the response")
