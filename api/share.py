from abc import abstractmethod
from typing import TypeVar
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


# TODO: read database url from env
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/ecommerce100"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
)

_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = _Session()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass


T = TypeVar("T", bound=Base)


class Repository:
    @abstractmethod
    def __init__(self, db: Session, entity: T) -> None:
        self.db = db
        self.entity = entity

    def get_all(self):
        return self.db.query(self.entity).all()

    def get_by_id(self, id: int):
        return self.db.query(self.entity).filter(self.id == id).first()


class ErrorResponse:
    def __init__(self, message: str) -> None:
        self.message = message
