from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from share.database import Base


class ProductBrand(Base):
    __tablename__ = "product_brands"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    products: Mapped[List["Product"]] = relationship(back_populates="product_brand")
