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
from middlewares.token_validator import get_user_email
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


user= APIRouter()
@user.get("/users", tags=["User"])
def get_users():
    query = select(users.c.user_id,users.c.status, users.c.NIT, users.c.company_name,
               users.c.contact, users.c.phone, users.c.email, users.c.address,
               users.c.password, regions.c.description.label("regions"), cities.c.description.label("cities"),agent.c.name.label("agent_name") )\
    .select_from(users.join(regions).join(cities).join(agent))
    result = conn.execute(query).fetchall()
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



@user.put("/update/{update}", tags=["User"])
async def update_user(update_data: Update):
    update_data= dict(update_data)
    update_query = users.update().where(users.c.user_id == update_data["user_id"]).values(
        status=update_data["status"]
    )
    conn.execute(update_query)
    return {"message": "User updated successfully"}

    