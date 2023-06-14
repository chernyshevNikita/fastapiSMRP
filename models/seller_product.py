from typing import List

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import SellerProduct

SellerProductOut = sqlalchemy_to_pydantic(SellerProduct)


class SellerProductIn(sqlalchemy_to_pydantic(SellerProduct)):
    class Config:
        orm_mode = True


#SellerProductIn.__fields__.pop('seller_id')
#print(SellerProductIn.__fields__)


class SellerProductsOut(BaseModel):
    sellers_products: List[SellerProductOut]