from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from routes.product_type.model import ProductType
from share.database import Repository, get_db_context


class ProductTypeRepository(Repository[ProductType]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)
