from fastapi import APIRouter, HTTPException
from clients.db import conn
from models.user import users
from models.schemas.user import User
from passlib.context import CryptContext
from fastapi import HTTPException
from middlewares.token_validator import get_user_email
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


user= APIRouter()
@user.get("/users", tags=["User"])
def get_users():
    result = conn.execute(users.select()).fetchall()
    return [dict(row._mapping) for row in result]



@user.post("/users", tags=["User"])
async def create_user(user: User):
    new_user=dict(user)
    new_user["password"]= pwd_context.hash(user.password)
    get= get_user_email(new_user["email"])
    if get:
        raise HTTPException(status_code=400, detail="User email already register")
    try:
        conn.execute(users.insert().values(new_user))
        conn.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Error creating a new user")



@user.get("/users/{user_id}", tags=["User"])
async def get_user(user_id: int):
    s = users.select().where(users.c.user_id == user_id)
    result = conn.execute(s).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(result._mapping)



