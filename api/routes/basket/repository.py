from datetime import timedelta
import json
from typing import Annotated

from fastapi import Depends
from redis import Redis
from routes.basket.model import CustomerBasket

from core.redis import get_redis_context


class BasketRepository:
    def __init__(self, db: Annotated[Redis, Depends(get_redis_context)]):
        self.db = db

    def get_basket(self, basket_id: str) -> CustomerBasket | None:
        basket_string = self.db.get(basket_id)
        if basket_string:
            return CustomerBasket(**json.loads(basket_string))
        return None

    def update_basket(self, basket: CustomerBasket):
        created = self.db.setex(
            basket.id, timedelta(30), json.dumps(basket, default=lambda o: o.__dict__)
        )
        if not created:
            return None
        return self.get_basket(basket.id)

    def delete_basket(self, basket_id: str):
        return self.db.delete(basket_id)
