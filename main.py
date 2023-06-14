from enum import Enum
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from endpoints import client_router, seller_router,seller_product_router,order_item_router
from database import get_session


app = FastAPI()
app.include_router(client_router)
app.include_router(seller_router)
app.include_router(seller_product_router)
app.include_router(order_item_router)
if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=5000,
                log_level="info",
                reload=True)