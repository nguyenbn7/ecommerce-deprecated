from datetime import timedelta, datetime
from fastapi import APIRouter, status
from jose import jwt
from jose.constants import ALGORITHMS

from passlib.context import CryptContext

from api.account.model import AppUser, LoginDTO, RegisterDTO, SuccessResponse
from share.model import APIException


account_router = APIRouter(prefix="/account", tags=["Account"])

# TODO: read secret key from env
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user = AppUser()


def create_access_token(claims: dict, expires_delta: timedelta | None = None):
    to_encode = claims.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHMS.HS256)
    return encoded_jwt


def generate_jwt_token(user: AppUser):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        claims={"sub": user.display_name}, expires_delta=access_token_expires
    )
    return access_token


@account_router.post("/login")
def login(loginDTO: LoginDTO):
    if loginDTO.email != user.email:
        raise APIException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Email or Password incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not pwd_context.verify(loginDTO.password, user.password_hash):
        raise APIException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Email or Password incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return SuccessResponse(generate_jwt_token(user), user.display_name, user.email)


@account_router.post("/register")
def register(registerDTO: RegisterDTO):
    if registerDTO.email == user.email:
        raise APIException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Email already exists",
        )

    password_hash = pwd_context.hash(registerDTO.password)
    print(password_hash)

    return SuccessResponse(generate_jwt_token(user), user.display_name, user.email)
