from typing import Dict
from pydantic import BaseModel 

class InventoryInDB(BaseModel): 
    id: int
    name: str
    price: int 
    quantity: int
    discount: int
    total_price: int
    

database_inventory = Dict[int, InventoryInDB]

database_inventory = {100:InventoryInDB(**{"id":100,
                              "name": "PS5",
                              "price": 350,
                              "quantity": 2,
                              "discount": 0 ,
                              "total_price":400}),
                101:InventoryInDB(**{"id":101,
                              "name": "Xbox Series X",
                              "price": 250,
                              "quantity": 5,
                              "discount": 0,
                              "total_price":400}),  
                102:InventoryInDB(**{"id":102,
                              "name": "Nintendo Switch",
                              "price": 250,
                              "quantity":12,
                              "discount": 0,
                              "total_price":250  }),  
                              }

# get, nos devuelve None si no existe o un item del inventario si existe
def get_inventory(id: int): 
    if id in database_inventory.keys(): 
        return database_inventory[id]
    else: 
        return None


def update_inventory(inventory: InventoryInDB): 
    database_inventory[inventory.id] = inventory
    #database_inventory[inventory.id].quantity -= inventory.quantity
    return inventory
