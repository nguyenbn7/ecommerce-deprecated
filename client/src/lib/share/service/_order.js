import { SpinnerService } from "$lib/component/share/spinner/page-spinner.svelte";
import { AccountService } from ".";
import { createHttpClient } from "../httpClient";
import { delayFetch, notifyFetchError } from "../httpClient/plugin";

const httpClientAuthPageSpinner = createHttpClient();
httpClientAuthPageSpinner.interceptors.request.use(config => {
    config.headers.Authorization = `Bearer ${AccountService.getAccessToken()}`;
    SpinnerService.showSpinner();
    return config;
})
httpClientAuthPageSpinner.interceptors.response.use(async (response) => {
    await delayFetch(1000);
    SpinnerService.hideSpinner();
    return response;
}, async (error) => {
    await delayFetch(1000);
    SpinnerService.hideSpinner();
    notifyFetchError(error);
});

/**
 * @param {Order} data
 */
async function createOrder(data) {
    return await httpClientAuthPageSpinner.post('/orders/', data);
}

/**
 * @returns {Promise<string>}
 */
async function getPaymentTypes() {
    const response = await httpClientAuthPageSpinner.get('/orders/payments');
    return response.data;
}

/**
 * @returns {Promise<DeliveryMethod[]>}
 */
async function getDeliveryMethods() {
    const response = await httpClientAuthPageSpinner.get('/orders/delivery-methods');
    return response.data;
}

export const OrderService = {
    createOrder,
    getPaymentTypes,
    getDeliveryMethods
};
