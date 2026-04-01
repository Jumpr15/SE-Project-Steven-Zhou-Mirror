from fastapi import APIRouter

from auth.userLogin import userLogin

class login_router:
     def __init__(self):
          self.router = APIRouter()
          
          self.userLogin = userLogin
          
          self.router.add_api_route(
               "/",
               endpoint=self.userLogin,
               methods=["POST"],
               tags=["auth", "signup"]
          )