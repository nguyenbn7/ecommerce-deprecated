from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from routes.basket.model import BasketItem
from routes.basket.repository import BasketRepository

from routes.order.model import Order, OrderDTO, OrderItem
from routes.order.repository import DeliveryMethodRepository, PaymentRepository


order_router = APIRouter(prefix="/orders", tags=["Order"])


def mapper(basket_item: BasketItem):
    order_item = OrderItem()
    order_item.product_name = basket_item.product_name
    order_item.price = basket_item.price
    order_item.quantity = basket_item.quantity
    order_item.picture_url = basket_item.picture_url
    order_item.brand = basket_item.brand
    order_item.type = basket_item.type
    return order_item


@order_router.post("")
def create_order(
    order_dto: OrderDTO,
    basket_repo: Annotated[BasketRepository, Depends(BasketRepository)],
    payment_repo: Annotated[PaymentRepository, Depends(PaymentRepository)],
    delivery_method_repo: Annotated[
        DeliveryMethodRepository, Depends(DeliveryMethodRepository)
    ],
):
    basket = basket_repo.get_basket(order_dto.basket_id)

    if not basket:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Basket not found")
    
    if not len(basket.items):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Basket has no item")
    
    payment_method = payment_repo.get_by_id(order_dto.payment_method_id)
    if not payment_method:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid payment method")

    delivery_method = delivery_method_repo.get_by_id(order_dto.delivery_method_id)
    if not delivery_method:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid delivery method")

    billing_address = order_dto.billing_address.convert_to_billing_address()
    if not order_dto.shipping_address:
        shipping_address = order_dto.billing_address.convert_to_shipping_address()
    else:
        shipping_address = order_dto.shipping_address.convert_to_shipping_address()

    order = Order()
    order.payment_method = payment_method.name
    order.items = map(mapper, basket.items)
    order.delivery_method_id = delivery_method.id
    order.billing_address = billing_address
    order.shipping_address = shipping_address
    return order
