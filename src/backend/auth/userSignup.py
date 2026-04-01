from models.user_signup_form_model import UserSignupForm

from auth.hashing import hash
from auth.token import create_jwt_token

from database.sql.User.UserDAO import user_exists, insert_user
from database.sql.engine import session_dep

from fastapi import status
from fastapi.responses import JSONResponse

async def userSignup(
     signupFormData: UserSignupForm,
     session: session_dep
):
     username = signupFormData.username
     password = signupFormData.password
     
     exists = user_exists(username, session)
     if exists is True:
          return JSONResponse(
               status_code=status.HTTP_409_CONFLICT,
               content={
                    "error": "Username already exists"
               }
          )
          
     insert_user(username, hash(password), session)
          
     access_token = create_jwt_token(username)
     
     return {
          "access_token": access_token,
          "token_type": "bearer"
     }