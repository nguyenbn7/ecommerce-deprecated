import { PUBLIC_BASE_API_URL } from '$env/static/public';

/**
 * @param {ShopParams} shopParams
 * @returns {Promise<Page<Product>>}
 */
export async function getPageProduct(shopParams) {
	const params = {};
	if (shopParams.brand_id > 0) params['brand_id'] = shopParams.brand_id;
	if (shopParams.type_id > 0) params['type_id'] = shopParams.type_id;
	params['sort'] = shopParams.sort;
	params['page_number'] = shopParams.page_number;
	params['page_size'] = shopParams.page_size;
	if (shopParams.search) params['search'] = shopParams.search;

	let paramsStr = Object.entries(params)
		.map((k) => `${k[0]}=${k[1]}`)
		.join('&');

	let param = paramsStr.length ? '?' + paramsStr : '';

	const response = await fetch(`${PUBLIC_BASE_API_URL}/products${param}`);
	return await response.json();
}

/**
 * @param {string} productId
 * @returns {Promise<Product>}
 */
export async function getProduct(productId) {
	const response = await fetch(`${PUBLIC_BASE_API_URL}/products/${productId}`);
	return await response.json();
}
