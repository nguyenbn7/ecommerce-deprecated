from sqlalchemy import ForeignKey, Numeric, String, BigInteger
from sqlalchemy.orm import mapped_column, Mapped

from shares.base_orm_models import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=False)

    product_brand_id: Mapped[int] = mapped_column(ForeignKey("product_brands.id"))
    product_type_id: Mapped[int] = mapped_column(ForeignKey("product_types.id"))
