import { PUBLIC_BASE_API_URL } from "$env/static/public";
import { get, writable } from "svelte/store";

/**
 * @type {import("svelte/store").Writable<Basket | null>}
 */
export const basketSource = writable(null);

/**
 * @type {import("svelte/store").Writable<BasketTotals | null>}
 */
export const basketTotalsSource = writable(null);

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
    calculateTotals();
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
    calculateTotals();
    return basketSource;
}

/**
 * @param {Basket} basket
 */
export async function deleteBasket(basket) {
    const response = await fetch(`${PUBLIC_BASE_API_URL}/basket?id=${basket.id}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    });

    if (response.status === 200) {
        basketSource.update(() => null);
        basketTotalsSource.update(() => null);
        return basketSource;
    }
    console.log(response.json());
    return basketSource;
}

/**
 * @param {BasketItem | Product} item
 * @param {number} quantity
 */
export async function addItemToBasket(item, quantity = 1) {
    if (isProduct(item))
        item = mapProductItemToBasketItem(item);

    const basket = get(basketSource) ?? createBasket();
    basket.items = addOrUpdateItem(basket.items, item, quantity);
    await setBasket(basket);
}

export async function loadBasket() {
    const basketId = localStorage.getItem('basket_id');
    if (basketId) await getBasket(basketId);
}

/**
 * @param {BasketItem[]} items
 * @param {BasketItem} itemToAdd
 * @param {number} quantity
 */
function addOrUpdateItem(items, itemToAdd, quantity) {
    const item = items.find((i) => i.id === itemToAdd.id);
    if (item) item.quantity += quantity;
    else {
        itemToAdd.quantity = quantity;
        items.push(itemToAdd);
    }
    return items;
}

function createBasket() {
    /**
     * @type {Basket}
     */
    const basket = {
        id: "basket1",
        items: []
    };
    localStorage.setItem('basket_id', basket.id);
    return basket;
}

/**
 * @param {Product} item
 * @returns {BasketItem}
 */
function mapProductItemToBasketItem(item) {
    return {
        id: item.id,
        product_name: item.name,
        price: item.price,
        quantity: 0,
        picture_url: item.picture_url,
        brand: item.product_brand,
        type: item.product_type,
    };
}

/**
 * @param {BasketItem | Product} item
 * @returns {item is Product}
 */
function isProduct(item) {
    return Object.hasOwn(item, "product_brand");
}

function calculateTotals() {
    const basket = get(basketSource);
    if (!basket) return;
    const shipping = 0;
    const subtotal = basket.items.reduce(
        (total, item) => total + item.price * item.quantity,
        0
    );
    const total = subtotal + shipping;
    basketTotalsSource.update(() => ({ shipping, subtotal, total }));
}

/**
 * @param {number} id
 */
export function removeItemFromBasket(id, quantity = 1) {
    const basket = get(basketSource);
    if (!basket) return;
    const item = basket.items.find((i) => i.id === id);
    if (item) {
        item.quantity -= quantity;
        if (item.quantity <= 0) {
            basket.items = basket.items.filter((i) => i.id !== id);
        }
        if (basket.items.length > 0) setBasket(basket);
        else deleteBasket(basket);
    }
}