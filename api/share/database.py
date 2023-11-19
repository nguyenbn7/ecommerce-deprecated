from abc import abstractmethod
from typing import Generic, List, TypeVar, get_args
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Query, Session
from core.database import engine

_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_context():
    db = _Session()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass


TEntity = TypeVar("TEntity", bound=Base)


class Specification:
    @abstractmethod
    def apply_spec(self, query: Query[TEntity]) -> Query[TEntity]:
        raise NotImplementedError("Specification is an Abstract class")


# https://stackoverflow.com/questions/48572831/how-to-access-the-type-arguments-of-typing-generic
class Repository(Generic[TEntity]):
    @abstractmethod
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.entity: TEntity = get_args(self.__orig_bases__[0])[0]
        self.base_query: Query[TEntity] = self.db.query(self.entity)

    def get_all(self, specification: Specification = None) -> List[TEntity]:
        query = self.base_query
        if specification:
            query = specification.apply_spec(query)
        return query.all()

    def get_by_id(self, id: int, specification: Specification = None) -> TEntity | None:
        query = self.base_query
        if specification:
            query = specification.apply_spec(query)
        return query.filter(self.entity.id == id).first()
