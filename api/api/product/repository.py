from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from api.product.model import Product
from share.database import Repository, get_db_context


class ProductRepository(Repository[Product]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)
