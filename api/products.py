from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def get_products():
    return "List of products here"


@router.get("/{product_id}")
def get_product(product_id: int):
    return f"Get product with product id: {product_id}"
