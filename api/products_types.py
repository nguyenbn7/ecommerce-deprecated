from fastapi import APIRouter

router = APIRouter(prefix="/products/types", tags=["Product Types"])


@router.get("/")
def get_products_types():
    return "List of product types"
