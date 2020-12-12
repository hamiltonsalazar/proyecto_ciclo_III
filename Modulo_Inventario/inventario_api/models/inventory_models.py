from pydantic import BaseModel
#from datetime import datetime

class InventoryIn(BaseModel):
    id: int
    quantity: int
    price: int 
    discount: int

class InventoryOut(BaseModel):
    name: str
    price: int
    discount: int
    total_price: int