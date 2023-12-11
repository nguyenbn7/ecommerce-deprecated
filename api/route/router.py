from fastapi import APIRouter
from route.products.router import product_router
from route.accounts.router import account_router
from route.baskets.router import basket_router
from route.orders.router import order_router


api_router = APIRouter(prefix="/api")

api_router.include_router(product_router)
api_router.include_router(account_router)
api_router.include_router(basket_router)
api_router.include_router(order_router)
