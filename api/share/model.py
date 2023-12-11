from dataclasses import dataclass
from typing import List, TypeVar, Generic
from sqlalchemy.orm import DeclarativeBase


class BaseORM(DeclarativeBase):
    pass


TData = TypeVar("TData")


@dataclass
class Page(Generic[TData]):
    pageNumber: int
    pageSize: int
    totalItems: int
    data: List[TData]
