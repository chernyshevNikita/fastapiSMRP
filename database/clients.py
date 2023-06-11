from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship

from .base_meta import Base


class Client(Base):
    __tablename__ = 'clients'
    __table_args__ = {'extend_existing': True}

    client_name = Column(Text, nullable=False)
    client_id = Column(Integer, primary_key=True)
    client_city = Column(Text, nullable=False)
    orders = relationship("Order")

    def __str__(self):
        return f"Клиент {self.client_id}: {self.client_name} {self.client_city}"