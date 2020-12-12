#from typing import Dict
from pydantic import BaseModel 

class UserInDB(BaseModel):
    username: str
