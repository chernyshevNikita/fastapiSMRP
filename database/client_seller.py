from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class ClientSeller(Base):
    __tablename__ = 'clients_sellers'
    __table_args__ = {'extend_existing': True}

    client_id = Column(ForeignKey("Client.client_id"), primary_key=True)
    seller_id = Column(ForeignKey("Seller.seller_id"), primary_key=True)

    clients = relationship("Client", back_populates="sellers")
    sellers = relationship("Seller", back_populates="clients")

    def __str__(self):
        return f"Покупатель - продавец {self.client_id}: {self.seller_id}"