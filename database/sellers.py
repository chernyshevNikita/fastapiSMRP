from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class Seller(Base):
    __tablename__ = 'sellers'
    __table_args__ = {'extend_existing': True}

    seller_id = Column(Integer, primary_key=True)
    seller_name = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    store_id = Column(Integer, ForeignKey('stores.store_id'))
    products = relationship('SellerProduct', backref="seller")
    store = relationship('Store')


    def __str__(self):
        return f"Продавец {self.seller_id}: {self.seller_name}"