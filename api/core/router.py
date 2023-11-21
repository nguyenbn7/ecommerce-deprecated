from fastapi import APIRouter
from product.router import product_router
from product_brand.router import product_brand_router
from product_type.router import product_type_router
from auth.account import account_router
from basket.router import basket_router


api_router = APIRouter(prefix="/api")

api_router.include_router(product_router)
api_router.include_router(product_brand_router)
api_router.include_router(product_type_router)
api_router.include_router(account_router)
api_router.include_router(basket_router)
