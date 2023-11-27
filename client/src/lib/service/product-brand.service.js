import { PUBLIC_BASE_API_URL } from '$env/static/public';

/**
 * @returns {Promise<ProductBrand[]>}
 */
export async function getProductBrands() {
	const response = await fetch(`${PUBLIC_BASE_API_URL}/products/brands/`);
	return await response.json();
}
