from sqlmodel import SQLModel, Field

class Conversation(SQLModel, field=True):
     id: int | None = Field(default=None, primary_key=True)
     user_id: int = Field(index=True)
     title: str