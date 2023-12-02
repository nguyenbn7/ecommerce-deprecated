from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from routes.account.model import (
    ApplicationUser,
    LoginDTO,
    RegisterDTO,
    SuccessResponse,
    UserInfo,
)
from routes.account.repository import UserRepository
from routes.account.service import (
    create_user,
    generate_jwt_token,
    get_current_user,
    sign_in,
)

account_router = APIRouter(prefix="/account", tags=["Account"])


@account_router.post("/login")
def login(
    loginDTO: LoginDTO, user_repo: Annotated[UserRepository, Depends(UserRepository)]
):
    user = sign_in(user_repo, loginDTO.email, loginDTO.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or Password incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

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
    user.email = registerDTO.email.strip()
    user.display_name = registerDTO.display_name.strip()
    user.user_name = user.email

    user = create_user(user_repo, user, registerDTO.password)

    return SuccessResponse(generate_jwt_token(user), user.email, user.display_name)


@account_router.get("/display")
def get_user_basic_info(
    current_user: Annotated[ApplicationUser, Depends(get_current_user)]
):
    return UserInfo(current_user.email, current_user.display_name)


# @account_router.get("/profile")
# def get_user_basic_info(
#     current_user: Annotated[ApplicationUser, Depends(get_current_user)],

# ):
#     return UserInfo(current_user.email, current_user.display_name)
