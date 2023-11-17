from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import BigInteger, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, Session
from share import Base, ErrorResponse, Repository, get_db


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=False)

    product_brand_id: Mapped[int] = mapped_column(ForeignKey("product_brands.id"))
    product_type_id: Mapped[int] = mapped_column(ForeignKey("product_types.id"))


class ProductRepo(Repository):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db, Product)


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def get_products(repo: Annotated[ProductRepo, Depends(ProductRepo)]):
    return repo.get_all()


@product_router.get("/{id}")
def get_product(id: int, repo: Annotated[ProductRepo, Depends(ProductRepo)]):
    product = repo.get_by_id(id)
    if not product:
        # TODO: use exception handler
        return JSONResponse(
            status_code=404, content=ErrorResponse("Product not found").__dict__
        )
    return product
