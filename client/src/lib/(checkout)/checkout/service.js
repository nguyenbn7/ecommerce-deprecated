import AccountService from '$lib/(account)/service';
import { apiClientAuthSpinner, httpClient } from '$lib/share/request';

/**
 * @param {Order} data
 */
async function createOrder(data) {
    return await apiClientAuthSpinner.post("/orders/", data)
}

/**
 * @returns {Promise<string>}
 */
async function getPaymentTypes() {
    const response = await apiClientAuthSpinner.get("/orders/payments");
    return response.data;
}

/**
 * @returns {Promise<DeliveryMethod[]>}
 */
async function getDeliveryMethods() {
    const response = await apiClientAuthSpinner.get("/orders/delivery-methods");
    return response.data
}

const OrderService = {
    createOrder,
    getPaymentTypes,
    getDeliveryMethods
}

export default OrderService;
