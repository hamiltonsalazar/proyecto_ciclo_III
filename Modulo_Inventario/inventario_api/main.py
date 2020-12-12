import math
from db.user_db import UserInDB 
from db.inventory_db import InventoryInDB 
from db.inventory_db import get_inventory,update_inventory
from models.user_models import UserIn, UserOut
from models.inventory_models import InventoryIn, InventoryOut


#import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

# obtener producto del inventario
@api.get("/producto/{inventory_id}")
async def inventory_get(inventory_id: int): 
    inventory_in = get_inventory(inventory_id) 
    if inventory_in == None: 
        raise HTTPException (status_code=404,
                detail="el producto no fue encontrado en el inventario") 
    inventory_out = InventoryOut(**inventory_in.dict())
    return inventory_out


# actualizar producto
@api.put("/producto")
async def product_update(inventory: InventoryIn): 
    inventory_in = get_inventory(inventory.id)
    if inventory_in == None: 
        return None 
    inventory_in.total_price = math.ceil((inventory.price/100)*(100-inventory.discount))
    inventory_in.price = inventory.price 
    inventory_in.quantity =  inventory.quantity
    inventory_in.discount = inventory.discount 
    update_inventory(inventory_in)
    inventory_out = InventoryOut(**inventory_in.dict())
    return inventory_out
    