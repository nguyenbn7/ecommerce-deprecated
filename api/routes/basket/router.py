from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response
from routes.basket.model import BasketItem, CustomerBasket, CustomerBasketDTO
from routes.basket.repository import BasketRepository

basket_router = APIRouter(prefix="/basket", tags=["Basket"])


@basket_router.get("")
def get_basket(
    id: str, basket_repo: Annotated[BasketRepository, Depends(BasketRepository)]
):
    basket = basket_repo.get_basket(id)
    if not basket:
        return CustomerBasket(id)
    return basket


@basket_router.post("/")
def update_basket(
    basketDTO: CustomerBasketDTO,
    basket_repo: Annotated[BasketRepository, Depends(BasketRepository)],
):
    basket = CustomerBasket(
        basketDTO.id,
        list(map(lambda b: BasketItem(*vars(b).values()), basketDTO.items)),
    )
    return basket_repo.update_basket(basket)


@basket_router.delete("/")
def delete_basket(
    id: str, basket_repo: Annotated[BasketRepository, Depends(BasketRepository)]
):
    deleted = basket_repo.delete_basket(id)
    if not deleted:
        raise HTTPException(404)
    return Response(status_code=200)
