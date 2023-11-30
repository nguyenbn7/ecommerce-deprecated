from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from routes.product.model import Product, ProductProjection, ProductsParams
from routes.product.repository import ProductRepository

from routes.product.specification import ProductSpecification
from share.model import Pageable, Page, SortOption, SortDirection


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def get_products(
    repo: Annotated[ProductRepository, Depends(ProductRepository)],
    products_params: Annotated[ProductsParams, Depends(ProductsParams)],
):
    sort_options = []
    if products_params.sort:
        match products_params.sort.lower():
            case "price":
                sort_options.append(SortOption(Product.price))
            case "-price":
                sort_options.append(SortOption(Product.price, SortDirection.DESC))
            case default:
                sort_options.append(SortOption(Product.name))
    else:
        sort_options.append(SortOption(Product.name))

    page_products: Page[ProductProjection] = repo.get_all(
        specification=ProductSpecification(
            products_params.brand_id, products_params.type_id, products_params.search
        ),
        sort_by=sort_options,
        pageable=Pageable(products_params.page_number - 1, products_params.page_size),
        projected_to=ProductProjection,
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
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product.to_dto()
