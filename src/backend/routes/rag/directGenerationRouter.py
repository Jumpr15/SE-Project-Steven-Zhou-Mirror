from fastapi import APIRouter

from core.directGeneration import directGeneration

class direct_generation_router:
     def __init__(self):
          self.router = APIRouter()
          
          self.directGeneration = directGeneration
          
          self.router.add_api_route(
               "/",
               endpoint=self.directGeneration,
               methods=["GET", "POST"],
               tags=["generation"]
          )
          