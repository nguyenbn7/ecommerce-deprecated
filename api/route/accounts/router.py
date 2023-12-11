from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from route.accounts.model import Authenticated, CustomerLogin, CustomerRegister, User
from route.accounts.service import (
    create_user,
    get_current_user,
    get_user_by_username,
    sign_in,
)
from share.dependency import get_db_session
from share.jwt_service import generate_jwt_token

account_router = APIRouter(prefix="/account", tags=["Account"])


@account_router.post("/login")
def login(
    customer_login: CustomerLogin,
    db_session: Annotated[Session, Depends(get_db_session)],
):
    user = sign_in(db_session, customer_login.email, customer_login.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or Password incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    claims = {"sub": user.user_name}

    return Authenticated(generate_jwt_token(claims), user.email, user.display_name)


@account_router.post("/register")
def register(
    customer_register: CustomerRegister,
    db_session: Annotated[Session, Depends(get_db_session)],
):
    user = get_user_by_username(db_session, customer_register.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    user = create_user(
        db_session,
        customer_register.email,
        customer_register.email,
        customer_register.displayName,
        customer_register.password,
    )

    claims = {"sub": user.user_name}

    return Authenticated(generate_jwt_token(claims), user.email, user.display_name)


@account_router.get("/display")
def get_email_and_display_name(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return {"email": current_user.email, "displayName": current_user.display_name}
