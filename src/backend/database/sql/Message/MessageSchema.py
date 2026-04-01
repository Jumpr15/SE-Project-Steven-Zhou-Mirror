from sqlmodel import SQLModel, Field

class Message(SQLModel, table=True):
     id: int | None = Field(default=None, primary_key=True)
     conversation_id: int
     role: str
     content: str