from pydantic import BaseModel
from datetime import datetime

class UserIn(BaseModel):
    username: str

class UserOut(BaseModel):
    username: str