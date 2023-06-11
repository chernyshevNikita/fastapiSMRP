from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class ProductManufacture(Base):
    __tablename__ = 'products_manufacturers'
    __table_args__ = {'extend_existing': True}

    product_id = Column(ForeignKey("products.product_id"), primary_key=True)
    manufacturer_id = Column(ForeignKey("manufacturers.manufacturer_id"), primary_key=True)

    products = relationship("Product", back_populates="manufactures")
    manufactures = relationship("Manufacture", back_populates="products")

    def __str__(self):
        return f"Завод - товар: {self.manufacture_id}: {self.product_id}"