from typing import List
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from share.model import BaseORM


class ProductType(BaseORM):
    __tablename__ = "product_types"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    products: Mapped[List["Product"]] = relationship(back_populates="product_type")
