from datetime import timedelta
import json
from types import SimpleNamespace

from redis import Redis

from route.baskets.model import CustomerBasket


def get_customer_basket(redis_session: Redis, basket_id: str) -> CustomerBasket | None:
    basket_string = redis_session.get(basket_id)
    if basket_string:
        return json.loads(basket_string, object_hook=lambda b: SimpleNamespace(**b))
    return None


def update_customer_basket(redis_session: Redis, basket: CustomerBasket):
    created = redis_session.setex(
        basket.id, timedelta(30), json.dumps(basket, default=lambda o: o.__dict__)
    )
    if not created:
        return None
    return get_customer_basket(redis_session, basket.id)


def delete_customer_basket(redis_session: Redis, basket_id: str):
    return redis_session.delete(basket_id)
