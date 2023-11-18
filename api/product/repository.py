from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from product.model import Product
from share import Repository, get_db


class ProductRepository(Repository[Product]):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db)
