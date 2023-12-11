from typing import TypeVar
from sqlalchemy import func
from sqlalchemy.orm import Query

from route.products.model import Product
from share.model import Page

TEntity = TypeVar("TEntity")


def apply_predicate(
    query: Query[TEntity],
    brand_id: int | None = None,
    type_id: int | None = None,
    search: str | None = None,
):
    if brand_id:
        query = query.filter(Product.product_brand_id == brand_id)

    if type_id:
        query = query.filter(Product.product_type_id == type_id)

    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))

    return query


def apply_sort(query: Query[TEntity], sort: str | None = None):
    if not sort:
        return query.order_by(Product.name)
    match sort.lower():
        case "price":
            return query.order_by(Product.price)
        case "-price":
            return query.order_by(Product.price.desc())
        case default:
            return query.order_by(Product.name)


def to_page(
    query: Query[TEntity],
    predicate_query: Query,
    page_number: int = 1,
    page_size: int = 6,
):
    total_items = predicate_query.with_entities(func.count()).scalar()

    page_index, page_size = page_number - 1, page_size

    if page_size < 1:
        page_size = 6

    if page_index * page_size > total_items:
        page_index = 1
        page_size = 6

    data = query.offset(page_index * page_size).limit(page_size).all()

    return Page[TEntity](page_index + 1, len(data), total_items, data)
