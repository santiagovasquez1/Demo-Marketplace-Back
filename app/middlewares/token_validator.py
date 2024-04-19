from models.schemas.token import TokenData
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv
load_dotenv()
from clients.db import conn
from models.user import users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user_email(username: str):
    
    user = conn.execute(users.select().where(users.c.email == username)).fetchone()
    return user

async def current_user(
        token: str = Depends(oauth2_scheme),
):
    credentials_exeptions= HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload= jwt.decode(
            token, os.getenv('SECRET_KEY'),algorithms=['HS256']
        )
        username = payload.get("sub")["email"]

        if username is None:
            raise credentials_exeptions
        token_data= TokenData(username=username)
    except JWTError:
        raise credentials_exeptions
    user=get_user_email(username= token_data.username)
    if user is None:
        raise credentials_exeptions
    return user


        


