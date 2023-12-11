from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from sqlalchemy.orm import Session

from passlib.context import CryptContext

from route.accounts.model import User
from share.dependency import get_db_session
from share.jwt_service import decode_jwt_token


_security = HTTPBearer()
_pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verfiy_password(secret: str | bytes, hash: str | bytes | None):
    return _pwd_context.verify(secret, hash)


def hash_password(password: str):
    return _pwd_context.hash(password)


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(_security)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_jwt_token(credentials.credentials)

        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    user = db_session.query(User).filter(User.normalized_user_name == username)

    if user is None:
        raise credentials_exception
    return user


def create_user(
    db_session: Session, username: str, email: str, display_name: str, password: str
):
    user = User()
    user.email = email.strip()
    user.display_name = display_name.strip()
    user.user_name = username
    user.password_hash = hash_password(password)
    user.normalized_email = user.email.upper()
    user.normalized_user_name = user.user_name.upper()

    db_session.add(user)
    db_session.commit()
    return user


def sign_in(db_session: Session, username: str, password: str):
    user = get_user_by_username(db_session, username)

    if not user:
        return None

    if not verfiy_password(password, user.password_hash):
        return None

    return user


def get_user_by_username(db_session: Session, username: str):
    return (
        db_session.query(User)
        .filter(User.normalized_user_name == username.upper())
        .first()
    )
