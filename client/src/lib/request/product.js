import { PUBLIC_BASE_API_URL } from "$env/static/public";

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

    let paramsStr = Object.entries(params)
        .map((k) => `${k[0]}=${k[1]}`)
        .join('&');

    let param = paramsStr.length ? '?' + paramsStr : '';

    const response = await fetch(`${PUBLIC_BASE_API_URL}/products${param}`);
    return await response.json();
}

/**
 * @returns {Promise<ProductBrand[]>}
 */
async function getProductBrands() {
    const response = await fetch(`${PUBLIC_BASE_API_URL}/products/brands/`);
    return await response.json();
}

/**
 * @returns {Promise<ProductType[]>}
 */
async function getProductTypes() {
    const response = await fetch(`${PUBLIC_BASE_API_URL}/products/types/`);
    return await response.json();
}

export {
    getPageProduct,
    getProductTypes,
    getProductBrands
}