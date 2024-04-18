
from pydantic import BaseModel,EmailStr

class User(BaseModel):
    status:int
    NIT:int
    company_name: str
    contact: str
    phone: int
    email: EmailStr
    region:int
    city:int
    agent_id:int
    address: str
    password: str

