from clients.db import conn
from sqlalchemy import select
from fastapi import HTTPException
from models.tablas_models import Tables
from models.schemas.user import User
from models.schemas.update_user import Update   
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from middlewares.token_validator import get_user_email

class UserController:
    def __init__(self):
        self.Tables= Tables()
        
    def get_users(self):  
                query = select(self.Tables.users().c.user_id,self.Tables.users().c.status, self.Tables.users().c.NIT, self.Tables.users().c.company_name,
                self.Tables.users().c.contact, self.Tables.users().c.phone, self.Tables.users().c.email, self.Tables.users().c.address,
                self.Tables.users().c.password, self.Tables.regions().c.description.label("regions"), self.Tables.cities().c.description.label("cities"),self.Tables.agent().c.name.label("agent_name") )\
                .select_from(self.Tables.users().join(self.Tables.regions()).join(self.Tables.cities()).join(self.Tables.agent()))
                result = conn.execute(query).fetchall()
                return [dict(row._mapping) for row in result]
        


    async def update_user(self, update_data: Update):
        update_data= dict(update_data)
        update_query = self.Tables.users().update().where(self.Tables.users().c.user_id == update_data["user_id"]).values(
            status=update_data["status"]
        )
        conn.execute(update_query)
        return {"message": "User updated successfully"}
    

    async def create_user(self, user: User):
        new_user=dict(user)
        new_user["password"]= pwd_context.hash(user.password)
        get= get_user_email(new_user["email"])
        if get:
            raise HTTPException(status_code=400, detail="User email already register")
        try:
            conn.execute(self.Tables.users().insert().values(new_user))
            conn.commit()
            return {"message": "User created successfully"}
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=400, detail="Error creating a new user")
        

        
        
    async def get_user_byid(self,user_id: int):
        s = self.Tables.users().select().where(self.Tables.users().c.user_id == user_id)
        result = conn.execute(s).fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
        return dict(result._mapping)
