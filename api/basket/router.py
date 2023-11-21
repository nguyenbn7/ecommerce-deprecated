from typing import Annotated
from fastapi import APIRouter, Depends, Response
from basket.model import BasketItem, CustomerBasket, CustomerBasketDTO
from basket.repository import BasketRepository
from share.model import APIException


basket_router = APIRouter(prefix="/basket", tags=["Basket"])


@basket_router.get("/")
def get_basket(
    basket_id: str, basket_repo: Annotated[BasketRepository, Depends(BasketRepository)]
):
    basket = basket_repo.get_basket(basket_id)
    if not basket:
        return CustomerBasket(basket_id)
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
    basket_id: str, basket_repo: Annotated[BasketRepository, Depends(BasketRepository)]
):
    deleted = basket_repo.delete_basket(basket_id)
    if not deleted:
        raise APIException(404)
    return Response(status_code=200)
