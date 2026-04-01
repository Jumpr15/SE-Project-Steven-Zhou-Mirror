from pydantic import BaseModel

class UserSignupForm(BaseModel):
     username: str
     password: str