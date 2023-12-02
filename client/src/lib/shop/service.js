import ShopHttpClient from './request';

/**
 * @param {number} productId
 */
async function getProduct(productId) {
    return ShopHttpClient.getProduct(productId);
}

/**
 * @param {ShopParams} shopParams
 */
async function loadShopData(shopParams) {
    const result = await Promise.all([
        ShopHttpClient.getProductBrands(),
        ShopHttpClient.getProductTypes(),
        ShopHttpClient.getPageProduct(shopParams)
    ]);

    return {
        productBrands: [{ id: 0, name: 'All' }, ...result[0]],
        productTypes: [{ id: 0, name: 'All' }, ...result[1]],
        products: [...result[2].data],
        page_number: result[2].page_number,
        page_size: result[2].page_size,
        totalItems: result[2].total_items,
    }
}

const ShopService = {
    getProduct,
    loadShopData
};

export default ShopService;
