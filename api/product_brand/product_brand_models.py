from typing import List
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from product.product_models import Product
from shares.base_orm_models import Base


class ProductBrand(Base):
    __tablename__ = "product_brands"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    products: Mapped[List[Product]] = relationship()
