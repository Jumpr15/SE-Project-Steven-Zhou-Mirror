from fastapi import APIRouter

from core.retrievalGeneration import retrievalGeneration

retrieval_router = APIRouter()

@retrieval_router.get("/retrieval/", tags=["retrieval"])
async def retrieval():
     return { "message" : "retrieval router"}

class retrieval_router:
     def __init__(self):
          self.router = APIRouter()
          
          self.retrievalGeneration = retrievalGeneration
          
          self.router.add_api_route(
               "/",
               endpoint=self.retrievalGeneration,
               methods=["GET"],
               tags=["retrieval"]
          )
          