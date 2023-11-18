from typing import Annotated
from fastapi import APIRouter, Depends
from product.model import map_to_dto, map_to_dtos
from product.repository import ProductRepository

from product.specification import ProductSpec, ProductsSpec
from share import NotFoundException


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def get_products(repo: Annotated[ProductRepository, Depends(ProductRepository)]):
    spec = ProductsSpec()
    products = repo.get_all(specification=spec)
    return map_to_dtos(products)


@product_router.get("/{id}")
def get_product(
    id: int, repo: Annotated[ProductRepository, Depends(ProductRepository)]
):
    spec = ProductSpec()
    product = repo.get_by_id(id, spec)
    if not product:
        raise NotFoundException("Product not found")
    return map_to_dto(product)
