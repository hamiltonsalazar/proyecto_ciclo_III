from db.customer_db import CustomerInDB
from db.customer_db import update_customer, get_customer
from models.customer_models import CustomerIn, CustomerOut, CustomerUpdateIn, CustomerUpdateOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

@api.post("/customer/auth/")
async def auth_customer(customer_in: CustomerIn):
    customer_in_db = get_customer(customer_in.username)
    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    if customer_in_db.password != customer_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.get("/customer/fullName/{username}")
async def get_fullName(username: str):
    customer_in_db = get_customer(username)
    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    customer_out = CustomerOut(**customer_in_db.dict())
    return customer_out


@api.put("/user/transaction/")
async def make_transaction(customer_update_in: CustomerUpdateIn):
    customer_update_db = get_customer(customer_update_in.username)
    if customer_update_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    if customer_update_db.password != customer_update_in.password:
        return {"Autenticado": False}
    customer_update_db.address=customer_update_in.address
    customer_update_db.numberPhone=customer_update_in.numberPhone
    update_customer(customer_update_db)
    return customer_update_db
