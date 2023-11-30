from datetime import datetime
import enum
from typing import List
from sqlalchemy import BigInteger, Integer, String, DateTime, Numeric, Enum, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from pydantic import BaseModel, Field

from share.model import BaseORM


class BillingAddressDTO(BaseModel):
    full_name: str
    email: str
    phone_number: str
    address: str
    address2: str
    country: str
    state: str
    zip_code: str

    def convert_to_billing_address(self):
        b = BillingAddress()
        b.full_name = self.full_name
        b.email = self.email
        b.phone_number = self.phone_number
        b.address = self.address
        b.country = self.country
        b.state = self.state
        b.zip_code = self.zip_code
        return b

    def convert_to_shipping_address(self):
        b = ShippingAddress()
        b.full_name = self.full_name
        b.email = self.email
        b.phone_number = self.phone_number
        b.address = self.address
        b.country = self.country
        b.state = self.state
        b.zip_code = self.zip_code
        return b


class ShippingAddressDTO(BaseModel):
    full_name: str
    email: str
    phone_number: str
    address: str
    address2: str
    country: str
    state: str
    zip_code: str

    def convert_to_shipping_address(self):
        b = ShippingAddress()
        b.full_name = self.full_name
        b.email = self.email
        b.phone_number = self.phone_number
        b.address = self.address
        b.country = self.country
        b.state = self.state
        b.zip_code = self.zip_code
        return b


class DeliveryMethodDTO(BaseModel):
    id: int
    short_name: str
    delivery_time: str
    price: float


class OrderDTO(BaseModel):
    basket_id: str
    billing_address: BillingAddressDTO
    shipping_address: ShippingAddressDTO | None = Field(default=None)
    delivery_method_id: int
    payment_method_id: int


class OrderItem(BaseORM):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    product_name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=False)
    brand: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order"] = relationship(back_populates="items")


class PaymentMethod(BaseORM):
    __tablename__ = "payment_methods"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    code: Mapped[str] = mapped_column(String, nullable=False)


class BillingAddress(BaseORM):
    __tablename__ = "billing_addresses"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    address2: Mapped[str | None] = mapped_column(String, nullable=True)
    country: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)
    zip_code: Mapped[str] = mapped_column(String, nullable=False)


class ShippingAddress(BaseORM):
    __tablename__ = "shipping_addresses"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    address2: Mapped[str | None] = mapped_column(String, nullable=True)
    country: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)
    zip_code: Mapped[str] = mapped_column(String, nullable=False)


class DeliveryMethod(BaseORM):
    __tablename__ = "delivery_methods"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    short_name: Mapped[str] = mapped_column(String, nullable=False)
    delivery_time: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)


class OrderStatus(enum.Enum):
    PENDING = "PENDING"
    PAYMENT_RECEIVED = "PAYMENT_RECEIVED"
    PAYMENT_FAILED = "PAYMENT_FAILED"


class Order(BaseORM):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False
    )
    payment_method: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow(), nullable=False
    )

    items: Mapped[List[OrderItem]] = relationship(back_populates="order")
    delivery_method_id: Mapped[int] = mapped_column(ForeignKey("delivery_methods.id"))
    delivery_method: Mapped[DeliveryMethod] = relationship()
    billing_address_id: Mapped[int] = mapped_column(ForeignKey("billing_addresses.id"))
    billing_address: Mapped[BillingAddress] = relationship()
    shipping_address_id: Mapped[int] = mapped_column(
        ForeignKey("shipping_addresses.id")
    )
    shipping_address: Mapped[ShippingAddress] = relationship()

    def get_total(self):
        return (
            sum(item.price * item.quantity for item in self.items)
            + self.delivery_method.price
        )
