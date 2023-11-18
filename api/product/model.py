from sqlalchemy import BigInteger, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from share import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=False)

    product_brand_id: Mapped[int] = mapped_column(ForeignKey("product_brands.id"), deferred=True)
    product_brand: Mapped["ProductBrand"] = relationship(back_populates="products")

    product_type_id: Mapped[int] = mapped_column(ForeignKey("product_types.id"), deferred=True)
    product_type: Mapped["ProductType"] = relationship(back_populates="products")
