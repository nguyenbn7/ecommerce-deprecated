from dataclasses import dataclass
from pydantic import BaseModel, Field, ValidationInfo, field_validator
from sqlalchemy import BigInteger, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from api.product_brand.model import ProductBrand
from api.product_type.model import ProductType

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


class ProductsParams(BaseModel):
    page_number: int | None = Field(default=1)
    page_size: int | None = Field(default=6)
    brand_id: int | None = Field(default=None)
    type_id: int | None = Field(default=None)
    sort: str | None = Field(default=None)
    search: str | None = Field(default=None)

    @field_validator("brand_id", "type_id", "page_number", "page_size")
    @classmethod
    def set_ids(cls, v: int | None, info: ValidationInfo):
        if v is None:
            return None
        if v < 1:
            raise ValueError(f"{info.field_name} can not be less than 1")
        return v


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
