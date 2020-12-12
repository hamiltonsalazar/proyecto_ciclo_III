from typing import Dict
from pydantic import BaseModel

class CustomerInDB(BaseModel):
    username: str
    password: str
    name: str
    secondName: str
    lastname: str
    secondLastname: str    
    address: str
    numberPhone: int
    
database_customers = Dict[str, CustomerInDB]

database_customers = {
    "camilo24": CustomerInDB(**{"username":"camilo24",
                            "password":"cami24",
                            "name": "Camilo",
                            "secondName": "",
                            "lastname": "Giraldo",
                            "secondLastname": "Sanchez",
                            "address": "",
                            "numberPhone": 0}),
    "hamilton22": CustomerInDB(**{"username":"hamilton22",
                            "password":"smith22",
                            "name": "Hamilton",
                            "secondName": "Smith",
                            "lastname": "Carvajal",
                            "secondLastname": "Salazar",
                            "address": "",
                            "numberPhone": 0}),
    "nico": CustomerInDB(**{"username":"nico",
                            "password":"nico20",
                            "name": "Nicolas",
                            "secondName": "Raúl",
                            "lastname": "Rojas",
                            "secondLastname": "Ferias",
                            "address": "",
                            "numberPhone": 0}),
    "diegoDD": CustomerInDB(**{"username":"diegoDD",
                            "password":"dd05",
                            "name": "Diego",
                            "secondName": "Aramando",
                            "lastname": "Diaz",
                            "secondLastname": "Diaz",
                            "address": "",
                            "numberPhone": 0}),
}

def get_customer(username: str):
    if username in database_customers.keys():
        return database_customers[username]
    else:
        return None

def update_customer(customer_in_db: CustomerInDB):
    database_customers[customer_in_db.username] = customer_in_db
    return customer_in_db