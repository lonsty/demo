# @FILENAME : app
# @AUTHOR : lonsty
# @DATE : 10/23/20 11:17 PM
from typing import Optional

from fastapi import FastAPI

from .schemas import Item

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: Item):
    # Insert item to db
    return {"msg": f"Item {item.name} has been created"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    # Query item from db, raise 404 if there is no record
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # Check if item_id exists in db, otherwise raise 404
    # Update item in db
    return {"item_name": item.name, "item_id": item_id}


@app.put("/items/{item_id}")
def delete_item(item_id: int):
    # Delete item from db
    return {"msg": f"Item {item_id} has been deleted"}
