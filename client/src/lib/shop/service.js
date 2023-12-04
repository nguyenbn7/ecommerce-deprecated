import { apiClientWithSpinner } from '$lib/share/request';

/**
 * @param {number} productId
 * @returns {Promise<Product>}
 */
async function getProduct(productId) {
	const response = await apiClientWithSpinner.get(`products/${productId}`);
	return response.data;
}

/**
 * @returns {Promise<ProductBrand[]>}
 */
async function getProductBrands() {
	const response = await apiClientWithSpinner.get(`products/brands/`);
	return response.data;
}

/**
 * @returns {Promise<ProductType[]>}
 */
async function getProductTypes() {
	const response = await apiClientWithSpinner.get(`products/types/`);
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

	const response = await apiClientWithSpinner.get('products', {
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
		page_number: result[2].page_number,
		page_size: result[2].page_size,
		totalItems: result[2].total_items
	};
}

const ShopService = {
	getProduct,
	loadShopData,
	getPageProduct,
	getProductBrands,
	getProductTypes
};

export default ShopService;
