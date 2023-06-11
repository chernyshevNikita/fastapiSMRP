from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class SellerProduct(Base):
    __tablename__ = 'sellers_products'
    __table_args__ = {'extend_existing': True}

    product_id = Column(ForeignKey("products.product_id"), primary_key=True)
    seller_id = Column(ForeignKey("sellers.seller_id"), primary_key=True)

    products = relationship("Product", back_populates="sellers")
    sellers = relationship("Seller", back_populates="products")

    def __str__(self):
        return f"Продавец - товар {self.seller_id}: {self.product_id}"