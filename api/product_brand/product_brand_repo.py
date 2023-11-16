from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from cores.repository import BaseRepository
from product_brand.product_brand_models import ProductBrand
from shares.database import get_db


class ProductBrandRepo(BaseRepository):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db, ProductBrand)
