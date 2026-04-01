from auth.token import verify_token

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def userAuthorization(
     token = Depends(oauth2_scheme)
):
     payload = verify_token(token)
     username = payload.get("sub")
     return username
     