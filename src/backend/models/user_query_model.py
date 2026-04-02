from pydantic import BaseModel

class UserQuery(BaseModel):
     username: str
     title: str
     content: str