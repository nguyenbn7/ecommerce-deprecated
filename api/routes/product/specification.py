from dataclasses import dataclass
from sqlalchemy import ColumnElement, ColumnExpressionArgument
from sqlalchemy.sql.expression import and_, true
from routes.product.model import Product
from share.model import Specification


@dataclass(frozen=True)
class ProductSpecification(Specification):
    brand_id: int | None = None
    type_id: int | None = None
    search_term: str | None = None

    def to_criterion(self) -> ColumnExpressionArgument[bool] | ColumnElement[bool]:
        predicates = []

        if self.brand_id:
            predicates.append(Product.product_brand_id == self.brand_id)

        if self.type_id:
            predicates.append(Product.product_type_id == self.type_id)

        if self.search_term:
            predicates.append(Product.name.ilike(f"%{self.search_term}%"))

        if len(predicates) > 1:
            return and_(*predicates)
        if len(predicates) > 0:
            return predicates[0]
        return true()
