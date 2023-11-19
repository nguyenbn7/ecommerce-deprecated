from sqlalchemy.orm import Query, joinedload
from product.model import Product
from share.database import Specification


class ProductsSpec(Specification):
    def apply_spec(self, query: Query[Product]) -> Query[Product]:
        query = query.options(joinedload(Product.product_brand, innerjoin=True))
        query = query.options(joinedload(Product.product_type, innerjoin=True))
        return query

class ProductSpec(Specification):
    def apply_spec(self, query: Query[Product]) -> Query[Product]:
        query = query.options(joinedload(Product.product_brand, innerjoin=True))
        query = query.options(joinedload(Product.product_type, innerjoin=True))
        return query
