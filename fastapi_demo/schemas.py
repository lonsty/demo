# @FILENAME : schemas
# @AUTHOR : lonsty
# @DATE : 10/23/20 11:16 PM
from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
