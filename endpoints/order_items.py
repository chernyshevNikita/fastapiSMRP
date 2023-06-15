from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import OrderItemOut, OrderItemIn
from database import get_session, OrderItems,Product
from models.order_items import OrderItemsOut

router = APIRouter(prefix="/order_item", tags=["order_item"])


@router.get("/get", response_model=OrderItemOut)
async def get_one(product_id: int, order_id: int,
                  session: Session = Depends(get_session)):
    order_item: OrderItems = session.query(OrderItems).get((order_id, product_id))
    if order_item:
        if order_item.product_id == product_id:
            order_item_dto = OrderItemOut(**order_item.__dict__)
            return order_item_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Order with id {order_id} not found!")


@router.get("/get_all", response_model=OrderItemsOut)
async def get_all():
    session = get_session()
    order_items: OrderItems = session.query(OrderItems).all()
    order_items_dto = list(map(lambda order_item: OrderItemOut(**order_item.__dict__), order_items))
    return OrderItemsOut(order_items=order_items_dto)


@router.post("/create_order_item", response_model=OrderItemOut)
async def create_order_item(order_item: OrderItemIn):
    session = get_session()
    orm_order_item = OrderItems(**order_item.dict())
    id_ = order_item.product_id
    prod = session.query(Product).get(id_)
    orm_order_item.product_price = prod.price
    session.add(orm_order_item)
    session.commit()
    order_item_dto = OrderItemOut(**orm_order_item.__dict__)
    return order_item_dto


@router.post("/update_order_item", response_model=OrderItemOut)
async def update_order_item(order_item: OrderItemIn):
    session = get_session()

    orm_order_item = session.query(OrderItems).get((order_item.order_id,order_item.product_id))
    orm_order_item.product_count = order_item.product_count
    id_ = order_item.product_id
    prod = session.query(Product).get(id_)
    orm_order_item.product_price = prod.price
    session.commit()
    order_item_dto = OrderItemOut.from_orm(orm_order_item)
    return order_item_dto


@router.delete("/delete_order_item/{order_id}/{product_id}", response_model=OrderItemOut)
async def delete_order_item(order_id: int,product_id: int , session: Session = Depends(get_session)):
    order_item: OrderItems = session.query(OrderItems).get((order_id, product_id))
    if order_item:
        order_item_dto = OrderItemOut(**order_item.__dict__)
        session.delete(order_item)
        session.commit()
        return order_item_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Order with id {order_id} not found!")