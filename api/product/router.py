from typing import Annotated
from fastapi import APIRouter, Depends
from product.repository import ProductRepository

from product.specification import ProductSpec, ProductsSpec
from share import NotFoundException


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def get_products(repo: Annotated[ProductRepository, Depends(ProductRepository)]):
    spec = ProductsSpec()
    products = repo.get_all(specification=spec)
    # TODO: add prefix of url
    for product in products:
        product.picture_url = f"http://localhost:8000/{product.picture_url}"
    return products


@product_router.get("/{id}")
def get_product(
    id: int, repo: Annotated[ProductRepository, Depends(ProductRepository)]
):
    spec = ProductSpec()
    product = repo.get_by_id(id, spec)
    if not product:
        raise NotFoundException("Product not found")
    return product
