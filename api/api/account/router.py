from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from api.account.model import (
    ApplicationUser,
    LoginDTO,
    RegisterDTO,
    SuccessResponse,
    UserInfo,
)
from api.account.repository import UserRepository
from api.account.service import (
    generate_jwt_token,
    get_current_user,
    hash_password,
    verfiy_password,
)

account_router = APIRouter(prefix="/account", tags=["Account"])


@account_router.post("/login")
def login(
    loginDTO: LoginDTO, user_repo: Annotated[UserRepository, Depends(UserRepository)]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Email or Password incorrect",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = user_repo.get_user_by_username(loginDTO.email)

    if not user:
        raise credentials_exception

    if not verfiy_password(loginDTO.password, user.password_hash):
        raise credentials_exception

    return SuccessResponse(generate_jwt_token(user), user.email, user.display_name)


@account_router.post("/register")
def register(
    registerDTO: RegisterDTO,
    user_repo: Annotated[UserRepository, Depends(UserRepository)],
):
    user = user_repo.get_user_by_email(registerDTO.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    user = ApplicationUser()
    user.user_name = registerDTO.email
    user.email = registerDTO.email
    user.display_name = registerDTO.display_name
    user.password_hash = hash_password(registerDTO.password)

    user_repo.save(user)

    return SuccessResponse(generate_jwt_token(user), user.email, user.display_name)


@account_router.get("/info")
def get_user_basic_info(
    current_user: Annotated[ApplicationUser, Depends(get_current_user)]
):
    return UserInfo(current_user.email, current_user.display_name)
