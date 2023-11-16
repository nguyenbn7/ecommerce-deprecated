from sqlalchemy import BigInteger, String
from sqlalchemy.orm import mapped_column, Mapped
from shares.base_orm_models import Base


class ProductType(Base):
    __tablename__ = "product_types"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
