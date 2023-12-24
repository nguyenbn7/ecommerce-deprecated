import { httpClientAuthSpinner } from '$lib/share/httpClient';

/**
 * @param {Order} data
 */
async function createOrder(data) {
    return await httpClientAuthSpinner.post('/orders/', data);
}

/**
 * @returns {Promise<string>}
 */
async function getPaymentTypes() {
    const response = await httpClientAuthSpinner.get('/orders/payments');
    return response.data;
}

/**
 * @returns {Promise<DeliveryMethod[]>}
 */
async function getDeliveryMethods() {
    const response = await httpClientAuthSpinner.get('/orders/delivery-methods');
    return response.data;
}

export const OrderService = {
    createOrder,
    getPaymentTypes,
    getDeliveryMethods
};
