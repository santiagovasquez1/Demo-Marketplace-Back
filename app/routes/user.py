from fastapi import APIRouter
from clients.db import conn
from models.user import users
from models.schemas.user import User

from fastapi import HTTPException


from cryptography.fernet import Fernet

key=Fernet.generate_key()
f = Fernet(key=key)


user= APIRouter()
@user.get("/users", response_model=list[User], tags=["User"])
def get_users():
    result = conn.execute(users.select()).fetchall()
    return [dict(row._mapping) for row in result]







@user.post("/users", tags=["User"])
async def create_user(user: User):
    new_user=dict(user)
    new_user["password"]= f.encrypt(user.password.encode("utf-8"))
    try:
        conn.execute(users.insert().values(new_user))
        conn.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Error al crear el usuario.")



@user.get("/users/{user_id}", tags=["User"])
def get_user(user_id: int):
    s = users.select().where(users.c.user_id == user_id)
    result = conn.execute(s).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(result._mapping)



