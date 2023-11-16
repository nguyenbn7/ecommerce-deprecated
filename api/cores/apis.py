from fastapi import APIRouter
from product.product_routes import router as products_router
from product_brand.product_brand_routes import router as products_brands_router
from product_type.product_type_routes import router as products_types_router
from auth.account_routes import router as account_router

router = APIRouter(prefix="/api")

router.include_router(products_router)
router.include_router(products_brands_router)
router.include_router(products_types_router)
router.include_router(account_router)
