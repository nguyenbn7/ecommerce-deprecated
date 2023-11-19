from dataclasses import dataclass
from sqlalchemy import ColumnElement, ColumnExpressionArgument
from sqlalchemy.sql.expression import and_, true
from sqlalchemy.orm import Query, joinedload
from product.model import Product, ProductsParams
from share.model import Specification


def _include_product_brand_and_type(query: Query[Product]):
    return query.options(joinedload(Product.product_brand, innerjoin=True)).options(
        joinedload(Product.product_type, innerjoin=True)
    )


@dataclass(frozen=True)
class ProductSpecification(Specification):
    brand_id: int | None
    type_id: int | None

    def to_criterion(self) -> ColumnExpressionArgument[bool] | ColumnElement[bool]:
        predicates = []

        if self.brand_id:
            predicates.append(Product.product_brand_id == self.brand_id)

        if self.type_id:
            predicates.append(Product.product_type_id == self.type_id)

        if len(predicates) > 1:
            return and_(*predicates)
        if len(predicates) > 0:
            return predicates[0]
        return true()


class ProductsCountSpec(Specification):
    def __init__(self, products_params: ProductsParams) -> None:
        self.products_params = products_params

    def apply_spec(self, query: Query[Product]) -> Query[Product]:
        if self.products_params.brand_id:
            query = query.filter(
                Product.product_brand_id == self.products_params.brand_id
            )

        if self.products_params.type_id:
            query = query.filter(
                Product.product_type_id == self.products_params.type_id
            )
        return query


class ProductSpec(Specification):
    def apply_spec(self, query: Query[Product]) -> Query[Product]:
        return _include_product_brand_and_type(query)
