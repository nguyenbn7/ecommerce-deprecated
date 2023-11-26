from datetime import timedelta, datetime

from passlib.context import CryptContext

from jose import jwt
from jose.constants import ALGORITHMS
from api.account.model import ApplicationUser

from share.setting import get_token_service_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# TODO: change this later
# 30 days
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 60 * 24

settings = get_token_service_settings()


def create_access_token(claims: dict, expires_delta: timedelta | None = None):
    to_encode = claims.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHMS.HS256)
    return encoded_jwt


def generate_jwt_token(user: ApplicationUser):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        claims={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return access_token


def verfiy_password(secret: str | bytes, hash: str | bytes | None):
    return pwd_context.verify(secret, hash)


def hash_password(password: str):
    return pwd_context.hash(password)
