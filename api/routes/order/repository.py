from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from routes.order.model import DeliveryMethod, Order, OrderStatus
from share.database import Repository, get_db_context


class OrderStatusRepository(Repository[OrderStatus]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)

    def find_by_name(self, status_name: str) -> OrderStatus | None:
        return (
            self.db_session.query(self.entity)
            .filter(OrderStatus.normalized_name == status_name.upper())
            .first()
        )


class DeliveryMethodRepository(Repository[DeliveryMethod]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)


class OrderRepository(Repository[Order]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)
