from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import ClientIn, ClientOut
from database import get_session, Client
from models.client import ClientsOut

router = APIRouter(prefix="/client", tags=["client"])


@router.get("/{client_id}", response_model=ClientOut)
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
    clients: Client = session.query(Client).all()
    clients_dto = list(map(lambda client: ClientOut(**client.__dict__), clients))
    return ClientsOut(clients=clients_dto)


@router.post("/", response_model=ClientOut)
async def create_client(client: ClientIn):
    session = get_session()
    orm_client = Client(**client.dict())
    session.add(orm_client)
    print(orm_client.__dict__)
    session.commit()
    print(orm_client.__dict__)
    client_dto = ClientOut(**orm_client.__dict__)
    return client_dto