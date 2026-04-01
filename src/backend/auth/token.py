from dotenv import load_dotenv
from fastapi import HTTPException, status
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
import jwt 
import datetime
import os

load_dotenv()

ENCRYPTION_ALGORITHM = "HS256"
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
EXPIRY_TIME_MINUTES = 15

credentials_exception = HTTPException(
     status_code=status.HTTP_401_UNAUTHORIZED,
     detail="Could not validate credentials",
     headers={"WWW-Authenticate": "Bearer"}
)

def create_jwt_token(username):
     payload = {
          "sub": username,
          "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=EXPIRY_TIME_MINUTES)
     }
     token = jwt.encode(payload, SECRET_KEY, algorithm=ENCRYPTION_ALGORITHM)
     return token

def verify_token(token):
     try:
          return jwt.decode(token, SECRET_KEY, algorithms=[ENCRYPTION_ALGORITHM])
     except ExpiredSignatureError:
          raise credentials_exception
     except InvalidTokenError:
          raise credentials_exception