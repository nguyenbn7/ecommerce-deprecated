from fastapi import APIRouter

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from product import product_router
from product_brand import product_brand_router
from product_type import product_type_router
from account import account_router

# TODO: read database url from env
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/ecommerce100"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


api_router = APIRouter(prefix="/api")

api_router.include_router(product_router)
api_router.include_router(product_brand_router)
api_router.include_router(product_type_router)
api_router.include_router(account_router)
