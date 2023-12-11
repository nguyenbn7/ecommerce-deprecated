from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from route.products.model import (
    ProductBrand,
    ProductType,
    Product,
    ProductsQueryParams,
    ProjectedProduct,
)
from route.products.service import apply_predicate, apply_sort, to_page
from share.dependency import get_db_session

from share.model import Page


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def get_products(
    db_session: Annotated[Session, Depends(get_db_session)],
    params: Annotated[ProductsQueryParams, Depends(ProductsQueryParams)],
):
    query = db_session.query(ProjectedProduct)

    query = apply_sort(
        apply_predicate(query, params.brandId, params.typeId, params.search),
        params.sort,
    )

    count_query = apply_predicate(
        db_session.query(Product), params.brandId, params.typeId, params.search
    )

    page_products = to_page(query, count_query, params.pageNumber, params.pageSize)

    return Page(
        page_products.pageNumber,
        page_products.pageSize,
        page_products.totalItems,
        list(map(lambda p: p.to_dto(), page_products.data)),
    )


@product_router.get("/types")
def get_product_types(db_session: Annotated[Session, Depends(get_db_session)]):
    return db_session.query(ProductType).all()


@product_router.get("/brands")
def get_product_brands(db_session: Annotated[Session, Depends(get_db_session)]):
    return db_session.query(ProductBrand).all()


@product_router.get("/{id}")
def get_product(
    id: int,
    db_session: Annotated[Session, Depends(get_db_session)],
):
    projected_product = (
        db_session.query(ProjectedProduct).filter(Product.id == id).first()
    )

    if not projected_product:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Product not found")

    return projected_product.to_dto()
