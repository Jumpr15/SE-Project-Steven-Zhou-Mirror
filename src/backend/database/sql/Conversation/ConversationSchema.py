from sqlmodel import SQLModel, Field

class Conversation(SQLModel, table=True):
     id: int | None = Field(default=None, primary_key=True)
     user_id: int | None = Field(default=None, foreign_key="user.id", index=True)
     title: str