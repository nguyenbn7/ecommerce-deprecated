import { getAccessToken } from '$lib/service/account.service';
import httpClientWithSpinner from '$lib/share/httpClient';

/**
 * @param {Order} data
 */
async function createOrder(data) {
	return await httpClientWithSpinner.post("/orders/", data, {
		headers: {
			Authorization: `Bearer ${getAccessToken() ?? ""}`
		}
	})
}
