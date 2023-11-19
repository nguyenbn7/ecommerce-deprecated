from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, status
from jose import jwt
from jose.constants import ALGORITHMS
from pydantic import BaseModel
from passlib.context import CryptContext

account_router = APIRouter(prefix="/account", tags=["Account"])

# TODO: read secret key from env
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AppUser:
    email: str = "bob@test.com"
    password_hash: str = "$2b$12$Fp7ady.Xio9zdHtBGWesauueVoG8rYqGy26ARRy5EjZFA5aQW0dP."
    display_name: str = "Bob"


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


class SuccessResponse:
    def __init__(self, token: str, display_name: str, email: str) -> None:
        self.token = token
        self.display_name = display_name
        self.email = email

    token: str
    display_name: str
    email: str


class LoginDTO(BaseModel):
    email: str
    password: str


class RegisterDTO(BaseModel):
    email: str
    password: str


user = AppUser()


@account_router.post("/login")
def login(loginDTO: LoginDTO):
    if loginDTO.email != user.email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"message": "Email or Password incorrect"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not pwd_context.verify(loginDTO.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"message": "Email or Password incorrect"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    return SuccessResponse(generate_jwt_token(user), user.display_name, user.email)


@account_router.post("/register")
def register(registerDTO: RegisterDTO):
    if registerDTO.email == user.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": "Email already exists"},
        )

    password_hash = pwd_context.hash(registerDTO.password)
    print(password_hash)

    return SuccessResponse(generate_jwt_token(user), user.display_name, user.email)
