from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

# Order Schemas
class OrderBase(BaseModel):
    symbol: str
    order_type: Literal['buy', 'sell', 'swap']
    quantity: int
    price: float
    timestamp: Optional[datetime] = None

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True  # This will make it work with SQLAlchemy ORM models
