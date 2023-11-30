from datetime import datetime
import enum
from functools import reduce
from typing import List
from sqlalchemy import BigInteger, Integer, String, DateTime, Numeric, Enum, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from pydantic import BaseModel

from share.model import BaseORM


class OrderItemDTO(BaseModel):
    product_id: int
    product_name: str
    picture_url: str
    price: float
    quantity: int


class BillingAddressDTO(BaseModel):
    full_name: str
    email: str
    phone_number: str
    address: str
    address2: str
    country: str
    state: str
    zip_code: str


class ShippingAddressDTO(BaseModel):
    full_name: str
    email: str
    phone_number: str
    address: str
    address2: str
    country: str
    state: str
    zip_code: str


class DeliveryMethodDTO(BaseModel):
    id: int
    short_name: str
    delivery_time: str
    price: float


class PaymentMethodDTO(BaseModel):
    id: int
    name: str


class OrderDTO(BaseModel):
    items: List[OrderItemDTO]
    billing_address: BillingAddressDTO
    shipping_address: ShippingAddressDTO | None
    delivery_method: DeliveryMethodDTO
    payment_method: PaymentMethodDTO


class OrderItem(BaseORM):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    product_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    product_name: Mapped[str] = mapped_column(String, nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    product_name: Mapped[str] = mapped_column(String, nullable=False)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order"] = relationship(back_populates="items")


class PaymentMethod(BaseORM):
    __tablename__ = "payment_methods"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    orders: Mapped[List["Order"]] = relationship()


class BillingAddress(BaseORM):
    __tablename__ = "billing_addresses"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    address2: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)
    zip_code: Mapped[str] = mapped_column(String, nullable=False)

    orders: Mapped[List["Order"]] = relationship()


class ShippingAddress(BaseORM):
    __tablename__ = "shipping_addresses"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    address2: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)
    zip_code: Mapped[str] = mapped_column(String, nullable=False)

    orders: Mapped[List["Order"]] = relationship()


class DeliveryMethod(BaseORM):
    __tablename__ = "delivery_methods"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    short_name: Mapped[str] = mapped_column(String, nullable=False)
    delivery_time: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)

    orders: Mapped[List["Order"]] = relationship(back_populates="delivery_method")


class OrderStatus(enum.Enum):
    PENDING = "PENDING"
    PAYMENT_RECEIVED = "PAYMENT_RECEIVED"
    PAYMENT_FAILED = "PAYMENT_FAILED"


class Order(BaseORM):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow(), nullable=False
    )
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False
    )

    delivery_method_id: Mapped[int] = mapped_column(ForeignKey("delivery_methods.id"))
    delivery_method: Mapped["DeliveryMethod"] = relationship(back_populates="orders")
    billing_address_id: Mapped[int] = mapped_column(ForeignKey("billing_addresses.id"))
    shipping_address_id: Mapped[int] = mapped_column(
        ForeignKey("shipping_addresses.id")
    )
    payment_method_id: Mapped[int] = mapped_column(ForeignKey("payment_methods.id"))

    items: Mapped[List[OrderItem]] = relationship(back_populates="order")

    def get_total(self):
        return (
            sum(item.price * item.quantity for item in self.items)
            + self.delivery_method.price
        )
