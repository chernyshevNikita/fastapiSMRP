from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import SellerProductIn, SellerProductOut
from database import get_session, SellerProduct
from models.seller_product import SellerProductsOut

router = APIRouter(prefix="/prod_sel", tags=["prod_sel"])


@router.get("/get", response_model=SellerProductOut)
async def get_one(seller_id: int, product_id: int,
                  session: Session = Depends(get_session)):
    seller_product: SellerProduct = session.query(SellerProduct).get((seller_id, product_id))
    if seller_product:
        if seller_product.product_id == product_id:
            seller_product_dto = SellerProductOut(**seller_product.__dict__)
            return seller_product_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Seller with id {seller_id} not found!")


@router.get("/get_all", response_model=SellerProductsOut)
async def get_all():
    session = get_session()
    seller_products: SellerProduct = session.query(SellerProduct).all()
    seller_products_dto = list(map(lambda seller_product: SellerProductOut(**seller_product.__dict__), seller_products))
    return SellerProductsOut(sellers_products=seller_products_dto)


@router.post("/create_seller_product", response_model=SellerProductOut)
async def create_seller_product(seller_product: SellerProductIn):
    session = get_session()
    orm_seller_product = SellerProduct(**seller_product.dict())
    session.add(orm_seller_product)
    print(orm_seller_product.__dict__)
    session.commit()
    print(orm_seller_product.__dict__)
    seller_products_dto = SellerProductOut(**orm_seller_product.__dict__)
    return seller_products_dto


@router.delete("/delete_seller_product/{seller_id}/{product_id}", response_model=SellerProductOut)
async def delete_seller_product(seller_id: int, product_id: int, session: Session = Depends(get_session)):
    seller_product: SellerProduct = session.query(SellerProduct).get((seller_id, product_id))

    if seller_product:
        if seller_product.product_id == product_id:
            seller_product_dto = SellerProductOut(**seller_product.__dict__)
            session.delete(seller_product)
            session.commit()
            return seller_product_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Seller with id {seller_id} not found!")


@router.post("/update_selprod", response_model=SellerProductOut)
async def update_sel_prod(selprod: SellerProductIn):
    session = get_session()

    orm_selprod = session.query(SellerProduct).get((selprod.seller_id,selprod.product_id))
    #session.add(orm_client)
    orm_selprod.seller_id = selprod.seller_id
    orm_selprod.product_id = selprod.product_id

    #print(orm_client.__dict__)
    session.commit()
    #print(orm_client.__dict__)
    selprod_dto = SellerProductOut.from_orm(orm_selprod)
    return selprod_dto