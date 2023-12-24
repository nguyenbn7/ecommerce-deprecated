import { get, readonly, writable } from 'svelte/store';
import { httpClient, httpClientSpinner } from '../httpClient';

const BASKET_ID = 'basketId';

/**
 * @type {import("svelte/store").Writable<Basket | null>}
 */
const basketSource = writable(null);
/**
 * @type {import("svelte/store").Writable<BasketTotals | null>}
 */
const basketTotalsSource = writable(null);

/**
 * @param {string} id
 */
async function getBasket(id) {
    /**
     * @type {Basket}
     */
    const newBasket = (await httpClient.get(`basket?id=${id}`)).data;
    basketSource.update(() => newBasket);
    calculateTotals();
}

/**
 * @param {Basket} basket
 */
async function setBasket(basket) {
    /**
     * @type {Basket}
     */
    const newBasket = (await httpClientSpinner.post(`basket/`, basket)).data;
    basketSource.update(() => newBasket);
    calculateTotals();
}

/**
 * @param {Basket} basket
 */
async function deleteBasket(basket) {
    const response = await httpClientSpinner.delete(`basket?id=${basket.id}`);

    if (response.status === 200) {
        basketSource.update(() => null);
        basketTotalsSource.update(() => null);
        return;
    }
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
    // TODO: set key here
    const basket = {
        id: 'basket1',
        items: []
    };
    localStorage.setItem(BASKET_ID, basket.id);
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
        picture_url: item.pictureUrl,
        brand: item.productBrand,
        type: item.productType
    };
}

/**
 * @param {BasketItem | Product} item
 * @returns {item is Product}
 */
function isProduct(item) {
    return Object.hasOwn(item, 'productBrand');
}

function calculateTotals() {
    const basket = get(basketSource);
    if (!basket) return;
    const shipping = 0;
    const subtotal = basket.items.reduce((total, item) => total + item.price * item.quantity, 0);
    const total = subtotal + shipping;
    basketTotalsSource.update(() => ({ shipping, subtotal, total }));
}

async function loadBasketBackground() {
    const basketId = localStorage.getItem(BASKET_ID);
    if (basketId) await getBasket(basketId);
}

/**
 * @param {BasketItem | Product} item
 * @param {number} quantity
 */
async function addItemToBasket(item, quantity = 1) {
    if (isProduct(item)) item = mapProductItemToBasketItem(item);

    const basket = get(basketSource) ?? createBasket();
    basket.items = addOrUpdateItem(basket.items, item, quantity);
    await setBasket(basket);
}

/**
 * @param {number} id
 */
function removeItemFromBasket(id, quantity = 1) {
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

export const basketTotals = readonly(basketTotalsSource);
export const basket = readonly(basketSource);

export const BasketService = {
    removeItemFromBasket,
    addItemToBasket,
    loadBasketBackground
};

