from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship

from .base_meta import Base


class Manufacture(Base):
    __tablename__ = 'manufacturers'
    __table_args__ = {'extend_existing': True}

    manufacturer_name = Column(Text, nullable=False)
    manufacturer_id = Column(Integer, primary_key=True)
    products = relationship("ProductManufacture", back_populates="manufactures")


    def __str__(self):
        return f"Завод {self.manufacturer_id}: {self.manufacturer_name}"