from fastapi import APIRouter

from sqlalchemy import create_engine

from product import product_router
from product_brand import product_brand_router
from product_type import product_type_router
from account import account_router


api_router = APIRouter(prefix="/api")

api_router.include_router(product_router)
api_router.include_router(product_brand_router)
api_router.include_router(product_type_router)
api_router.include_router(account_router)
