from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar, get_args
from sqlalchemy import func, select
from sqlalchemy.orm import sessionmaker, Session
from core.database import engine
from share.model import Base, Pageable, Pagination, Specification

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
    def __init__(self, db: Session):
        self.db: Session = db
        self.entity: TEntity = get_args(self.__orig_bases__[0])[0]

    def get_all(
        self,
        specification: Specification | None = None,
        pageable: Pageable | None = None,
        projected_to: TClass | None = None,
    ):
        new_query = (
            self.db.query(self.entity)
            if not projected_to
            else self.db.query(projected_to)
        )

        if specification:
            new_query = new_query.filter(specification())

        if pageable:
            total_items = self.db.execute(
                select(func.count())
                .select_from(self.entity)
                .filter(specification())
                .order_by(None)
            ).scalar()

            page_index, page_size = pageable.page_index, pageable.page_size

            if page_index * page_size > total_items:
                page_index = 1
                page_size = 6

            data = new_query.offset((page_index - 1) * page_size).limit(page_size).all()

            return Pagination[TClass](page_index, len(data), total_items, data)

        return new_query.all()

    def get_by_id(
        self,
        id: Any,
        specification: Specification | None = None,
        projected_to: TClass | None = None,
    ):
        new_query = (
            self.db.query(self.entity)
            if not projected_to
            else self.db.query(projected_to)
        )

        new_query = new_query.filter(self.entity.__mapper__.primary_key[0] == id)

        if specification:
            return new_query.filter(specification()).first()
        return new_query.first()
