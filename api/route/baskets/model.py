from dataclasses import dataclass, field
from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field


@dataclass
class BasketItem:
    id: int
    productName: str
    price: float
    quantity: int
    pictureUrl: str
    brand: str
    type: str


@dataclass
class Basket:
    id: str | None = str(uuid4())
    items: List[BasketItem] = field(default_factory=list)


class CustomerBasketItem(BaseModel):
    id: int
    productName: str
    price: float
    quantity: int
    pictureUrl: str
    brand: str
    type: str


class CustomerBasket(BaseModel):
    id: str = Field()
    items: List[CustomerBasketItem] = Field()
