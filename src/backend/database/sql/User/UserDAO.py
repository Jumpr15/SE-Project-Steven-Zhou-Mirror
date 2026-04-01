from database.sql.User.UserSchema import User

from sqlmodel import select

def user_exists(
     username: str,
     session
):
     statement = select(User).where(User.username == username)
     user = session.exec(statement).first()
     if user is not None:
          return True
     return False

def get_user(
     username: str,
     session
):
     statement = select(User).where(User.username == username)
     user = session.exec(statement).first()
     return user

def get_user_conversations():
     pass

def insert_user(
     username: str,
     password: str,
     session
):
     user = User(
          username=username,
          password=password
     )
     session.add(user)
     session.commit()

def update_user(
     username: str,
     new_username: str,
     session
):
     statement = select(User).where(User.username == username)
     user = session.exec(statement).first()
     user.username = new_username
     session.add(user)
     session.commit()
     

def delete_user(
     username: str,
     session
):
     statement = select(User).where(User.username == username)
     user = session.exec(statement).first()
     session.delete(user)
     session.commit()

          
