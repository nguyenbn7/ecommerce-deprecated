from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from product_brand.model import ProductBrand
from share import Repository, get_db


class ProductBrandRepository(Repository[ProductBrand]):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db)
