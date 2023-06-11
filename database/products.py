from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_meta import Base


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}

    product_name = Column(Text, nullable=False)
    product_id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.manufacturer_id'))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    seller_id = Column(Integer, ForeignKey('sellers.seller_id'))
    category = relationship('Categories')
    delivery = relationship('Delivery')
    manufactures = relationship("ProductManufacture", back_populates="products")
    orders = relationship("OrderItems", back_populates="products")
    sellers = relationship("SellerProduct", backref="product")
    def __str__(self):
        return f"Товар {self.product_id}: {self.product_name}"
