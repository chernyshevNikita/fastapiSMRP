from typing import List

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import OrderItems

OrderItemOut = sqlalchemy_to_pydantic(OrderItems)


class OrderItemIn(sqlalchemy_to_pydantic(OrderItems)):
    class Config:
        orm_mode = True


class OrderItemsOut(BaseModel):
    order_items: List[OrderItemOut]