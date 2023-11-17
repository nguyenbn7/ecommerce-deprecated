from typing import Annotated

from fastapi import APIRouter, Depends
from share import Base, Repository, get_db

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import mapped_column, Mapped, Session


class ProductType(Base):
    __tablename__ = "product_types"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)


class ProductTypeRepo(Repository):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db, ProductType)


product_type_router = APIRouter(prefix="/products/types", tags=["Product Types"])


@product_type_router.get("/")
def get_products_types(repo: Annotated[ProductTypeRepo, Depends(ProductTypeRepo)]):
    return repo.get_all()
