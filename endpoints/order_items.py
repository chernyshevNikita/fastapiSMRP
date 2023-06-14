from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import OrderItemOut, OrderItemIn
from database import get_session, OrderItems
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
    order_items_dto = list(map(lambda order_item: OrderItemOut(**order_items.__dict__), order_items))
    return OrderItemsOut(order_items=order_items_dto)


@router.post("/create_order_item", response_model=OrderItemOut)
async def create_order_item(order_item: OrderItemIn):
    session = get_session()
    orm_order_item = OrderItems(**order_item.dict())
    session.add(orm_order_item)
    session.commit()
    order_item_dto = OrderItemOut(**orm_order_item.__dict__)
    return order_item_dto


