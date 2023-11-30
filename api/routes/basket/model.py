from dataclasses import dataclass
import json
from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field


class BasketItem:
    def __init__(
        self,
        id: int,
        product_name: str,
        price: float,
        quantity: int,
        picture_url: str,
        brand: str,
        type: str,
    ) -> None:
        self.id = id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.picture_url = picture_url
        self.brand = brand
        self.type = type

    def __repr__(self) -> str:
        return json.dumps(self.__dict__)

    def default(self):
        return self.__dict__


class CustomerBasket:
    def __init__(self, id: str, items: List[dict]):
        self.id = id
        if not id:
            self.id = str(uuid4())
        self.items = []
        if len(items):
            for item in items:
                bi = BasketItem(**item)
                self.items.append(bi)

    def __repr__(self) -> str:
        return json.dumps(self.__dict__)

    def default(self):
        return self.__dict__


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
