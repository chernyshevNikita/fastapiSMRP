from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import ClientIn, ClientOut
from database import get_session, Client
from models.client import ClientsOut

router = APIRouter(prefix="/client", tags=["client"])


@router.get("/get", response_model=ClientOut)
async def get_one(client_id: int,
                  session: Session = Depends(get_session)):
    client: Client = session.query(Client).get(client_id)
    if client:
        client_dto = ClientOut(**client.__dict__)
        return client_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Client with id {client_id} not found!")


@router.get("/get_all", response_model=ClientsOut)
async def get_all():
    session = get_session()
    clients = session.query(Client).all()
    clients_dto = list(map(lambda client: ClientOut(**client.__dict__), clients))
    return ClientsOut(clients=clients_dto)


@router.post("/create_client", response_model=ClientOut)
async def create_client(client: ClientIn):
    session = get_session()
    orm_client = Client(**client.dict())
    session.add(orm_client)
    print(orm_client.__dict__)
    session.commit()
    print(orm_client.__dict__)
    client_dto = ClientOut(**orm_client.__dict__)
    return client_dto


@router.delete("/delete_client/{client_id}", response_model=ClientOut)
async def delete_client(client_id: int, session: Session = Depends(get_session)):
    client: Client = session.query(Client).get(client_id)
    if client:
        client_dto = ClientOut(**client.__dict__)
        session.delete(client)
        session.commit()
        return client_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Client with id {client_id} not found!")


@router.post("/update_client", response_model=ClientOut)
async def update_client(client: ClientIn):
    session = get_session()

    orm_client = session.query(Client).get(client.client_id)
    #session.add(orm_client)
    orm_client.client_name = client.client_name
    orm_client.client_city = client.client_city

    print(orm_client.__dict__)
    session.commit()
    print(orm_client.__dict__)
    client_dto = ClientOut.from_orm(orm_client)
    return client_dto
