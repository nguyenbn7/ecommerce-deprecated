from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response
from redis import Redis

from route.baskets.model import Basket, BasketItem, CustomerBasket
from route.baskets.service import (
    delete_customer_basket,
    get_customer_basket,
    update_customer_basket,
)
from share.dependency import get_redis_session

basket_router = APIRouter(prefix="/basket", tags=["Basket"])


@basket_router.get("/")
def get_basket(id: str, redis_session: Annotated[Redis, Depends(get_redis_session)]):
    basket = get_customer_basket(redis_session, id)
    if not basket:
        return Basket(id, [])
    return basket


@basket_router.post("/")
def update_basket(
    customer_basket: CustomerBasket,
    redis_session: Annotated[Redis, Depends(get_redis_session)],
):
    basket = Basket(
        customer_basket.id,
        list(map(lambda b: BasketItem(*vars(b).values()), customer_basket.items)),
    )
    return update_customer_basket(redis_session, basket)


@basket_router.delete("/")
def delete_basket(id: str, redis_session: Annotated[Redis, Depends(get_redis_session)]):
    deleted = delete_customer_basket(redis_session, id)
    if not deleted:
        raise HTTPException(404)
    return Response(status_code=200)
