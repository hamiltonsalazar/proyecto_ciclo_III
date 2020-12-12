from pydantic import BaseModel

class CustomerIn(BaseModel):
    username: str
    password: str

class CustomerOut(BaseModel):
    username: str
    name: str
    secondName: str
    lastname: str
    secondLastname: str
    address: str
    numberPhone: int

class CustomerUpdateIn(BaseModel):
    username: str
    password: str
    address: str
    numberPhone: int

class CustomerUpdateOut(BaseModel):
    username: str
    name: str
    secondName: str
    lastname: str
    secondLastname: str
    address: str
    numberPhone: int
