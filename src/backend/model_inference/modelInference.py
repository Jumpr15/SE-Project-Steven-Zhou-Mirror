from ollama import chat
from typing import Optional

import os
from dotenv import load_dotenv

load_dotenv()

class model_inference:
     def __init__(
          self, 
          available_embedding_models: list[str] = ["snowflake-arctic-embed:137m"],
          available_inference_models: list[str] = ["smollm:360m", "sam860/LFM2:350m"],
          default_system_prompt: Optional[str] = os.getenv("DEFAULT_SYSTEM_PROMPT")
          
     ):
          self.available_embedding_models = available_embedding_models
          self.available_inference_models = available_inference_models
     
     async def text_generation(self, model_name , prompt_text):
          if model_name not in self.available_inference_models:
               model_name = self.available_inference_models[0]
               
          response = chat(
               model=model_name,
               messages=[
                    {
                         "role": "system",
                         "content": os.getenv("DEFAULT_SYSTEM_PROMPT")
                    },
                    {
                         "role": "user",
                         "content": prompt_text
                    }
               ]
          )
          
          return response["message"]["content"]

          
          # for chunk in streamed_response:
          #      return chunk['message']
          