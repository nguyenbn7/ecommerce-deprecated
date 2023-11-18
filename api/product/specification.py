from sqlalchemy.orm import Query, load_only, joinedload
from product.model import Product
from share import Specification


class ProductsSpec(Specification):
    def apply_spec(self, query: Query[Product]) -> Query[Product]:
        query = query.options(joinedload(Product.product_brand, innerjoin=True))
        query = query.options(joinedload(Product.product_type, innerjoin=True))
        return query
