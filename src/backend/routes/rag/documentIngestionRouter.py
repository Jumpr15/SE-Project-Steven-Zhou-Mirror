from fastapi import APIRouter

from core.documentIngestion import documentIngestion

class ingestion_router:
     def __init__(self):
          self.router = APIRouter()
      
          self.documentIngestion = documentIngestion   
           
          self.router.add_api_route(
               "/",
               endpoint=self.documentIngestion,
               methods=["POST"],
               tags=["ingestion"]
          )
          
          
     