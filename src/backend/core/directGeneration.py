from auth.userAuth import userAuthorization

from model_inference.modelInference import model_inference
from models.user_query_model import UserQuery

from fastapi import Depends

async def directGeneration(
     query: UserQuery,
     username: str = Depends(userAuthorization)
):
     model = model_inference() 
     response = await model.text_generation("sam860/LFM2:350m", query.query_text)
     
     return {
          "usernmae": username,
          "content": response
     }
     