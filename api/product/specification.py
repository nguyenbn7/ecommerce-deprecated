from dataclasses import dataclass
from sqlalchemy import ColumnElement, ColumnExpressionArgument
from sqlalchemy.sql.expression import and_, true
from product.model import Product
from share.model import Specification


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
