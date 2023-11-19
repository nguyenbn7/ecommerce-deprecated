from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, TypeVar, Generic
from sqlalchemy import ColumnElement, ColumnExpressionArgument
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class APIException(Exception):
    def __init__(
        self, status_code: int, message: str, headers: dict | None = None
    ) -> None:
        self.status_code = status_code
        self.message = message
        self.headers = headers


TPage = TypeVar("TPage")


class Pagination(Generic[TPage]):
    def __init__(
        self, page_index: int, page_size: int, total_items: int, data: List[TPage]
    ) -> None:
        self.page_index = page_index
        self.page_size = page_size
        self.total_items = total_items
        self.data = data


class Specification(ABC):
    @abstractmethod
    def to_criterion(self) -> ColumnExpressionArgument[bool] | ColumnElement[bool]:
        """
        Use `and_`, `or_` and many more functions in `sqlalchemy.sql.expression`
        """
        raise NotImplementedError()

    def __call__(self) -> ColumnExpressionArgument[bool] | ColumnElement[bool]:
        return self.to_criterion()


@dataclass(frozen=True)
class Pageable:
    page_index: int
    page_size: int
