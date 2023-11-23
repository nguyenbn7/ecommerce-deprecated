from typing import Annotated
from fastapi import APIRouter, Depends

from api.product_brand.repository import ProductBrandRepository


product_brand_router = APIRouter(prefix="/products/brands", tags=["Product Brands"])


@product_brand_router.get("/")
def get_products_brands(
    repo: Annotated[ProductBrandRepository, Depends(ProductBrandRepository)]
):
    return repo.get_all()
