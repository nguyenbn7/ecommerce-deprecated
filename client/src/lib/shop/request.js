import httpClientWithSpinner from '$lib/share/httpClient';

/**
 * @param {number} productId
 * @returns {Promise<Product>}
 */
async function getProduct(productId) {
    const response = await httpClientWithSpinner.get(`products/${productId}`);
    return response.data;
}

/**
 * @returns {Promise<ProductBrand[]>}
 */
async function getProductBrands() {
    const response = await httpClientWithSpinner.get(`products/brands/`);
    return response.data;
}

/**
 * @returns {Promise<ProductType[]>}
 */
async function getProductTypes() {
    const response = await httpClientWithSpinner.get(`products/types/`);
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

    const response = await httpClientWithSpinner.get('products', {
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
