from fastapi import APIRouter

router = APIRouter(
    prefix="/products/brands",
    tags=["Product Brands"]
)

@router.get("/")
def get_products_brands():
    return "List of product brands"