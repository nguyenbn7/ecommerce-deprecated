from typing import Annotated
from fastapi import APIRouter, Depends

from product_brand.product_brand_repo import ProductBrandRepo

router = APIRouter(
    prefix="/products/brands",
    tags=["Product Brands"]
)

@router.get("/")
def get_products_brands(repo: Annotated[ProductBrandRepo, Depends(ProductBrandRepo)]):
    return repo.get_all()