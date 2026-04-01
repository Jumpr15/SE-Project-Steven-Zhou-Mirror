from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("NEON_POSTGRES_CONNECTION_STRING")


engine = create_engine(
     connection_string, 
     pool_pre_ping=True,
     echo=True
     )

def create_db_and_tables():
     SQLModel.metadata.create_all(engine)
     
def get_session():
     with Session(engine) as session:
          yield session

def ret_session():
     with Session(engine) as session:
          return session
          
# create session dependency
session_dep = Annotated[Session, Depends(get_session)]