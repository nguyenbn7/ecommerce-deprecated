from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from cores.repository import BaseRepository
from product_type.product_type_models import ProductType
from shares.database import get_db


class ProductTypeRepo(BaseRepository):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db, ProductType)
