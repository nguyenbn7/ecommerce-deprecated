from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from routes.order.model import DeliveryMethod, Order, PaymentMethod
from share.database import Repository, get_db_context


class PaymentRepository(Repository[PaymentMethod]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)

class DeliveryMethodRepository(Repository[DeliveryMethod]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)

class OrderRepository(Repository[Order]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)
