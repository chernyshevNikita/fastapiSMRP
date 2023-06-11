from datetime import datetime

from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}

    order_id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, default=datetime.now)
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    store_id = Column(Integer, ForeignKey('stores.store_id'))
    client = relationship("Client")
    store = relationship("Store")
    products = relationship("OrderItems", back_populates="orders")
    def __str__(self):
        return f"Заказ {self.order_id}: {self.order_date}"