from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import SellerIn, SellerOut
from database import get_session, Seller
from models.seller import SellersOut

router = APIRouter(prefix="/seller", tags=["seller"])


@router.get("/{seller_id}", response_model=SellerOut)
async def get_one(seller_id: int,
                  session: Session = Depends(get_session)):
    seller: Seller = session.query(Seller).get(seller_id)
    if seller:
        seller_dto = SellerOut(**seller.__dict__)
        return seller_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Seller with id {seller_id} not found!")


@router.get("/get_all", response_model=SellersOut)
async def get_all():
    session = get_session()
    sellers: Seller = session.query(Seller).all()
    sellers_dto = list(map(lambda seller: SellerOut(**seller.__dict__), sellers))
    return SellersOut(sellers=sellers_dto)


@router.post("/create_seller", response_model=SellerOut)
async def create_seller(seller: SellerIn):
    session = get_session()
    orm_seller = Seller(**seller.dict())
    session.add(orm_seller)
    print(orm_seller.__dict__)
    session.commit()
    print(orm_seller.__dict__)
    seller_dto = SellerOut(**orm_seller.__dict__)
    return seller_dto


@router.delete("/delete_seller/{seller_id}", response_model=SellerOut)
async def delete_seller(seller_id: int, session: Session = Depends(get_session)):
    seller: Seller = session.query(Seller).get(seller_id)
    if seller:
        seller_dto = SellerOut(**seller.__dict__)
        session.delete(seller)
        session.commit()
        return seller_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Seller with id {seller_id} not found!")

@router.post("/update_seller", response_model=SellerOut)
async def update_seller(seller: SellerIn):
    session = get_session()

    orm_seller = session.query(Seller).get(seller.seller_id)
    #session.add(orm_client)
    orm_seller.seller_name = seller.seller_name
    orm_seller.rating = seller.rating
    orm_seller.store_id = seller.store_id

    print(orm_seller.__dict__)
    session.commit()
    print(orm_seller.__dict__)
    seller_dto = SellerOut.from_orm(orm_seller)
    return seller_dto
