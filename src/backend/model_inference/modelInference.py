from ollama import chat
from typing import Optional

import os
from dotenv import load_dotenv

load_dotenv()

class model_inference:
     def __init__(
          self,
          openai_client,
          model
     ):
          self.openai = openai_client
          self.model = model
          
     async def text_generation(self, prompt):
          response = self.openai.responses.create(
               model="openai/gpt-oss-20b",
               input=prompt
          )
          
          return response.output_text
          
