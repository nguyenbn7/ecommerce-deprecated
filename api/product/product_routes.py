from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from shares.response_models import ErrorResponse
from .product_repo import ProductRepo


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def get_products(repo: Annotated[ProductRepo, Depends(ProductRepo)]):
    return repo.get_all()


@router.get("/{id}")
def get_product(id: int, repo: Annotated[ProductRepo, Depends(ProductRepo)]):
    product = repo.get_by_id(id)
    if not product:
        return JSONResponse(
            status_code=404, content=ErrorResponse("Product not found").__dict__
        )
    return product
