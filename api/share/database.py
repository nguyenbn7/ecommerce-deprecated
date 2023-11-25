from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, List, TypeVar, get_args
from sqlalchemy import func, select, desc
from sqlalchemy.orm import sessionmaker, Session
from core.database import engine
from share.model import Base, Pageable, Page, SortOption, SortDirection, Specification

_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_context():
    db = _Session()
    try:
        yield db
    finally:
        db.close()


TEntity = TypeVar("TEntity", bound=Base)
TClass = TypeVar("TClass", bound=Base)


# https://stackoverflow.com/questions/48572831/how-to-access-the-type-arguments-of-typing-generic
@dataclass(frozen=True)
class Repository(Generic[TEntity], ABC):
    @abstractmethod
    def __init__(self, db: Session):
        self.db: Session = db
        self.entity: TEntity = get_args(self.__orig_bases__[0])[0]

    def get_all(
        self,
        specification: Specification | None = None,
        sort: List[SortOption] | None = None,
        pageable: Pageable | None = None,
        projected_to: TClass | None = None,
    ) -> Page[TClass | TEntity] | List[TClass | TEntity]:
        new_query = (
            self.db.query(self.entity)
            if not projected_to
            else self.db.query(projected_to)
        )

        sort_options = None

        if sort:
            sort_options = list(
                map(
                    lambda s: desc(s.by) if s.direction == SortDirection.DESC else s.by,
                    sort,
                )
            )

        if specification:
            new_query = new_query.filter(specification())

        if not pageable:
            if sort_options and len(sort_options) > 0:
                new_query = new_query.order_by(*sort_options)
            return new_query.all()

        count_statement = (
            select(func.count()).select_from(self.entity).filter(specification())
        )

        total_items = self.db.execute(count_statement).scalar()

        page_number, page_size = pageable.page_index, pageable.page_size

        if page_size < 1:
            page_size = 6

        if page_number * page_size > total_items:
            page_number = 1
            page_size = 6

        data_statement = new_query

        if sort_options and len(sort_options) > 0:
            data_statement = data_statement.order_by(*sort_options)

        data_statement = data_statement.offset((page_number - 1) * page_size).limit(
            page_size
        )

        data = data_statement.all()

        return Page[TClass | TEntity](page_number, len(data), total_items, data)

    def get_by_id(
        self,
        id: Any,
        specification: Specification | None = None,
        projected_to: TClass | None = None,
    ) -> TEntity | TClass | None:
        new_query = (
            self.db.query(self.entity)
            if not projected_to
            else self.db.query(projected_to)
        )

        new_query = new_query.filter(self.entity.__mapper__.primary_key[0] == id)

        if specification:
            return new_query.filter(specification()).first()
        return new_query.first()
