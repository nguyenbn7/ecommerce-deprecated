from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from redis import Redis
from route.accounts.model import User
from route.accounts.service import get_current_user
from route.baskets.service import delete_customer_basket, get_customer_basket

from route.orders.model import CustomerOrder, DeliveryMethod, PaymentType
from route.orders.service import create_customer_order
from share.dependency import get_db_session, get_redis_session


order_router = APIRouter(prefix="/orders", tags=["Order"])


@order_router.post("/")
def create_order(
    customer_order: CustomerOrder,
    current_user: Annotated[User, Depends(get_current_user)],
    redis_session: Annotated[Redis, Depends(get_redis_session)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    basket = get_customer_basket(redis_session, customer_order.basketId)

    if not basket:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Basket not found")

    if not len(basket.items):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Basket has no item")

    if customer_order.paymentType.upper() not in PaymentType:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid payment type")

    delivery_method = (
        db_session.query(DeliveryMethod)
        .filter(DeliveryMethod.id == customer_order.deliveryMethodId)
        .first()
    )
    if not delivery_method:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid delivery method")

    new_order = create_customer_order(
        db_session,
        current_user.email,
        customer_order.paymentType,
        delivery_method.id,
        customer_order.billingAddress,
        customer_order.shippingAddress,
        basket,
    )

    delete_customer_basket(redis_session, customer_order.basketId)

    return {"order_id": new_order.id}


@order_router.get("/payments")
def get_payment_methods(_: Annotated[User, Depends(get_current_user)]):
    return list(p.value for p in PaymentType)


@order_router.get("/delivery-methods")
def get_delivery_methods(
    _: Annotated[User, Depends(get_current_user)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    return db_session.query(DeliveryMethod).all()
