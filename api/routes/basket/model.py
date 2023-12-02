from dataclasses import dataclass, field
import json
from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field


@dataclass
class BasketItem:
    id: int
    product_name: str
    price: float
    quantity: int
    picture_url: str
    brand: str
    type: str


@dataclass
class CustomerBasket:
    id: str | None = str(uuid4())
    items: List[BasketItem] = field(default_factory=list)


class BasketItemDTO(BaseModel):
    id: int
    product_name: str
    price: float
    quantity: int
    picture_url: str
    brand: str
    type: str


class CustomerBasketDTO(BaseModel):
    id: str = Field()
    items: List[BasketItemDTO] = Field()
