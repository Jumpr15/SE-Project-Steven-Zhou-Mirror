from typing import Annotated
from fastapi import Depends


async def retrieveChatLog(
     user: str
):
     return {
          "message": "retrieve chat log core function",
          "user": user
     }