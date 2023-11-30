from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from routes.account.model import ApplicationUser
from share.database import Repository, get_db_context


class UserRepository(Repository[ApplicationUser]):
    def __init__(self, db: Annotated[Session, Depends(get_db_context)]) -> None:
        super().__init__(db)

    def get_user_by_username(self, username: str) -> ApplicationUser | None:
        return (
            self.db.query(self.entity)
            .filter(self.entity.normalized_user_name == username.upper())
            .first()
        )

    def get_user_by_email(self, email: str) -> ApplicationUser | None:
        return (
            self.db.query(self.entity)
            .filter(self.entity.normalized_email == email.upper())
            .first()
        )

    def save(self, entity: ApplicationUser):
        entity.normalized_email = entity.email.strip().upper()
        entity.normalized_user_name = entity.user_name.strip().upper()
        self.db.add(entity)
        self.db.commit()
        return entity
