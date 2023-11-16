from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from cores.repository import BaseRepository
from product.product_models import Product
from shares.database import get_db


class ProductRepo(BaseRepository):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db, Product)
