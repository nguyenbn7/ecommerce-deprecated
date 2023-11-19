from typing import List
from sqlalchemy import BigInteger, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from share.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=False)

    product_brand_id: Mapped[int] = mapped_column(
        ForeignKey("product_brands.id"), deferred=True
    )
    product_brand: Mapped["ProductBrand"] = relationship(back_populates="products")

    product_type_id: Mapped[int] = mapped_column(
        ForeignKey("product_types.id"), deferred=True
    )
    product_type: Mapped["ProductType"] = relationship(back_populates="products")


class ProductDTO:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id", -1)
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.price = kwargs.get("price", -1.1)
        self.picture_url = f"http://localhost:8000/{kwargs.get('picture_url', '')}"
        self.product_type = kwargs["product_type"].name
        self.product_brand = kwargs["product_brand"].name


def map_to_dtos(products: List[Product]) -> List[ProductDTO]:
    return list(map(map_to_dto, products))


def map_to_dto(product: Product) -> ProductDTO:
    return ProductDTO(**vars(product))
