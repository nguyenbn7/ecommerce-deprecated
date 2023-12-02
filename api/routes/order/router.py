from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from routes.account.model import ApplicationUser
from routes.account.service import get_current_user
from routes.basket.model import BasketItem
from routes.basket.repository import BasketRepository

from routes.order.model import Order, OrderDTO, OrderItem, PaymentType
from routes.order.repository import (
    DeliveryMethodRepository,
    OrderRepository,
    OrderStatusRepository,
)


order_router = APIRouter(prefix="/orders", tags=["Order"])


def map_basket_item_to_order_item(basket_item: BasketItem):
    order_item = OrderItem()
    order_item.product_name = basket_item.product_name
    order_item.price = basket_item.price
    order_item.quantity = basket_item.quantity
    order_item.picture_url = basket_item.picture_url
    order_item.brand = basket_item.brand
    order_item.type = basket_item.type
    return order_item


@order_router.post("/")
def create_order(
    order_dto: OrderDTO,
    current_user: Annotated[ApplicationUser, Depends(get_current_user)],
    basket_repo: Annotated[BasketRepository, Depends(BasketRepository)],
    order_status_repo: Annotated[OrderStatusRepository, Depends(OrderStatusRepository)],
    delivery_method_repo: Annotated[
        DeliveryMethodRepository, Depends(DeliveryMethodRepository)
    ],
    order_repo: Annotated[OrderRepository, Depends(OrderRepository)],
):
    basket = basket_repo.get_basket(order_dto.basket_id)

    if not basket:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Basket not found")

    if not len(basket.items):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Basket has no item")

    if order_dto.payment_type not in PaymentType:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid payment type")

    delivery_method = delivery_method_repo.get_by_id(order_dto.delivery_method_id)
    if not delivery_method:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid delivery method")

    billing_address = order_dto.billing_address.convert_to_billing_address()
    if not order_dto.shipping_address:
        shipping_address = order_dto.billing_address.convert_to_shipping_address()
    else:
        shipping_address = order_dto.shipping_address.convert_to_shipping_address()

    order = Order()
    order.buyer_email = current_user.email
    order.payment_type = order_dto.payment_type
    order.items = list(map(map_basket_item_to_order_item, basket.items))
    order.delivery_method_id = delivery_method.id
    order.status_id = order_status_repo.find_by_name("pending").id
    order.delivery_price = delivery_method.price
    order.billing_address = billing_address
    order.shipping_address = shipping_address
    order.subtotal = sum(item.price * item.quantity for item in order.items)

    order_repo.save(order)

    basket_repo.delete_basket(order_dto.basket_id)

    return {"order_id": order.id}


@order_router.get("/payments")
def get_payment_methods(
    current_user: Annotated[ApplicationUser, Depends(get_current_user)]
):
    return list(p.value for p in PaymentType)
