from fastapi import APIRouter
from routes.product.router import product_router
from routes.product_brand.router import product_brand_router
from routes.product_type.router import product_type_router
from routes.account.router import account_router
from routes.basket.router import basket_router
from routes.order.router import order_router


api_router = APIRouter(prefix="/api")

api_router.include_router(product_router)
api_router.include_router(product_brand_router)
api_router.include_router(product_type_router)
api_router.include_router(account_router)
api_router.include_router(basket_router)
api_router.include_router(order_router)
