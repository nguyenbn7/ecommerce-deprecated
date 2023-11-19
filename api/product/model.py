from typing import List
from pydantic import BaseModel, Field
from sqlalchemy import BigInteger, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from share.model import Base


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
        print(kwargs)
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


class ProductsParams(BaseModel):
    page_index: int | None = Field(default=1, ge=1)
    page_size: int | None = Field(default=6, ge=1, le=200)
    brand_id: int | None = Field(default=None, gt=0)
    type_id: int | None = Field(default=None, gt=0)
    sort: str | None = Field(default=None)
    search: str | None = Field(default=None)

