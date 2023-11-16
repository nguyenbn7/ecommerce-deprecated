from typing import Annotated
from fastapi import APIRouter, Depends

from product_type.product_type_repo import ProductTypeRepo

router = APIRouter(prefix="/products/types", tags=["Product Types"])


@router.get("/")
def get_products_types(repo: Annotated[ProductTypeRepo, Depends(ProductTypeRepo)]):
    return repo.get_all()
