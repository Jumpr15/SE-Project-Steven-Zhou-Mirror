from database.sql.User.UserSchema import User
from database.sql.Conversation.ConversationSchema import Conversation

from sqlmodel import select

def insert_conversation(
    username: str,
    title: str,
    session
):
     statement = select(User).where(User.username == username)
     user = session.exec(statement).first()
     
     conversation = Conversation(
          user_id=user.id,
          title=title
     )
     session.add(user)
     session.commit()
     
def 
     