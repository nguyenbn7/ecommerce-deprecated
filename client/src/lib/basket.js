import { writable } from "svelte/store";
import { setBasket } from "./request/cart";

/**
 * @type {import("svelte/store").Writable<Basket | null>}
 */
export const basketSource = writable(null);

function getCurrentBasket() {
    /**
     * @type {Basket | null}
     */
    let basket = null;
    const unsub = basketSource.subscribe(b => basket = b);
    unsub();
    return basket;
}

/**
 * @param {BasketItem | Product} item
 * @param {number} quantity
 */
export async function addItemToBasket(item, quantity = 1) {
    if (isProduct(item))
        item = mapProductItemToBasketItem(item);

    const basket = getCurrentBasket() ?? createBasket();
    basket.items = addOrUpdateItem(basket.items, item, quantity);
    console.log(basket);    
    await setBasket(basket);
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