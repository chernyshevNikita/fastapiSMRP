from typing import List

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import Client

ClientOut = sqlalchemy_to_pydantic(Client)


class ClientIn(sqlalchemy_to_pydantic(Client)):
    class Config:
        orm_mode = True


#ClientIn.__fields__.pop('client_id')
#print(ClientIn.__fields__)


class ClientsOut(BaseModel):
    clients: List[ClientOut]
