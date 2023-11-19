from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from product_brand.model import ProductBrand
from share.database import Repository, get_db_context


class ProductBrandRepository(Repository[ProductBrand]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)
