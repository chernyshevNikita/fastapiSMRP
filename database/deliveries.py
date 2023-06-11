from datetime import datetime

from sqlalchemy import Column, Text, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base_meta import Base


class Delivery(Base):
    __tablename__ = 'deliveries'
    __table_args__ = {'extend_existing': True}

    delivery_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('stores.store_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    product_count = Column(Integer, nullable=False)
    delivery_date = Column(DateTime)
    products = relationship('Product')
    store = relationship('Store')

    def __str__(self):
        return f"Доставка {self.delivery_id}: {self.delivery_date}"