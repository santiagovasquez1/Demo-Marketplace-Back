
from pydantic import BaseModel

class User(BaseModel):
    status:int
    NIT:int
    company_name: str
    contact: str
    phone: int
    email: str
    region:int
    city:int
    agent_id:int
    address: str
    password: str

