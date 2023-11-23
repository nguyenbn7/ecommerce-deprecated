from fastapi import APIRouter
from api.product.router import product_router
from api.product_brand.router import product_brand_router
from api.product_type.router import product_type_router
from api.account.router import account_router
from api.basket.router import basket_router


api_router = APIRouter(prefix="/api")

api_router.include_router(product_router)
api_router.include_router(product_brand_router)
api_router.include_router(product_type_router)
api_router.include_router(account_router)
api_router.include_router(basket_router)
