from models.user_signup_form_model import UserSignupForm

from auth.hashing import verify
from auth.token import create_jwt_token

from database.sql.User.UserDAO import get_user
from database.sql.engine import session_dep

from fastapi import status
from fastapi.responses import JSONResponse

async def userLogin(
     loginFormData: UserSignupForm,
     session: session_dep
):
     username = loginFormData.username
     password = loginFormData.password
     
     user = get_user(username, session)
     if user is None:
          return JSONResponse(
               status_code=status.HTTP_401_UNAUTHORIZED,
               content={
                    "error": "user not found"
               }
          )
     
     matching_passwords = verify(password, user.password)
     if matching_passwords is False:
          return JSONResponse(
               status_code=status.HTTP_401_UNAUTHORIZED,
               content={
                    "error": "incorrect password"
               }
          )
     
     access_token = create_jwt_token(username)
     
     return {
          "access_token": access_token,
          "token_type": "bearer"
     }
     