from typing import Union
from app.db import Base, engine
from fastapi import FastAPI
from app.routes import router

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World 0.4"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app.include_router(router)
