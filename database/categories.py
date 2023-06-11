from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship

from .base_meta import Base


class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}

    category_name = Column(Text, nullable=False)
    category_id = Column(Integer, primary_key=True)
    product = relationship('Product')
    def __str__(self):
        return f"Категория {self.category_id}: {self.category_name}"