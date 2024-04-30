from fastapi import APIRouter, HTTPException
from clients.db import conn
from models.user import users
from models.regions import regions
from models.cities import cities
from models.agents import agent
from models.schemas.update_user import Update   
from sqlalchemy import select
from models.schemas.user import User
from passlib.context import CryptContext
from controllers.user_controller import UserController
from middlewares.token_validator import get_user_email
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



    
user= APIRouter()

@user.get("/users", tags=["User"])
def get_users():
    return UserController().get_users()



@user.post("/users", tags=["User"])
async def create_user(user: User):
    return await UserController().create_user(user)



@user.get("/users/{user_id}", tags=["User"])
async def get_user(user_id: int):
    return await UserController().get_user_byid(user_id)


@user.put("/update", tags=["User"])
async def update_user(update_data: Update):
    return await UserController().update_user(update_data)


    