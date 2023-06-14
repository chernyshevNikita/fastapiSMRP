from typing import List

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import Seller

SellerOut = sqlalchemy_to_pydantic(Seller)


class SellerIn(sqlalchemy_to_pydantic(Seller)):
    class Config:
        orm_mode = True





class SellersOut(BaseModel):
    sellers: List[SellerOut]