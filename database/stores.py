from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship

from .base_meta import Base


class Store(Base):
    __tablename__ = 'stores'
    __table_args__ = {'extend_existing': True}

    store_name = Column(Text, nullable=False)
    store_id = Column(Integer, primary_key=True)
    orders = relationship("Order")
    sellers = relationship('Seller')

    def __str__(self):
        return f"Магазин {self.store_id}: {self.store_name}"