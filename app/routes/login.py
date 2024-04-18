# login.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from clients.db import conn
from models.user import users
from routes.user import pwd_context
from middlewares.token_creation import create_token
 

pwd_context=pwd_context

def verify_password(plain_password, hashed_password):
    return  pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    
    user = conn.execute(users.select().where(users.c.email == username)).fetchone()
    user = dict(user._mapping)

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if (user["status"]==0 or user["status"]==2 ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your User hasn´t been acepted or is pending",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user



login=router = APIRouter()

@login.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    access_token= create_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}



