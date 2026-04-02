from auth.userAuth import userAuthorization

from database.sql.Conversation.ConversationDAO import insert_conversation
from database.sql.engine import session_dep

from model_inference.modelInference import model_inference
from models.user_query_model import UserQuery

import os
from dotenv import load_dotenv
from fastapi import Depends
import openai

load_dotenv()

async def directGeneration(
     query: UserQuery,
     session: session_dep,
     username: str = Depends(userAuthorization)
):
     openai_cli = openai.OpenAI(
          api_key=os.getenv("GROQ_API_KEY"),
          base_url="https://api.groq.com/openai/v1"
     )
     
     model = model_inference(
          openai_cli,
          "openai/gpt-oss-20b"
     ) 
     response = await model.text_generation(query.content)
     
     title = query.title
     if not title:
          title_prompt = "Generate a title of max 5 words that best fits the given query: "
          title = await model.text_generation(title_prompt + query.content)
     insert_conversation(query.username, title, session)
     
     return {
          "username": username,
          "title": title,
          "content": response
     }
     