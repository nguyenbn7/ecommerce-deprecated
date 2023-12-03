import AccountService from '$lib/account/service';
import { SpinnerService } from '$lib/components/share/spinner.svelte';
import { ToastService } from '$lib/components/share/toast.svelte';
import { delay, httpClient } from '$lib/share/request';
import { AxiosError } from 'axios';

httpClient.interceptors.request.use(config => {
	SpinnerService.show();
	return config;
})

httpClient.interceptors.response.use(async (response) => {
	await delay();
	SpinnerService.hide();
	return response;
}, error => {
	if (error instanceof AxiosError) {
		const response = error.response;
		let errorMessage = error.message;
		if (response) {
			errorMessage = response.data.message
		}
		ToastService.notifyError(errorMessage);
		console.log(error)
	}
	SpinnerService.hide();
	throw error;
});

/**
 * @param {Order} data
 */
async function createOrder(data) {
	return await httpClient.post("/orders/", data, {
		headers: {
			Authorization: `Bearer ${AccountService.getAccessToken()}`
		}
	})
}

const OrderHttpClient = {
	createOrder
}

export default OrderHttpClient;
