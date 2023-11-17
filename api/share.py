from abc import abstractmethod
from typing import Generic, TypeVar, get_args
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


# https://stackoverflow.com/questions/48572831/how-to-access-the-type-arguments-of-typing-generic
class Repository(Generic[T]):
    @abstractmethod
    def __init__(self, db: Session) -> None:
        self.db = db
        self.entity = get_args(self.__orig_bases__[0])[0]

    def get_all(self):
        return self.db.query(self.entity).all()

    def get_by_id(self, id: int):
        return self.db.query(self.entity).filter(self.entity.id == id).first()


class ErrorResponse:
    def __init__(self, message: str) -> None:
        self.message = message
