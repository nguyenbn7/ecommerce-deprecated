import { PUBLIC_BASE_API_URL } from '$env/static/public';
import { SpinnerService } from '$lib/components/share/spinner.svelte';
import { ToastService } from '$lib/components/share/toast.svelte';
import { delay } from '$lib/share/functions';
import axios, { AxiosError } from 'axios';

const httpClient = axios.create({
	baseURL: PUBLIC_BASE_API_URL,
	timeout: 5000
});

httpClient.interceptors.response.use(async (response) => {
	await delay();
	return response;
});

/**
 * @param {number} productId
 * @returns {Promise<Product>}
 */
export async function getProduct(productId) {
	try {
		SpinnerService.show();
		const response = await httpClient.get(`products/${productId}`);
		return response.data;
	} catch (error) {
		if (error instanceof AxiosError) {
			ToastService.notifyError(error.message);
		}
		// TODO: Enhance error
		// @ts-ignore
		return error;
	} finally {
		SpinnerService.hide();
	}
}

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

	const response = await httpClient.get('products', {
		params
	});
	return response.data;
}
