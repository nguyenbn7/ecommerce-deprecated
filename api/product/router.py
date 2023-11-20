from typing import Annotated
from fastapi import APIRouter, Depends
from product.model import ProductProjection, ProductsParams
from product.repository import ProductRepository

from product.specification import ProductSpecification
from share.model import APIException, Pageable, Pagination


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def get_products(
    repo: Annotated[ProductRepository, Depends(ProductRepository)],
    products_params: ProductsParams = Depends(),
):
    page_products: Pagination[ProductProjection] = repo.get_all(
        ProductSpecification(products_params.brand_id, products_params.type_id),
        Pageable(products_params.page_index, products_params.page_size),
        ProductProjection,
    )
    page_products.data = list(map(lambda p: p.to_dto(), page_products.data))
    return page_products


@product_router.get("/{id}")
def get_product(
    id: int, repo: Annotated[ProductRepository, Depends(ProductRepository)]
):
    product: ProductProjection | None = repo.get_by_id(
        id, projected_to=ProductProjection
    )
    if not product:
        raise APIException(404, "Product not found")
    return product.to_dto()
