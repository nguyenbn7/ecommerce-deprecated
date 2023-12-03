import { SpinnerService } from "$lib/components/share/spinner.svelte";
import { ToastService } from "$lib/components/share/toast.svelte";
import { delay, httpClient } from "$lib/share/request";
import { AxiosError } from "axios";

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
 * @param {number} productId
 * @returns {Promise<Product>}
 */
async function getProduct(productId) {
    const response = await httpClient.get(`products/${productId}`);
    return response.data;
}

/**
 * @returns {Promise<ProductBrand[]>}
 */
async function getProductBrands() {
    const response = await httpClient.get(`products/brands/`);
    return response.data;
}

/**
 * @returns {Promise<ProductType[]>}
 */
async function getProductTypes() {
    const response = await httpClient.get(`products/types/`);
    return response.data;
}

/**
 * @param {ShopParams} shopParams
 * @returns {Promise<Page<Product>>}
 */
async function getPageProduct(shopParams) {
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

const ShopHttpClient = {
    getPageProduct,
    getProduct,
    getProductBrands,
    getProductTypes
};

export default ShopHttpClient;
