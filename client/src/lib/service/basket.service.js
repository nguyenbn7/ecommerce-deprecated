import { PUBLIC_BASE_API_URL } from '$env/static/public';
import { get, readonly, writable } from 'svelte/store';

/**
 * @type {import("svelte/store").Writable<Basket | undefined>}
 */
const _basket = writable(undefined);
/**
 * @type {import("svelte/store").Writable<BasketTotals | undefined>}
 */
const _basketTotals = writable(undefined);
const BASKET_KEY_NAME = 'basket_id';

export const basketTotals = readonly(_basketTotals);
export const basket = readonly(_basket);

/**
 * @param {string} id
 */
async function getBasket(id) {
	const response = await fetch(`${PUBLIC_BASE_API_URL}/basket?id=${id}`);
	const newBasket = await response.json();
	_basket.update(() => newBasket);
	calculateTotals();
}

/**
 * @param {Basket} basket
 */
async function setBasket(basket) {
	const response = await fetch(`${PUBLIC_BASE_API_URL}/basket/`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(basket)
	});
	const newBasket = await response.json();
	_basket.update(() => newBasket);
	calculateTotals();
}

/**
 * @param {Basket} basket
 */
async function deleteBasket(basket) {
	const response = await fetch(`${PUBLIC_BASE_API_URL}/basket?id=${basket.id}`, {
		method: 'DELETE',
		headers: {
			'Content-Type': 'application/json'
		}
	});

	if (response.status === 200) {
		_basket.update(() => undefined);
		_basketTotals.update(() => undefined);
		return;
	}
	console.error('Error: ', response.status);
	console.error('Detail: ', response.json());
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
	localStorage.setItem(BASKET_KEY_NAME, basket.id);
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
		type: item.product_type
	};
}

/**
 * @param {BasketItem | Product} item
 * @returns {item is Product}
 */
function isProduct(item) {
	return Object.hasOwn(item, 'product_brand');
}

function calculateTotals() {
	const basket = get(_basket);
	if (!basket) return;
	const shipping = 0;
	const subtotal = basket.items.reduce((total, item) => total + item.price * item.quantity, 0);
	const total = subtotal + shipping;
	_basketTotals.update(() => ({ shipping, subtotal, total }));
}

export async function loadBasket() {
	const basketId = localStorage.getItem(BASKET_KEY_NAME);
	if (basketId) await getBasket(basketId);
}

/**
 * @param {BasketItem | Product} item
 * @param {number} quantity
 */
export async function addItemToBasket(item, quantity = 1) {
	if (isProduct(item)) item = mapProductItemToBasketItem(item);

	const basket = get(_basket) ?? createBasket();
	basket.items = addOrUpdateItem(basket.items, item, quantity);
	await setBasket(basket);
}

/**
 * @param {number} id
 */
export function removeItemFromBasket(id, quantity = 1) {
	const basket = get(_basket);
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
