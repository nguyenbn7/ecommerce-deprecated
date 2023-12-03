import AccountService from '$lib/account/service';
import { httpClient } from '$lib/share/request';

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

async function getPaymentTypes() {
    const response = await httpClient.get("/orders/payments", {
        headers: {
            Authorization: `Bearer ${AccountService.getAccessToken()}`
        }
    });
    return response.data;
}

const OrderService = {
    createOrder,
    getPaymentTypes
}

export default OrderService;
