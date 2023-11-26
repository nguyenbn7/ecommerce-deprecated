import { PUBLIC_BASE_API_URL } from "$env/static/public";
import { basketSource } from "$lib/basket";

/**
 * @param {string} id
 */
export async function getBasket(id) {
    const response = await fetch(`${PUBLIC_BASE_API_URL}/basket?id=${id}`);

    /**
     * @type {Basket}
     */
    const basket = await response.json();
    basketSource.update(() => basket);
    return basketSource;
}

/**
 * @param {Basket} basket
 */
export async function setBasket(basket) {
    const response = await fetch(`${PUBLIC_BASE_API_URL}/basket/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(basket)
    });

    /**
     * @type {Basket}
     */
    const newBasket = await response.json();
    basketSource.update(() => newBasket);
    return basketSource;
}