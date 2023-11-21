from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List, TypeVar, Generic
from sqlalchemy import ColumnElement, ColumnExpressionArgument
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


@dataclass
class APIException(Exception):
    status_code: int
    message: str | None = None
    headers: dict | None = None


TData = TypeVar("TData")


@dataclass
class Pagination(Generic[TData]):
    page_index: int
    page_size: int
    total_items: int
    data: List[TData]


class Specification(ABC):
    @abstractmethod
    def to_criterion(self) -> ColumnExpressionArgument[bool] | ColumnElement[bool]:
        """
        Use `and_`, `or_` and many more functions in `sqlalchemy.sql.expression` to
        construct criteria.
        """
        raise NotImplementedError()

    def __call__(self) -> ColumnExpressionArgument[bool] | ColumnElement[bool]:
        return self.to_criterion()


class SortDirection(Enum):
    ASC = 1
    DESC = 2


@dataclass(frozen=True)
class Sort:
    by: ColumnExpressionArgument | str
    direction: SortDirection | None = SortDirection.ASC


@dataclass(frozen=True)
class Pageable:
    page_index: int
    page_size: int
