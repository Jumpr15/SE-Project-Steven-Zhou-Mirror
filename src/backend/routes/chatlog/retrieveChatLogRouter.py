from fastapi import APIRouter

from core.retrieveChatLog import retrieveChatLog

class retreive_chat_log_router:
     def __init__(self):
          self.router = APIRouter()
          
          self.retrieveChatLog = retrieveChatLog
          
          self.router.add_api_route(
               "/",
               endpoint=self.retrieveChatLog,
               methods=["POST"],
               tags=["chatlog"]
          )
