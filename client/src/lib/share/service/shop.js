import { httpClient, httpClientSpinner } from "../httpClient";

/**
 * @param {number} productId
 * @returns {Promise<Product>}
 */
async function getProduct(productId) {
    const response = await httpClientSpinner.get(`products/${productId}`);
    return response.data;
}

/**
 * @returns {Promise<ProductBrand[]>}
 */
async function getProductBrands() {
    const response = await httpClientSpinner.get(`products/brands/`);
    return response.data;
}

/**
 * @returns {Promise<ProductType[]>}
 */
async function getProductTypes() {
    const response = await httpClientSpinner.get(`products/types/`);
    return response.data;
}

/**
 * @param {ShopParams} shopParams
 * @returns {Promise<Page<Product>>}
 */
async function getPageProduct(shopParams) {
    const params = {};
    if (shopParams.brandId > 0) params['brandId'] = shopParams.brandId;
    if (shopParams.typeId > 0) params['typeId'] = shopParams.typeId;
    params['sort'] = shopParams.sort;
    params['pageNumber'] = shopParams.pageNumber;
    params['pageSize'] = shopParams.pageSize;
    if (shopParams.search) params['search'] = shopParams.search;

    const response = await httpClientSpinner.get('products', {
        params
    });
    return response.data;
}

/**
 * @param {ShopParams} shopParams
 */
async function loadShopData(shopParams) {
    const result = await Promise.all([
        getProductBrands(),
        getProductTypes(),
        getPageProduct(shopParams)
    ]);

    return {
        productBrands: [{ id: 0, name: 'All' }, ...result[0]],
        productTypes: [{ id: 0, name: 'All' }, ...result[1]],
        products: [...result[2].data],
        pageNumber: result[2].pageNumber,
        pageSize: result[2].pageSize,
        totalItems: result[2].totalItems
    };
}

/**
 * @returns {Promise<Product>}
 */
async function getDealProduct() {
    const response = await httpClient.get('products/deal');
    return response.data;
}
/**
 * @returns {Promise<Array<Product>>}
 */
async function getNewArrivalProducts() {
    const response = await httpClient.get('products/new-arrivals');
    return response.data;
}

export const ShopService = {
    getProduct,
    loadShopData,
    getPageProduct,
    getProductBrands,
    getProductTypes,
    getDealProduct,
    getNewArrivalProducts
};
