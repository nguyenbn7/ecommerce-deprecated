from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from product_type.model import ProductType
from share import Repository, get_db


class ProductTypeRepository(Repository[ProductType]):
    def __init__(self, db: Annotated[Session, Depends(get_db)]) -> None:
        super().__init__(db)
