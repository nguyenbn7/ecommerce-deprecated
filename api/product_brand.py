from typing import Annotated, List
from fastapi import APIRouter, Depends
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session
from product import Product
from share import Base, Repository, get_db


class ProductBrand(Base):
    __tablename__ = "product_brands"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    products: Mapped[List[Product]] = relationship()


class ProductBrandRepository(Repository[ProductBrand]):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db)


product_brand_router = APIRouter(prefix="/products/brands", tags=["Product Brands"])


@product_brand_router.get("/")
def get_products_brands(
    repo: Annotated[ProductBrandRepository, Depends(ProductBrandRepository)]
):
    return repo.get_all()
