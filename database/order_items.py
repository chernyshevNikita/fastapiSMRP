from datetime import datetime

from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class OrderItems(Base):
    __tablename__ = 'order_items'
    __table_args__ = {'extend_existing': True}

    order_id = Column(ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(ForeignKey("products.product_id"), primary_key=True)
    product_count = Column(Integer, nullable=False)
    product_price = Column(Integer, nullable=False)
    orders = relationship("Order", back_populates="products")
    products = relationship("Product", back_populates="orders")
    def __str__(self):
        return f"Заказ {self.order_id}: {self.product_id}"
