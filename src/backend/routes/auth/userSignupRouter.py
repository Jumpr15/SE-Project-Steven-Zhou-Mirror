from fastapi import APIRouter, Depends

from auth.userSignup import userSignup

class signup_router:
     def __init__(self):
          self.router = APIRouter()
          
          self.userSignup = userSignup
          
          self.router.add_api_route(
               "/",
               endpoint=self.userSignup,
               methods=["POST"],
               tags=["auth", "signup"]
          )