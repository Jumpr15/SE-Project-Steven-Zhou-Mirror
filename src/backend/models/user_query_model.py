from pydantic import BaseModel

class UserQuery(BaseModel):
     query_text: str