from sqlalchemy.orm import Session
from route.baskets.model import Basket, BasketItem
from route.orders.model import (
    BillingAddress,
    CustomerAddress,
    DeliveryMethod,
    Order,
    OrderItem,
    OrderStatus,
    PaymentType,
    ShippingAddress,
)


def map_basket_item_to_order_item(basket_item: BasketItem):
    order_item = OrderItem()
    order_item.product_name = basket_item.productName
    order_item.price = basket_item.price
    order_item.quantity = basket_item.quantity
    order_item.picture_url = basket_item.pictureUrl
    order_item.brand = basket_item.brand
    order_item.type = basket_item.type
    return order_item


def to_billing_address(customer_address: CustomerAddress):
    b = BillingAddress()
    b.full_name = customer_address.fullName
    b.email = customer_address.email
    b.phone_number = customer_address.phoneNumber
    b.address = customer_address.address
    b.country = customer_address.country
    b.state = customer_address.state
    b.zip_code = customer_address.zipCode
    return b


def to_shipping_address(customer_address: CustomerAddress):
    b = ShippingAddress()
    b.full_name = customer_address.fullName
    b.email = customer_address.email
    b.phone_number = customer_address.phoneNumber
    b.address = customer_address.address
    b.country = customer_address.country
    b.state = customer_address.state
    b.zip_code = customer_address.zipCode
    return b


def get_order_status(db_session: Session, name: str):
    return (
        db_session.query(OrderStatus)
        .filter(OrderStatus.normalized_name == name.upper())
        .first()
    )


def create_customer_order(
    db_session: Session,
    buyer_email: str,
    payment_type: str,
    delivery_method: DeliveryMethod,
    basket: Basket,
    billing_address: CustomerAddress,
    shipping_address: CustomerAddress | None,
):
    order_status = get_order_status(db_session, "pending")
    if order_status is None:
        raise Exception("order status named 'pending' not found")

    order = Order()
    order.buyer_email = buyer_email
    order.payment_type = PaymentType(payment_type.upper())
    order.items = list(map(map_basket_item_to_order_item, basket.items))
    order.delivery_method_id = delivery_method.id
    order.status_id = order_status.id
    order.delivery_price = delivery_method.price
    order.billing_address = to_billing_address(billing_address)
    order.shipping_address = (
        to_shipping_address(shipping_address)
        if shipping_address
        else to_shipping_address(billing_address)
    )
    order.subtotal = sum(item.price * item.quantity for item in order.items)

    db_session.add(order)
    db_session.commit()
    return order
