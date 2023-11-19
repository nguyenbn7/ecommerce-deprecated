from typing import Annotated
from fastapi import APIRouter, Depends
from product.model import ProductsParams, map_to_dto, map_to_dtos
from product.repository import ProductRepository

from product.specification import ProductSpec, ProductSpecification
from share.model import APIException, Pageable, Pagination


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def get_products(
    repo: Annotated[ProductRepository, Depends(ProductRepository)],
    products_params: ProductsParams = Depends(),
):
    # TODO: add join
    return repo.get_all(
        ProductSpecification(products_params.brand_id, products_params.type_id),
        Pageable(products_params.page_index, products_params.page_size),
    )


@product_router.get("/{id}")
def get_product(
    id: int, repo: Annotated[ProductRepository, Depends(ProductRepository)]
):
    # spec = ProductSpec()
    product = repo.get_by_id(id)
    if not product:
        raise APIException(404, "Product not found")
    return map_to_dto(product)
