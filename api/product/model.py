from dataclasses import dataclass
from typing import List
from pydantic import BaseModel, Field
from sqlalchemy import BigInteger, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from product_brand.model import ProductBrand
from product_type.model import ProductType

from share.model import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=False)

    product_brand_id: Mapped[int] = mapped_column(ForeignKey("product_brands.id"))
    product_brand: Mapped[ProductBrand] = relationship(back_populates="products")

    product_type_id: Mapped[int] = mapped_column(ForeignKey("product_types.id"))
    product_type: Mapped["ProductType"] = relationship(back_populates="products")


@dataclass(frozen=True)
class ProductDTO:
    id: int
    name: str
    description: str
    price: float
    picture_url: str
    product_brand: str
    product_type: str


# def map_to_dtos(products: List[Product]) -> List[ProductDTO]:
#     return list(map(map_to_dto, products))


class ProductsParams(BaseModel):
    page_index: int | None = Field(default=1, ge=1)
    page_size: int | None = Field(default=6, ge=1, le=200)
    brand_id: int | None = Field(default=None, gt=0)
    type_id: int | None = Field(default=None, gt=0)
    sort: str | None = Field(default=None)
    search: str | None = Field(default=None)


class ProductProjection(Base):
    __table__ = Product.__table__.join(ProductBrand.__table__).join(
        ProductType.__table__
    )
    product_brand = column_property(ProductBrand.__table__.c.name)
    _product_brand_id = column_property(ProductBrand.__table__.c.id)
    product_type = column_property(ProductType.__table__.c.name)
    _product_type_id = column_property(ProductType.__table__.c.id)

    __mapper_args__ = {"exclude_properties": ["product_brand_id", "product_type_id"]}

    def to_dto(self) -> ProductDTO:
        return ProductDTO(
            self.id,
            self.name,
            self.description,
            self.price,
            f"http://localhost:8000/{self.picture_url}",  # TODO: read url from env
            self.product_brand,
            self.product_type,
        )
