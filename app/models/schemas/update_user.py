
from pydantic import BaseModel

class Update(BaseModel):
    user_id: int
    status:int

